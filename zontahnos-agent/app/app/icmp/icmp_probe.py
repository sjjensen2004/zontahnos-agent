from utils.request_manager import update_icmp
from core.config import config
import time
import logging
from core.logging_config import logger
from ping3 import ping


# Load config values
SECRET_KEY = config.get("SECRET_KEY")
PROBE_NAME = config.get("PROBE_NAME")
LOCATION = config.get("LOCATION")
HOST_TARGETS = config.get("HOST_TARGETS")
INTERVAL = config.get("INTERVAL", 5)  # Default to 5 seconds if not set


def ping_host(host):
    """Ping the target host and return response time."""
    response = ping(host)

    return (
        (response) * 1000 if response else None
    )  # Convert to milliseconds if response exists


def execute_icmp_ping(host):
    """Continuously ping a given host and send results."""
    while True:
        latency = ping_host(host)
        logger.info(
            f"{host} → Latency: {latency}ms"
            if latency
            else f"{host} → Host unreachable"
        )

        data = {
            "location": LOCATION,
            "probe_name": PROBE_NAME,
            "target_host": host,
            "latency": latency,
            "status": 0 if latency else 1,
            "key": SECRET_KEY,
        }

        update_icmp(data)
        time.sleep(INTERVAL)  # Wait for the next probe
