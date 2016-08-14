import time
import unittest

import hug
from tuxeatpi.components.wings import WingsError

from tuxeatpi_server.droid import tux
from tuxeatpi_server import static


class StaticFolderTests(unittest.TestCase):
    """Static Folder tests"""

    def setUp(self):
        """Method called before each test function"""
        tux.create_droid("tests/conf/tuxeatpi-conf1.yml")

    def tearDown(self):
        """Method called after each test function"""
        hug.API('tuxeatpi_server.droid.tux').context["droid"].wings.move_stop()
        del(hug.API('tuxeatpi_server.droid.tux').context["droid"])

    def test_ui(self):
        """Static tests"""
        # Get empty_for_git file
        result = hug.test.get(static, '/ui/empty_for_git')
        self.assertEqual(result.status, "200 OK")
        self.assertEqual(result.data, '')
