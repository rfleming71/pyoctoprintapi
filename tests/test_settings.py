"""Test setting information API."""
import json

from pyoctoprintapi.settings import TrackingSetting, WebcamSettings, DiscoverySettings
from fixtures import TEST_SETTINGS_CAMERA, TEST_SETTINGS_CAMERA_1, TEST_SETTINGS_TRACKING, TEST_SETTINGS_DISCOVERY

def test_tracking_setting_properties():
    tracking = TrackingSetting(json.loads(TEST_SETTINGS_TRACKING))
    assert not tracking.enabled
    assert tracking.unique_id == "6c4fae84-4be3-4c4d-8fbd-de9d0c3e1fcb"

def test_discovery_settings_properties():
    tracking = DiscoverySettings(json.loads(TEST_SETTINGS_DISCOVERY))
    assert tracking.http_username == "username"
    assert tracking.http_password == "password"
    assert tracking.public_host == "host"
    assert tracking.public_port == 80
    assert tracking.upnp_uuid == "436fc3ec-fc2e-4851-b289-eb17974aa706"

def test_webcam_settings_properties():
    tracking = WebcamSettings("https://foo.com:8080", json.loads(TEST_SETTINGS_CAMERA))
    assert tracking.enabled 
    assert tracking.bitrate == "10000k"
    assert tracking.external_snapshot_url == "https://foo.com:8080/webcam/?action=snapshot"
    assert tracking.stream_url == "https://foo.com:8080/webcam/?action=stream"

def test_webcam_settings_2_properties():
    tracking = WebcamSettings("https://foo.com:8080", json.loads(TEST_SETTINGS_CAMERA))
    assert tracking.enabled 
    assert tracking.bitrate == "10000k"
    assert tracking.external_snapshot_url == "https://foo.com:8080/webcam/?action=snapshot"
    assert tracking.stream_url == "https://foo.com:8080/webcam/?action=stream"

def test_webcam_settings_2_properties():
    tracking = WebcamSettings("https://foo.com:8080", json.loads(TEST_SETTINGS_CAMERA_1))
    assert tracking.enabled 
    assert tracking.bitrate == "10000k"
    assert tracking.external_snapshot_url == "http://127.0.0.1:8000/webcam/?action=snapshot"
    assert tracking.stream_url == "http://127.0.0.1:8000/webcam/?action=stream"