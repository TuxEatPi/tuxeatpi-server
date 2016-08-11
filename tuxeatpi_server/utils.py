"""Util functions for tuxeatpi server"""


def cors_support(response, *args, **kwargs):  # pylint: disable=W0613
    """Add cors support for an endpoint"""
    response.set_header('Access-Control-Allow-Origin', '*')
