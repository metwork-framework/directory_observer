#!/usr/bin/env python
import fastentrypoints  # noqa: F401
import sys
from setuptools import setup
from setuptools import find_packages

required = []
dependency_links = []
EGG_MARK = '#egg='
with open('requirements.txt') as reqs:
    for line in reqs.read().split('\n'):
        if line.startswith('-e git:') or line.startswith('-e git+') or \
                line.startswith('git:') or line.startswith('git+'):
            if EGG_MARK in line:
                package_name = line[line.find(EGG_MARK) + len(EGG_MARK):]
                required.append(package_name)
                dependency_links.append(line)
            else:
                print('Dependency to a git repository should have the format:')
                print('git+ssh://git@github.com/xxxxx/xxxxxx#egg=package_name')
                sys.exit(1)
        else:
            required.append(line)

DESCRIPTION = ("directory_observer is a tool that allows you to monitor activity on "
               "various directories and push the corresponding events to a Redis queue")

setup(
    name='directory_observer',
    version="0.0.1",
    url="https://github.com/metwork-framework/directory_observer",
    packages=find_packages(),
    install_requires=required,
    dependency_links=dependency_links,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "directory_observer = directory_observer.directory_observer:main",
        ]
    }

)
