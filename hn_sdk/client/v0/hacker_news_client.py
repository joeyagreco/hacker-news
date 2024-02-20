import requests

from hn_sdk.client.util import rest_call

# TODO: put these in config file
BASE_URL = "https://hacker-news.firebaseio.com"
VERSION = "v0"
TOP_STORIES_PATH = "topstories"


def get_top_stories() -> dict:
    url = f"{BASE_URL}/{VERSION}/{TOP_STORIES_PATH}.json"
    response = rest_call(requests.get, url)
    response.raise_for_status()
    return response.json()
