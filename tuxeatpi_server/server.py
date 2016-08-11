"""Entrypoint file for tuxeatpi-server"""

import argparse

import hug

from tuxeatpi_server.droid import tux


@hug.get('/')
def root():
    """Root path function"""
    return "root"


@hug.extend_api('/tux')
def tux_routes():
    """Import all tuxdroid functions"""
    return [tux]


def read_args():
    """Read command line arguments"""
    # Create arg parser
    args_parser = argparse.ArgumentParser(description='TuxEatPi Server')
    args_parser.add_argument('-c', '--config', type=str, required=True,
                             help='Config file')
    args_parser.add_argument('-v', '--verbose', action='store_true', default=False,
                             required=False, help='Verbose. Default: False')

    # Parse args
    args = args_parser.parse_args()
    # Store args
    hug.API(__name__).context['config'] = args.config
    hug.API(__name__).context['verbose'] = args.verbose


def main():
    """Main function
    - Read arguments
    - Start web server
    """
    read_args()
    try:
        __hug__.http.serve()  # pylint: disable=E0602
    except KeyboardInterrupt:
        pass
    del hug.API('tuxeatpi_server.droid.tux').context["droid"]


if __name__ == '__main__':
    main()
