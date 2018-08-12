import sys

if sys.version_info < (2, 7):
  print('ga-api-python-client requires python version >= 2.7.',
        file=sys.stderr)
  sys.exit(1)
if (3, 1) <= sys.version_info < (3, 3):
  print('ga-api-python-client requires python3 version >= 3.3.',
        file=sys.stderr)
  sys.exit(1)

from setuptools import setup
import gaclient

setup(
    name="ga-api-python-client",
    version=gaclient.__version__,
    description="Google Analytics API Client Library for Python",
    long_description="""The Google Analytics API Client for Python is a client library for
    accessing google analytics api.""",
    author="Rakesh Gunduka",
    author_email="rakesh.gunduka@gmail.com",
    url="http://github.com/rakesh/ga-api-python-client/",
    install_requires=["google-api-python-client", "oauth2client", "walrus"],
    packages=["gaclient"],
    package_data={},
    license="http://www.opensource.org/licenses/mit-license.php",
    keywords="google analytics api client",
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
