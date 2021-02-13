"""Test setting information API."""
import json

from pyoctoprintapi.settings import TrackingSetting
from fixtures import TEST_SETTINGS_TRACKING

def test_properties():
    tracking = TrackingSetting(json.loads(TEST_SETTINGS_TRACKING))
    assert not tracking.enabled
    assert tracking.unique_id == "6c4fae84-4be3-4c4d-8fbd-de9d0c3e1fcb"