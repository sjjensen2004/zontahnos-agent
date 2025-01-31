from scapy.all import ICMP, IP, sr1
from utils.request_manager import send_probe
from core.config import config
import time
import logging
from core.logging_config import logger 


# Load config values
SECRET_KEY = config.get("SECRET_KEY")
PROBE_NAME = config.get("PROBE_NAME")
LOCATION = config.get("LOCATION")
HOST_TARGETS = config.get("HOST_TARGETS")
INTERVAL = config.get("INTERVAL", 5)  # Default to 5 seconds if not set

def ping_host(host):
    """Ping the target host and return response time."""
    packet = IP(dst=host) / ICMP()
    response = sr1(packet, timeout=1, verbose=0)

    return (response.time - packet.sent_time) * 1000 if response else None  # Convert to milliseconds if response exists

def execute_icmp_ping(host):
    """Continuously ping a given host and send results."""
    while True:
        latency = ping_host(host)
        logger.info(f"{host} → Latency: {latency}ms" if latency else f"{host} → Host unreachable")

        data = {
            "location": LOCATION,
            "probe_name": PROBE_NAME,
            "target_host": host,
            "latency": latency,
            "status": 0 if latency else 1,
            "key": SECRET_KEY
        }
        
        send_probe(data)
        time.sleep(INTERVAL)  # Wait for the next probe