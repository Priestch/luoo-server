from requests import Request, Session
from user_agent import generate_user_agent

session = Session()
crawl_timeout = None


def get(url):
    req = Request(
        "GET", url, headers={"User-Agent": generate_user_agent(os=("mac", "linux"))}
    )
    prepared = session.prepare_request(req)
    return session.send(prepared)
