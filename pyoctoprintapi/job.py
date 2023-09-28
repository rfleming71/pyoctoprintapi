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


class OctoprintJobFile:
    """Current job file information"""

    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def name(self) -> str | None:
        return self._raw.get("name")

    @property
    def origin(self) -> str or None:
        return self._raw.get("origin")

    @property
    def size(self) -> int or None:
        return self._raw.get("size")


class OctoprintJob:
    """Current job information"""

    def __init__(self, raw: dict):
        self._raw = raw
        self._file = OctoprintJobFile(raw["file"])

    @ property
    def file(self) -> OctoprintJobFile | None:
        return self._file

    @ property
    def completion(self) -> float or None:
        return self._raw.get("completion")

    @ property
    def estimated_print_time(self) -> int or None:
        return self._raw.get("estimatedPrintTime")


class OctoprintJobInfo:
    """Define print job information"""

    def __init__(self, raw: dict):
        self._raw = raw
        self._progress = OctoprintJobProgress(raw["progress"])
        self._job = OctoprintJob(raw["job"])

    @ property
    def state(self) -> str:
        return self._raw.get("state")

    @ property
    def progress(self) -> OctoprintJobProgress:
        return self._progress

    @property
    def job(self) -> OctoprintJob:
        return self._job

    @property
    def error(self) -> str | None:
        if "error" in self._raw:
            return self._raw["error"]

        return None
