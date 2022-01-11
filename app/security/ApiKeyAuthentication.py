from configparser import ConfigParser

from fastapi import Security
from fastapi.security import APIKeyHeader
from starlette.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

path_to_configuration_file = "config.ini"

config_init = ConfigParser()
config_init.read(path_to_configuration_file)
config = config_init["AUTHENTICATION"]
API_KEY = config["API_KEY"]
API_KEY_NAME = config["API_KEY_NAME"]
api_key_header = APIKeyHeader(name=API_KEY_NAME)


async def get_api_key(
    api_key_header_to_check: str = Security(api_key_header),
):
    if api_key_header_to_check == API_KEY:
        return api_key_header_to_check
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
