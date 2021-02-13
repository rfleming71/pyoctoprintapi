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
