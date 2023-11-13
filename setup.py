from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="0.9",
    author="Yule Kang",
    author_email="yulekang@fau.de",
    packages=find_packages(),
    install_requires=["numpy"]
)