import unittest
import sys

import hug

from tuxeatpi_server import server


class ServerTests(unittest.TestCase):
    """Server tests"""

    def test_server(self):
        """Server/Basic tests"""
        # Parse arguments
        sys.argv = ["tuxeatpi_server", "-c", "tests/conf/tuxeatpi-conf1.yml"]
        server.read_args()
        self.assertEqual(hug.API(server.__name__).context['config'],  "tests/conf/tuxeatpi-conf1.yml")
        self.assertEqual(hug.API(server.__name__).context['verbose'],  False)
