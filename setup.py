#!/usr/bin/env python
import io

from setuptools import setup, find_packages


long_description = io.open('README.md', encoding='utf-8').read()

METADATA = dict(
    name='django-allauth-correctiv',
    version='0.0.1',
    author='Stefan Wehrmeyer',
    author_email='stefan.wehrmeyer@correctiv.org',
    description='Django applications addressing'
    ' authentication with Correctiv.org as a django-allauth module',
    long_description=long_description,
    url='http://github.com/correctiv/django-allauth-correctiv',
    keywords='django auth account social oauth correctiv registration',
    tests_require=[],
    install_requires=['django-allauth'],
    include_package_data=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    packages=find_packages(),
)

if __name__ == '__main__':
    setup(**METADATA)
