from distutils.core import setup
from setuptools import setup

with open('Readme.rst', 'r') as f:
        long_description = f.read()

setup(
    zip_safe=False,
    name='cheerio',
    version=1.1,
    author='Lucy Wyman',
    author_email='wyman.lucy@gmail.com',
    description='Pseudo-randomly generated goodbyes',
    long_description=long_description,
    packages=['cheerio'],
    include_package_data=True,
    keywords=['goodbye', 'cheerio'],
    url='https://github.com/lucywyman/cheerio',
)
