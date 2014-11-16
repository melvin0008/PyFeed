from setuptools import setup
setup(
    name = 'feedzilla-api',
    packages = ['pyfeed'], 
    version = '0.3',
    description = 'Unofficial Feedzilla Python API Wrapper',
    author = 'Melvin Philips',
    author_email = 'me@melvinphilips.com',
    url = 'https://github.com/melvin0008/PyFeed',
    download_url = 'https://github.com/melvin0008/PyFeed/tarball/0.3',
    keywords = ['feedzilla-api', 'api', 'feedzilla','feedzilla-wrapper'], 
    classifiers = [],  
    install_requires=[
          'simplejson',
      ],
      zip_safe=False
    )