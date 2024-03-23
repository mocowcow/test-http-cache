
from datetime import datetime
import hashlib

DATA_PATTERN = "%a, %d %b %Y %H:%M:%S GMT"


def get_time_now() -> str:
    return datetime.now().strftime(DATA_PATTERN)


def parse_time(s: str) -> datetime:
    return datetime.strptime(s, DATA_PATTERN)


def generate_etag(data: str) -> str:
    return hashlib.sha1(data.encode()).hexdigest()
