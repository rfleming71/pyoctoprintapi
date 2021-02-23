""" Defines the OctoprintApi module """

from .api import OctoprintApi
from .octoprint_client import OctoprintClient
from .job import OctoprintJobInfo, OctoprintJobProgress
from .printer import OctoprintPrinterInfo, ToolTemperature, PrinterFlags, PrinterState
from .server import OctoprintServerInfo
from .settings import TrackingSetting, DiscoverySettings

class ApiError(Exception):
    """Base API Exception"""

class PrinterOffline(ApiError):
    """Indicate the printer to not connected to the server"""
