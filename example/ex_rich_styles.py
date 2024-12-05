from rich.logging import RichHandler
import logging

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    handlers=[RichHandler()]
)

logging.info("To jest informacja")
logging.error("To jest błąd!")