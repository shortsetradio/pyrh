from setuptools import setup
from setuptools import find_packages

# get version
def get_version():
    '''Tries to get version from pyrh/__init__.py'''
    version = 'unknown'
    with open('./pyrh/__init__.py') as fin:
        init_file = fin.readlines()
    for line in init_file:
        if '__version__ = ' in line:
            version = line.replace('__version__ = ', '').replace('\n', '').replace('"', '')
    return version


setup(name='pyrh',
      version=get_version(),
      description='Unofficial Python API, custom4tandr',
      author='',
      author_email='',
      url='',
      download_url='',
      license='',
      install_requires=[],
      extras_require={},
      packages=find_packages())