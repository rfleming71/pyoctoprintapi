"""Define information about the octoprint server"""

class OctoprintServerInfo:
    """Current job information"""
    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def safe_mode(self) -> str or None:
        return self._raw.get("safemode")

    @property
    def version(self) -> str:
        return self._raw.get("version")
