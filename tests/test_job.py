"""Test job information API."""
import json

from pyoctoprintapi.job import OctoprintJobInfo
from fixtures import TEST_JOB

def test_properties():
    job = OctoprintJobInfo(json.loads(TEST_JOB))
    assert job.state == "Printing"
    assert job.progress.completion == 45.65
    assert job.progress.print_time == 15432
    assert job.progress.print_time_left == 12354