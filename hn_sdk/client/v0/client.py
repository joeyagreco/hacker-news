import requests

from hn_sdk.client.util import rest_call

# TODO: put these in config file
BASE_URL = "https://hacker-news.firebaseio.com"
VERSION = "v0"
TOP_STORIES_PATH = "topstories"
NEW_STORIES_PATH = "newstories"
BEST_STORIES_PATH = "beststories"
ASK_STORIES_PATH = "askstories"
SHOW_STORIES_PATH = "showstories"
JOB_STORIES_PATH = "jobstories"
ITME_PATH = "item"
USER_PATH = "user"
MAX_ITEM_PATH = "maxitem"
UPDATES_PATH = "updates"


def get_item_by_id(item_id: str) -> dict:
    """
    https://github.com/HackerNews/API?tab=readme-ov-file#items
    """
    url = f"{BASE_URL}/{VERSION}/{ITME_PATH}/{item_id}.json"
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
