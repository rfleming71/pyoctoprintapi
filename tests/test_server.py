"""Test server information API."""
import json

from pyoctoprintapi.server import OctoprintServerInfo
from fixtures import TEST_SERVER

def test_properties():
    server = OctoprintServerInfo(json.loads(TEST_SERVER))
    assert server.safe_mode == "bad_file"
    assert server.version == "1.5.3"