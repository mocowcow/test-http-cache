
from data_module import util

shared_data: str = None
last_modified: str = None
etag: str = None
resp_count: int = 0


def update(s: str) -> None:
    global shared_data, last_modified, etag, resp_count
    shared_data = s
    last_modified = util.get_time_now()
    etag = util.generate_etag(shared_data)
    resp_count = 0


def is_modified_since(time: str) -> bool:
    if time is None:
        return False
    print("客戶端檔案時間 :", time)
    print("伺服器檔案時間 :", last_modified)
    return time == last_modified


def is_etag_match(e: str) -> bool:
    if etag is None:
        return False
    print("客戶端 etag :", e)
    print("伺服器 etag :", etag)
    return e == etag


def get() -> dict:
    data = {
        "resp count": f"這是第 {count()} 次伺服器回應",
        "data": shared_data,
    }
    return data


def count() -> int:
    global resp_count
    resp_count += 1
    return resp_count
