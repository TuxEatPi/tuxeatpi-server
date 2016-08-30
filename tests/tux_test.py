import time
import unittest

import hug
from tuxeatpi.components.wings import WingsError

from tuxeatpi_server.droid import tux


class TuxTests(unittest.TestCase):
    """Tux tests"""

    def setUp(self):
        """Method called before each test function"""
        tux.create_droid("tests/conf/tuxeatpi-conf1.yml")

    def tearDown(self):
        """Method called after each test function"""
        hug.API('tuxeatpi_server.droid.tux').context["droid"].wings.move_stop()
        hug.API('tuxeatpi_server.droid.tux').context["droid"].shutdown()

    def test_tux_root(self):
        """Tux/Main tests"""
        # Root
        result = hug.test.get(tux, '')
        self.assertEqual(result.status, "200 OK")
        self.assertRegexpMatches(result.data, "tuxeatpi.tux.Tux object")
        # Name
        result = hug.test.get(tux, 'name')
        self.assertEqual(result.status, "200 OK")
        self.assertEqual(result.data, "TuxDroid")

    def test_wings_root(self):
        """Tux/Wings tests"""
        # Wings
        result = hug.test.get(tux, 'wings')
        self.assertEqual(result.status, "200 OK")
        self.assertRegexpMatches(result.data, "components.wings.(Fake|)Wings object")
        # Get Position
        result = hug.test.get(tux, 'wings/position')
        self.assertEqual(result.status, "200 OK")
        self.assertEqual(result.data, "down")
        # Set bad Position
        self.assertRaises(WingsError, lambda: hug.test.post(tux, 'wings/position', {"position": "toto"}))
        # Set Position
        result = hug.test.post(tux, 'wings/position', {"position": "up"})
        self.assertEqual(result.status, "200 OK")
        self.assertEqual(result.data, None)
        time.sleep(3)
        # Get Position
        result = hug.test.get(tux, 'wings/position')
        self.assertEqual(result.status, "200 OK")
        self.assertEqual(result.data, "up")
