"""API for interacting with an Octoprint server""" 

import asyncio
import logging

import aiohttp

from .exceptions import ApiError, PrinterOffline, UnauthorizedException

_LOGGER = logging.getLogger(__name__)

APPKEY_ENDPOINT_BASE = "plugin/appkeys"
APPKEY_PROBE_ENDPOINT = APPKEY_ENDPOINT_BASE + "/probe"
APPKEY_REQUEST_ENDPOINT = APPKEY_ENDPOINT_BASE + "/request"
CONNECTION_ENDPOINT = "api/connection"
JOB_ENDPOINT = "api/job"
PRINTER_ENDPOINT = "api/printer"
SERVER_ENDPOINT = "api/server"
SETTINGS_ENDPOINT = "api/settings"
BED_ENDPOINT = "api/printer/bed"
TOOL_ENDPOINT = "api/printer/tool"
SYSTEM_COMMAND_ENDPOINT = "/api/system/commands"

class OctoprintApi:
    """Client for interacting with an Octoprint server"""
    def __init__(self, base_url: str, session: aiohttp.ClientSession):
        if not base_url.endswith("/"):
            base_url += "/"
        self._base_url = base_url
        self._headers = {}
        self._session = session

    def set_api_key(self, api_key: str) -> None:
        self._headers.update({"X-Api-Key": api_key})

    async def get_printer_info(self):
        _LOGGER.debug("Request Method=GET Endpoint=%s", PRINTER_ENDPOINT)
        response = await self._session.get(self._base_url + PRINTER_ENDPOINT, headers=self._headers)
        if response.status == 409:
            raise PrinterOffline("Printer is not operational")
        if response.status == 403:
            raise UnauthorizedException

        return await response.json()

    async def get_job_info(self):
        return await self._get_request(JOB_ENDPOINT)

    async def get_connection_info(self):
        return await self._get_request(CONNECTION_ENDPOINT)

    async def get_server_info(self):
        return await self._get_request(SERVER_ENDPOINT)

    async def get_settings(self):
        return await self._get_request(SETTINGS_ENDPOINT)

    async def check_appkeys_enabled(self):
        _LOGGER.debug("Request Method=GET Endpoint=%s", APPKEY_PROBE_ENDPOINT)
        response = await self._session.get(self._base_url + APPKEY_PROBE_ENDPOINT)
        if response.status != 204:
            return False

        return True

    async def appkeys_start_auth(self, appname: str, user: str = None):
        data = { "app": appname }
        if user:
            data["user"] = user
        _LOGGER.debug("Request Method=GET Endpoint=%s", APPKEY_REQUEST_ENDPOINT)
        response = await self._session.post(self._base_url + APPKEY_REQUEST_ENDPOINT, json = data)
        if response.status == 201:
            location_url = response.headers["Location"]
            return location_url[location_url.rindex("/") + 1:]

        raise ApiError(f"Failed to start auth process: code {response.status}")

    async def appkeys_check_status(self, appkey:str):
        _LOGGER.debug("Request Method=GET Endpoint=%s", APPKEY_REQUEST_ENDPOINT)
        response = await self._session.get(f"{self._base_url}{APPKEY_REQUEST_ENDPOINT}/{appkey}")
        if response.status == 404:
            raise ApiError("Application key creation request has been denied or timed out")

        body = await response.json()
        return body

    async def issue_system_command(self, source:str, action:str) -> None:
        _LOGGER.debug("Request Method=POST Endpoint=%s", SYSTEM_COMMAND_ENDPOINT)
        url = f"{self._base_url}{SYSTEM_COMMAND_ENDPOINT}/{source}/{action}"
        response = await self._session.post(url, headers=self._headers)
        if response.status != 204:
            raise ApiError(f"Failed to issue command {source}.{action} - code {response.status}")

    async def issue_job_command(self, command: str, action:str = None) -> None:
        _LOGGER.debug("Request Method=POST Endpoint=%s", JOB_ENDPOINT)
        data = {"command": command}
        if action:
            data["action"] = action
        response = await self._session.post(f"{self._base_url}{JOB_ENDPOINT}", json=data, headers=self._headers)
        if response.status != 204:
            raise ApiError("The printer is not operational or the current print job state does not match the preconditions for the command")

    async def issue_connection_command(self, command: str, **args) -> None:
        _LOGGER.debug("Request METHOD=POST Endpoint=%s", CONNECTION_ENDPOINT)
        url = f"{self._base_url}{CONNECTION_ENDPOINT}"
        data = {
            key: value for key, value in args.items() if value is not None
        }
        data["command"] = command
        response = await self._session.post(url, json=data, headers=self._headers)
        if response.status != 204:
            raise ApiError(f"Failed to issue connection command {command} - code {response.status}")

    async def set_bed_temperature(self, target:int, offset: int = 0) -> None:
        _LOGGER.debug("Request METHOD=POST Endpoint=%s Target=%d Offset=%d", BED_ENDPOINT, target, offset)
        url = f"{self._base_url}/{BED_ENDPOINT}"
        data = {
            "command": "target",
            "target": target,
            "offset": offset
        }
        response = await self._session.post(url, json=data, headers=self._headers)
        if response.status != 204:
            raise ApiError(f"Failed to set bed temperature - code {response.status}")

    async def issue_tool_command(self, command: str, **args) -> None:
        _LOGGER.debug("Request Method=POST Endpoint=%s", TOOL_ENDPOINT)
        data = {
            key: value for key, value in args.items() if value is not None
        }
        data["command"] = command
        response = await self._session.post(f"{self._base_url}{TOOL_ENDPOINT}", json=data, headers=self._headers)
        if response.status != 204:
            raise ApiError("The printer is not operational or the current print job state does not match the preconditions for the command")

    async def _get_request(self, endpoint: str):
        _LOGGER.debug("Request Method=GET Endpoint=%s", endpoint)
        response = await self._session.get(self._base_url + endpoint, headers=self._headers)
        try:
            response.raise_for_status()
        except aiohttp.ClientResponseError as ex:
            if ex.status == 403:
                raise UnauthorizedException from ex

            raise ApiError from ex

        if response.content_length == 0:
            return None

        body = await response.json()
        return body
