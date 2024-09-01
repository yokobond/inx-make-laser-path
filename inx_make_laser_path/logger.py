"""
This is a simple logger.
"""

import logging

logging.basicConfig(
    filename="./make_laser_path.log",
    filemode="w",
    format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("make_laser_path")
