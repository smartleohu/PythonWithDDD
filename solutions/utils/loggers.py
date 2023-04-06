import datetime
from pathlib import Path

from loguru import logger

log_file = Path(__file__).parents[2] / "logs" /\
           "app_risks_" \
           f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

# logger.add(sys.stdout, format="{time} {level} {message}", colorize=True)
logger.add(log_file, format="{time} {level} {message}", colorize=True)


