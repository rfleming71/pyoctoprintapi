""" Setting classes """
from urllib.parse import urlparse, urlunparse, urlencode, parse_qsl

class TrackingSetting:
    """Tracking information and settings"""
    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def enabled(self) -> bool:
        return self._raw["enabled"]

    @property
    def unique_id(self) -> str:
        return self._raw["unique_id"]

class DiscoverySettings:
    """Discovery plugin settings"""
    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def http_password(self):
        return self._raw.get("httpPassword")

    @property
    def http_username(self):
        return self._raw.get("httpUsername")

    @property
    def public_host(self):
        return self._raw.get("publicHost")

    @property
    def public_port(self):
        return self._raw.get("publicPort")

    @property
    def upnp_uuid(self):
        return self._raw.get("upnpUuid")

class WebcamSettings:
    """Webcam settings"""
    def __init__(self, base_url: str, raw: dict):
        self._base_url = base_url
        self._raw = raw

    @property
    def bitrate(self) -> str:
        return self._raw["bitrate"]

    @property
    def flip_horizontal(self) -> str:
        return self._raw["flipH"]

    @property
    def flip_vertical(self) -> str:
        return self._raw["flipV"]

    @property
    def rotate_90(self) -> str:
        return self._raw["rotate90"]

    @property
    def snapshot_ssl_validation_enabled(self) -> bool:
        return self._raw["snapshotSslValidation"]

    @property
    def internal_snapshot_url(self) -> str:
        return self._raw["snapshotUrl"]

    @property
    def external_snapshot_url(self) -> str:
        url = self.stream_url
        parsed = list(urlparse(url))
        parsed[2] = parsed[2].replace("//", "/")
        query = dict(parse_qsl(parsed[4]))
        query["action"] = "snapshot"
        parsed[4] = urlencode(query)

        return urlunparse(parsed)

    @property
    def stream_url(self) -> str:
        stream_url = self._raw["streamUrl"]
        return f"{self._base_url}{stream_url}"

    @property
    def enabled(self) -> bool:
        return self._raw["webcamEnabled"]
