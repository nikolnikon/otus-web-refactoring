from setuptools import setup, find_packages
from os.path import join, dirname

with open(join(dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='code_stat',
    version='0.0.1',
    description='Библиотека для сбора статистики по использованию слов в названиях функций',
    long_description=README,
    author='N.Nikonov',
    author_email='nikolnikon@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    install_requires=[
        'nltk ~= 3.2.0',
    ],
)
