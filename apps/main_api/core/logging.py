import logging
import sys

def setup_logging():
    log_level = logging.DEBUG if os.getenv("ENVIRONMENT") == "development" else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout
    )