"""Test job information API."""
import json

from pyoctoprintapi.printer import OctoprintPrinterInfo
from fixtures import TEST_PRINTER

def test_properties():
    printer = OctoprintPrinterInfo(json.loads(TEST_PRINTER))
    assert printer.state.flags.ready
    assert not printer.state.flags.printing
    assert not printer.state.flags.error
    assert printer.state.text == "Operational"
    assert printer.has_heated_bed
    assert printer.temperatures[0].name == "bed"
    assert printer.temperatures[0].actual_temp == 14.53
    assert printer.temperatures[0].offset == -5
    assert printer.temperatures[0].target_temp == 60
    assert printer.temperatures[1].name == "tool0"
    assert printer.temperatures[1].actual_temp == 14.17
    assert printer.temperatures[1].offset == 10
    assert printer.temperatures[1].target_temp == 200