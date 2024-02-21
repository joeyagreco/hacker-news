import requests

from hn_sdk.client.util import rest_call
from hn_sdk.util.ConfigReader import ConfigReader

BASE_URL = ConfigReader.get("client", "HACKER_NEWS_API", "BASE_URL")
VERSION = ConfigReader.get("client", "HACKER_NEWS_API", "VERSION")
TOP_STORIES_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "TOP_STORIES_PATH")
NEW_STORIES_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "NEW_STORIES_PATH")
BEST_STORIES_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "BEST_STORIES_PATH")
ASK_STORIES_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "ASK_STORIES_PATH")
SHOW_STORIES_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "SHOW_STORIES_PATH")
JOB_STORIES_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "JOB_STORIES_PATH")
ITEM_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "ITEM_PATH")
USER_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "USER_PATH")
MAX_ITEM_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "MAX_ITEM_PATH")
UPDATES_PATH = ConfigReader.get("client", "HACKER_NEWS_API", "UPDATES_PATH")


def get_item_by_id(item_id: int) -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#items
    """
    if not isinstance(item_id, int):
        raise ValueError("item id must be an integer")
    url = f"{BASE_URL}/{VERSION}/{ITEM_PATH}/{item_id}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_user_by_username(username: str) -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#users
    """
    url = f"{BASE_URL}/{VERSION}/{USER_PATH}/{username}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_max_item_id() -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#live-data
    """
    url = f"{BASE_URL}/{VERSION}/{MAX_ITEM_PATH}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_top_stories() -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#live-data
    """
    url = f"{BASE_URL}/{VERSION}/{TOP_STORIES_PATH}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_new_stories() -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#live-data
    """
    url = f"{BASE_URL}/{VERSION}/{NEW_STORIES_PATH}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_best_stories() -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#live-data
    """
    url = f"{BASE_URL}/{VERSION}/{BEST_STORIES_PATH}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_ask_stories() -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#live-data
    """
    url = f"{BASE_URL}/{VERSION}/{ASK_STORIES_PATH}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_show_stories() -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#live-data
    """
    url = f"{BASE_URL}/{VERSION}/{SHOW_STORIES_PATH}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_job_stories() -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#live-data
    """
    url = f"{BASE_URL}/{VERSION}/{JOB_STORIES_PATH}.json"
    response = rest_call(requests.get, url)
    return response.json()


def get_updates() -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#live-data
    """
    url = f"{BASE_URL}/{VERSION}/{UPDATES_PATH}.json"
    response = rest_call(requests.get, url)
    return response.json()
