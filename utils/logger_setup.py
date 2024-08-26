import logging

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Function to setup a logger with a specific name and log level.
    Logs are output to the console.
    """
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.setLevel(level)
        logger.addHandler(handler)

    return logger