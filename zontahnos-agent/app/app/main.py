from icmp.icmp_probe import execute_icmp_ping
from icmp.icmp_probe import SECRET_KEY
import concurrent.futures
from core.config import config
from core.logging_config import logger

HOST_TARGETS = config.get("HOST_TARGETS")

if __name__ == "__main__":

    while True:
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=len(HOST_TARGETS)
        ) as executor:
            for host in HOST_TARGETS:
                executor.submit(execute_icmp_ping, host)
