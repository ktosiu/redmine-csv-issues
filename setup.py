# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages


setup (
    name = "Redmine Importer",
    version = "0.1",
    description="Tool for importing issues to Redmine",
    author="Michał Rzeszut",
    author_email="rzeszut.michal@gmail.com",
    url="http://www.rzeszut.eu",
    packages = find_packages(exclude="test"),
    entry_points = {
        'console_scripts': ['redimport = redmine_csv_issues.main:main']
        },
    test_suite='tests'
)
