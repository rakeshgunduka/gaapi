import sys

if sys.version_info < (2, 7):
  print('gaapi requires python version >= 2.7.',
        file=sys.stderr)
  sys.exit(1)
if (3, 1) <= sys.version_info < (3, 3):
  print('gaapi requires python3 version >= 3.3.',
        file=sys.stderr)
  sys.exit(1)

from setuptools import setup
import gaapi

setup(
    name="gaapi",
    version=gaapi.__version__,
    description="A light weight python wrapper for Google’s Analytics Reporting API v4 written upon Google API Python Client.",
    long_description="""Google analytics python api wrapper for Google’s Analytics Reporting API v4 using Googles API python client. Additionally also enables caching.""",
    author="Rakesh Gunduka",
    author_email="rakesh.gunduka@gmail.com",
    url="http://github.com/rakesh/gaapi/",
    install_requires=["google-api-python-client", "google-auth", "walrus"],
    packages=["gaapi"],
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
    ],
)
