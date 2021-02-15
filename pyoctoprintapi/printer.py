"""Define information about a printer"""

import typing

class ToolTemperature:
    """Define temperature information"""
    def __init__(self, raw: dict, name: str):
        self._raw = raw
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def actual_temp(self) -> float:
        return self._raw.get("actual")

    @property
    def offset(self) -> float:
        return self._raw.get("offset")

    @property
    def target_temp(self) -> float:
        return self._raw.get("target")
    
class PrinterFlags:
    """Define state flags"""
    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def cancelling(self) -> bool:
        return self._get_flag("cancelling")

    @property
    def closed_or_error(self) -> bool:
        return self._get_flag("closedOrError")

    @property
    def error(self) -> bool:
        return self._get_flag("error")

    @property
    def finishing(self) -> bool:
        return self._get_flag("finishing")

    @property
    def operational(self) -> bool:
        return self._get_flag("operational")

    @property
    def paused(self) -> bool:
        return self._get_flag("paused")

    @property
    def pausing(self) -> bool:
        return self._get_flag("pausing")

    @property
    def printing(self) -> bool:
        return self._get_flag("printing")

    @property
    def ready(self) -> bool:
        return self._get_flag("ready")

    @property
    def resuming(self) -> bool:
        return self._get_flag("resuming")

    @property
    def sd_ready(self) -> bool:
        return self._get_flag("sdReady")

    def _get_flag(self, flag_name:str) -> bool:
        return self._raw.get(flag_name)

class PrinterState:
    """Define state flags"""
    def __init__(self, raw: dict):
        self._raw = raw
        self._flags = PrinterFlags(raw["flags"])

    @property
    def text(self) -> str:
        return self._raw.get("text")

    @property
    def flags(self) -> PrinterFlags:
        return self._flags

class OctoprintPrinterInfo:
    """Define information about a printer"""
    def __init__(self, raw: dict):
        self._raw = raw
        self._tempatures = [
            ToolTemperature(raw["temperature"][x], x) for x in raw["temperature"]
        ]
        self._state = PrinterState(raw["state"])
        self._has_heated_bed = "bed" in raw["temperature"]

    @property
    def temperatures(self) -> typing.List[ToolTemperature]:
        return self._tempatures

    @property
    def state(self) -> PrinterState:
        return self._state

    @property
    def has_heated_bed(self) -> bool:
        return self._has_heated_bed    