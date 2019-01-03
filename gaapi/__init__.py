import re
import hashlib
import pickle

from apiclient.discovery import build
from google.oauth2 import service_account

from walrus import Database

class InvalidJsonError(Exception):
    code = 400
    msg = 'Invalid json request'


def _decamelify(obj):
    func = lambda string: re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()
    return modify_object(obj, func)


def _camelify(obj):
    func = lambda string: re.sub(r'_(\w)', lambda match: match.group(1).upper(), string)
    return modify_object(obj, func)


def modify_object(obj, func):
    if isinstance(obj, dict):
        temp_obj = {}
        for key in obj:
            temp_obj[func(key)] = modify_object(obj[key], func)
        return temp_obj
    if isinstance(obj, list):
        temp_obj = []
        for key in obj:
            temp_obj.append(modify_object(key, func))
        return temp_obj
    if isinstance(obj, bool):
        return obj
    if isinstance(obj, str) and not obj.isupper():
        return func(obj)
    return obj


class Query(object):
    def __init__(self):
        self.query = {}

    def __getattr__(self, name):
        def f(*args, **kw):
            if not getattr(self.query, name, None):
                self.query.setdefault(name, [])
            clean = kw.pop('clean', None)
            if clean:
                self.query[name] = []
            if args:
                self.query[name] = args
            elif kw:
                self.query[name].append(kw)
            return self
        return f

    def json(self, camelify=False):
        if camelify:
            return _camelify(self.query)
        return self.query

    def clone(self, query):
        self.query.update(query.json())
        return self


class Client(object):

    def __init__(self, credentials, view_id, redis_args=None):
        credentials = service_account.Credentials.from_service_account_info(credentials)
        # Build the service object.
        self.redis_args = redis_args or {}
        self.view_id = view_id
        self.build(credentials)


    def build(self, credentials):
        self.analytics = build('analyticsreporting', 'v4', credentials=credentials).reports().batchGet


    def batch_get(self, query=None, cache_ttl=None):
        cache_on = bool(cache_ttl)
        if isinstance(obj, Query):
            request_params = obj.json(camelify=True)
        elif isinstance(obj, dict):
            request_params = _camelify(obj)
        else:
            raise InvalidJsonError()
        request_params['viewId'] = self.view_id
        self.request_query = {
            'reportRequests': request_params
        }
        execute = self.analytics(body=self.request_query).execute
        if cache_on:
            if not self.cache:
                self.cache = Database(**redis_args).cache()
            deco = self.cache.cached(self.key_fn, timeout=self.cache_ttl, metrics=True)
            execute = deco(execute)
        resp = execute()
        return resp

    def key_fn(self, a, k):
        return hashlib.md5(
            pickle.dumps((self.request_query, a, k))
        ).hexdigest()

    def __getattr__(self, name):
        if name == 'query':
            return Query()


class RTClient(Client):

    def build(self, credentials):
        self.analytics = build('analytics', 'v3', credentials=credentials).data().realtime().get


    def get(self, *args, **kw):
        resp = self.analytics(**kw).execute()
        return resp
