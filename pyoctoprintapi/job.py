"""Define information about the print job"""

class OctoprintJobProgress:
    """Current job information"""
    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def completion(self) -> float or None:
        return self._raw.get("completion")

    @property
    def print_time(self) -> int or None:
        return self._raw.get("printTime")

    @property
    def print_time_left(self) -> int or None:
        return self._raw.get("printTimeLeft")

class OctoprintJobInfo:
    """Define print job information"""
    def __init__(self, raw: dict):
        self._raw = raw
        self._progress = OctoprintJobProgress(raw["progress"])

    @property
    def state(self) -> str:
        return self._raw.get("state")

    @property
    def progress(self) -> OctoprintJobProgress:
        return self._progress