import requests
from core.config import config
import logging
from core.logging_config import logger

ZONTAHNOS_IP = config.get("ZONTAHNOS_IP")


API_URL = f"http://{ZONTAHNOS_IP}/api/v1/icmp/update"


def update_icmp(data):
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            logger.info(f"ICMP Probe stored successfully.")
        else:
            logger.info(
                f"Failed to send probe: {response.status_code}: {response.text}"
            )
    except Exception as e:
        logger.error(f"⚠️ API connection error: {e}")
