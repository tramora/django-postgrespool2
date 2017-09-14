#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

required = [
    'psycopg2',
    'sqlalchemy'
]

setup(
    name='django-postgrespool2',
    version='0.1.0',
    description='Postgres Connection Pooling for Django.',
    long_description=open('README.rst').read(),
    author='lcd1232',
    author_email='malexey1984@gmail.com',
    url='https://github.com/lcd1232/django-postgrespool2',
    packages= ['django_postgrespool2'],
    install_requires=required,
    license='MIT',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
)
