"""Fetch data from S3 wifi stick."""
import logging

import httpcore
import httpx
import os
from httpx_auth import Basic
from .data_classes import InverterData

BASIC_AUTH = Basic(os.getenv("SOLIS_ADMIN_USER", "admin"),
                   os.getenv("SOLIS_LOGGER_PASSWORD", "geheim"))
SOLIS_URL = f"http://{os.getenv('SOLIS_HOST', '192.168.128.118')}/inverter.cgi"


def fetch(client=None):
    if not client:
        client = httpx
    try:
        response = client.get(SOLIS_URL)
    except (httpcore.ConnectTimeout, httpx.ConnectTimeout) as error:
        raise error
    return response


def fetch_data() -> InverterData:
    data: InverterData
    try:
        with httpx.Client(auth=BASIC_AUTH) as client:
            response = fetch(client=client)
            logging.info(f"Response ${response.text}")
    except (httpcore.ConnectTimeout, httpx.ConnectTimeout) as error:
        data = InverterData.timeout_value()
        logging.warning(f"Connect Timeout.")
    else:
        data = InverterData.from_response(response.text)
        logging.info(f"Current power: {data.current_power}")

    return data
