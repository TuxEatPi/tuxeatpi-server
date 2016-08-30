"""Module to interact with TuxDroid using tuxeatpi lib"""

import hug
from tuxeatpi.tux import Tux
from tuxeatpi.voice.common import VOICES

from tuxeatpi_server.utils import cors_support


@hug.startup()
def init_droid(interface_api):  # pylint: disable=W0613
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


@hug.get("/name", requires=cors_support)
def name():
    """Return Tux name"""
    return get_droid().settings['global']['name']


@hug.get("/wings")
def wings():
    """Root path for wings"""
    return str(get_droid().wings)


@hug.get("/wings/position", requires=cors_support)
def wings_position():
    """Return wings position"""
    return get_droid().wings.get_position()


@hug.post("/wings/position", requires=cors_support)
def wings_move(position):
    """Move Wings to a position"""
    get_droid().wings.move_to_position(position)


@hug.post("/voice/tts", requires=cors_support)
def voice_tts(text):
    """Text to speech"""
    get_droid().say(text)


@hug.get("/settings", requires=cors_support)
def get_settings():
    """Get Tux settings"""
    return dict(get_droid().settings)


@hug.post("/settings", requires=cors_support)
def save_settings(settings):
    """Save Tux settings"""
    if get_droid().update_setting(settings):
        return get_droid().settings
        # TODO OK
    else:
        return get_droid().settings
        # TODO Error


@hug.get("/settings/languages", requires=cors_support)
def get_languages():
    """Get Tux languages capabilities"""
    return VOICES


@hug.post("/nlu/text", requires=cors_support)
def understand_text(text, say_it=False):
    """Try to understand text (NLU)"""
    answer = get_droid().understand_text(text, say_it=say_it)
    return {"answer": answer}
