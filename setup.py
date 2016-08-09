#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='tuxeatpi_server',
    entry_points="""
    [console_scripts]
    tuxeatpi_server=tuxeatpi_server.server:main
    """,
)
