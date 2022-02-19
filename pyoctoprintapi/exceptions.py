""" Library exception defs """

class OctoprintException(Exception):
    """Base Exception"""

class ApiError(OctoprintException):
    """Base API Exception"""

class PrinterOffline(ApiError):
    """Indicate the printer to not connected to the server"""

class UnauthorizedException(ApiError):
    """Indicate the client is not authorized to communicate with the server."""