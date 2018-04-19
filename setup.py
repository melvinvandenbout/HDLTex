import io
import os


import numpy
from setuptools import Extension
from setuptools import setup, find_packages

__author__ = 'Kamran Kowsari <kowsari.net>'


def readme():
    with open('README.md') as f:
        return f.read()


def readfile(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(path, encoding='utf8').read()


setup(
    name='HDLTex',
    version='1.0.2',
    description='HDLTex: Hierarchical Deep Learning for Text Classification',
    long_description=readfile('README.md'),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
    url='https://github.com/kk7nc/HDLTex',
    author='Kamran Kowsari',
    author_email='kk7nc@virginia.edu',
    packages=['HDLTex'] + find_packages('HDLTex'),
    install_requires=[
        'matplotlib==2.1.2',
        'numpy==1.12.1',
        'pandas==0.22.0',
        'scipy',
        'tensorflow-gpu',
        'keras==2.0.9',
        'scikit-learn==0.19.0',
        'nltk==3.2.4'
    ],
    include_package_data=False
)