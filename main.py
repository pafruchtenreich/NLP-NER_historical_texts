### IMPORTS ###
from src.setup.setup_device import (
    get_allowed_cpu_count,
    set_up_device,
    setup_config_device,
)
from src.setup.setup_logger import setup_logger

### GLOBAL VARIABLES ###
if __name__ == "__main__":
    # Initialize logger
    logger = setup_logger()
    device = set_up_device()
    cpu_count = get_allowed_cpu_count()
    n_process = setup_config_device(cpu_count)

    # Load data
    logger.info("Loading data")

    # Preprocess data
    logger.info("Preprocessing data")
