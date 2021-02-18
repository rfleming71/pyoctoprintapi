""" Setting classes """

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