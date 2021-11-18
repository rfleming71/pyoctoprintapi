"""Test entry point"""

import aiohttp
import pyoctoprintapi
import argparse
import asyncio
import logging
from types import MappingProxyType

LOGGER = logging.getLogger(__name__)


async def main(host, user, port, use_ssl):
    """Main function."""
    LOGGER.info("Starting octoprint")

    async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True)) as websession:
        websession._default_headers = MappingProxyType({})  # type: ignore
        client = pyoctoprintapi.OctoprintClient(host, websession, port, use_ssl, "/")
        api_key = await client.request_app_key("testapp", user, 60)
        client.set_api_key(api_key)
        printer_info = await client.get_printer_info()
        job_info = await client.get_job_info()
        server_info = await client.get_server_info()
        tracking_info = await client.get_tracking_info()
        discovery_info = await client.get_discovery_info()
        camera_info = await client.get_webcam_info()

        await websession.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("user", type=str)
    parser.add_argument("-p", "--port", type=int, default=80)
    parser.add_argument("-s", "--ssl", type=bool, default=False)
    parser.add_argument("-d", "--debug", type=bool, default=False)
    args = parser.parse_args()

    LOG_LEVEL = logging.INFO
    if args.debug:
        LOG_LEVEL = logging.DEBUG
    logging.basicConfig(format="%(message)s", level=LOG_LEVEL)

    try:
        asyncio.run(
            main(args.host, args.user, args.port, args.ssl)
        )
    except KeyboardInterrupt:
        pass