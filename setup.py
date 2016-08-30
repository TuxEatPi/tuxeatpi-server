#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


packages = ['tuxeatpi_server',
            'tuxeatpi_server.droid',
            ]

setup(
    name='tuxeatpi_server',
    version='0.0.1',
    packages=packages,
    description="""New TuxDroid heart powered by Raspberry pi - Rest API server""",
    author="TuxEatPi Team",
    # TODO create team mail
    author_email='titilambert@gmail.com',
    url="https://github.com/TuxEatPi/tuxeatpi_server",
    download_url="https://github.com/TuxEatPi/tuxeatpi_server/archive/0.0.1.tar.gz",
    package_data={'': ['LICENSE.txt']},
    package_dir={'tuxeatpi_server': 'tuxeatpi_server'},
    include_package_data=True,
    license='Apache 2.0',
    classifiers=(
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
    ),
    entry_points="""
    [console_scripts]
    tuxeatpi_server=tuxeatpi_server.server:main
    """,
)
