"""Module to interact with TuxDroid using tuxeatpi lib"""

import time

import hug
from tuxeatpi.tux import Tux


@hug.startup()
def init_droid(interface_api):
    """Wrapper to init the TuxDroid on server startup"""
    # FYI hug.API('tuxeatpi_server.server') is interface_api.api
    if "droid" not in hug.API(__name__).context:
        create_droid(hug.API('tuxeatpi_server.server').context["config"])


def create_droid(config_file):
    """Init the TuxDroid"""
    hug.API(__name__).context["droid"] = Tux(config_file)
    return hug.API(__name__).context["droid"]


def get_droid():
    """Return TuxDroid"""
    return hug.API(__name__).context["droid"]


@hug.get("/")
def root():
    """Root path for Tux"""
    return str(get_droid())


@hug.get("/name")
def name():
    """Return Tux name"""
    return get_droid().name


@hug.get("/wings")
def wings():
    """Root path for wings"""
    return str(get_droid().wings)


@hug.get("/wings/position")
def wings_position():
    """Return wings position"""
    return get_droid().wings.get_position()


@hug.post("/wings/position")
def wings_move(position):
    """Move Wings to a position"""
    get_droid().wings.move_to_position(position)
