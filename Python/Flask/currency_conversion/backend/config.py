import os
import logging


class Config:
    SECRET = os.environ.get("SECRET")


logging.basicConfig(
    format="%(asctime)s: %(levelname)s: %(message)s",
    filename="log.log",
    filemode="w",
    level=logging.DEBUG,
)
stderrLogger = logging.StreamHandler()
stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(stderrLogger)
