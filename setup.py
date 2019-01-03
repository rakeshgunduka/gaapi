__version__ = '0.1.4'

from setuptools import setup

setup(
    name="gaapi",
    version=__version__,
    description="A light weight python wrapper for Google's Analytics Reporting API v4 written upon Google API Python Client.",
    long_description="""Google analytics python api wrapper for Google's Analytics Reporting API v4 using Googles API python client. Additionally also enables caching.""",
    author="Rakesh Gunduka",
    author_email="rakesh.gunduka@gmail.com",
    url="http://github.com/rakeshgunduka/gaapi/",
    install_requires=["google-api-python-client", "google-auth", "walrus"],
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
