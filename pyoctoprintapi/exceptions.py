""" Library exception defs """

class OctoprintException(Exception):
    """Base Exception"""

class ApiError(OctoprintException):
    """Base API Exception"""

class PrinterOffline(ApiError):
    """Indicate the printer to not connected to the server"""