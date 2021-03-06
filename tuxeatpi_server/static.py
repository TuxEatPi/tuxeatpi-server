"""Handle static files and folder"""

import os

import hug

from tuxeatpi_server.utils import get_main_folder


@hug.static("/ui")
def tuxeatpi_web():
    """Return ui files from ui folder
    populated by tuxeatpi-web project
    """
    ui_folder = os.path.join(get_main_folder(), "ui")
    return (ui_folder, )


# Maybe this is not needed
@hug.static("/service-worker.js")
def tuxeatpi_web_worker():
    """Return service-worker.js"""
    ui_folder = os.path.join(get_main_folder(), "ui/service-worker.js")
    return (ui_folder, )
