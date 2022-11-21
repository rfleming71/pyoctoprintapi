"""Client for interacting with an Octoprint server""" 

import asyncio
import logging
from typing import Optional

import aiohttp

from .api import OctoprintApi
from .const import (CONNECTION_COMMAND_CONNECT, CONNECTION_COMMAND_DISCONNECT,
                    JOB_COMMAND_CANCEL, JOB_COMMAND_PAUSE,
                    JOB_COMMAND_PAUSE_PAUSE, JOB_COMMAND_PAUSE_RESUME)
from .exceptions import OctoprintException
from .job import OctoprintJobInfo
from .printer import OctoprintPrinterInfo
from .server import OctoprintServerInfo
from .settings import DiscoverySettings, TrackingSetting, WebcamSettings

_LOGGER = logging.getLogger(__name__)

class OctoprintClient:
    """Client for interacting with an Octoprint server"""
    def __init__(self, host: str, session: aiohttp.ClientSession, port: int = 80, ssl: bool = False, path: str = "/"):
        protocol = "https" if ssl else "http"
        self._base_url = f"{protocol}://{host}:{port}{path}"
        self._api = OctoprintApi(self._base_url, session)

    async def request_app_key(self, app_name: str, user:str, timeout:int = 5) -> str:
        if not await self._api.check_appkeys_enabled():
            raise OctoprintException("The application keys plugin appears to be disabled")

        request_id = await self._api.appkeys_start_auth(app_name, user)
        status_response = await self._api.appkeys_check_status(request_id)
        while ("api_key" not in status_response):
            await asyncio.sleep(1)
            status_response = await self._api.appkeys_check_status(request_id)
            if "message" in status_response:
                _LOGGER.debug("Message: %s", status_response["message"])
                
            timeout -= 1
            if timeout <= 0:
                raise OctoprintException("Timeout waiting for authorization")

        return status_response["api_key"]
    
    def set_api_key(self, api_key: str) -> None:
        self._api.set_api_key(api_key)

    async def get_printer_info(self) -> OctoprintPrinterInfo:
        response = await self._api.get_printer_info()
        return OctoprintPrinterInfo(response)

    async def get_job_info(self) -> OctoprintJobInfo:
        response = await self._api.get_job_info()
        return OctoprintJobInfo(response)

    async def get_server_info(self) -> OctoprintServerInfo:
        response = await self._api.get_server_info()
        return OctoprintServerInfo(response)

    async def get_tracking_info(self) -> Optional[TrackingSetting]:
        response = await self._api.get_settings()
        if "tracking" in response["plugins"]:
            return TrackingSetting(response["plugins"]["tracking"])
        
        return None

    async def get_webcam_info(self) -> Optional[WebcamSettings]:
        response = await self._api.get_settings()
        if "webcam" in response:
            return WebcamSettings(self._base_url, response["webcam"])
        
        return None

    async def get_discovery_info(self) -> Optional[DiscoverySettings]:
        response = await self._api.get_settings()
        if "discovery" in response["plugins"]:
            return DiscoverySettings(response["plugins"]["discovery"])

        return None

    async def shutdown(self) -> None:
        _LOGGER.debug("Sending shutdown command")
        await self._api.issue_system_command("core", "shutdown")

    async def reboot_system(self) -> None:
        _LOGGER.debug("Sending reboot command")
        await self._api.issue_system_command("core", "reboot")

    async def restart(self) -> None:
        _LOGGER.debug("Sending restart command")
        await self._api.issue_system_command("core", "restart")

    async def cancel_job(self) -> None:
        _LOGGER.debug("Sending cancel job command")
        await self._api.issue_job_command(JOB_COMMAND_CANCEL)

    async def pause_job(self) -> None:
        _LOGGER.debug("Sending pause job command")
        await self._api.issue_job_command(JOB_COMMAND_PAUSE, JOB_COMMAND_PAUSE_PAUSE)

    async def resume_job(self) -> None:
        _LOGGER.debug("Sending resume job command")
        await self._api.issue_job_command(JOB_COMMAND_PAUSE, JOB_COMMAND_PAUSE_RESUME)

    async def disconnect(self) -> None:
        _LOGGER.debug("Disconnecting from printer")
        await self._api.issue_connection_command(CONNECTION_COMMAND_DISCONNECT)

    async def connect(self, port: Optional[str] = None, baud_rate: Optional[int] = None, printer_profile: Optional[str] = None, save: Optional[bool] = None, auto_connect: Optional[bool] = None) -> None:
        _LOGGER.debug("Connecting to printer")
        await self._api.issue_connection_command(CONNECTION_COMMAND_CONNECT, port=port, baudrate=baud_rate, printerprofile=printer_profile, save=save, autoconnect=auto_connect)

    async def set_bed_temperature(self, target: int, offset: int = 0) -> None:
        _LOGGER.debug("Setting bed temp to %d, offset %d", target, offset)
        await self._api.set_bed_temperature(target, offset=offset)

    async def turn_bed_off(self) -> None:
        _LOGGER.debug("Turning off bed")
        await self._api.set_bed_temperature(0)

    async def set_tool_temperature(self, tool: str, target: int) -> None:
        _LOGGER.debug("Setting tool %s temp to %d", tool, target)
        targets = {
            tool: target
        }
        await self._api.issue_tool_command("target", targets=targets)

    async def turn_tool_off(self, tool: str) -> None:
        _LOGGER.debug("Turning off tool %s", tool)
        targets = {
            tool: 0
        }
        await self._api.issue_tool_command("target", targets=targets)
