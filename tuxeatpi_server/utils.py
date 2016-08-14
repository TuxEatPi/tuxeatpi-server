"""Util functions for tuxeatpi server"""

import os


def get_main_folder():
    """Get main folder path"""
    current_folder = os.path.dirname(os.path.realpath(__file__))
    return os.path.realpath(os.path.join(current_folder, '..'))


def cors_support(response, *args, **kwargs):  # pylint: disable=W0613
    """Add cors support for an endpoint"""
    response.set_header('Access-Control-Allow-Origin', '*')
