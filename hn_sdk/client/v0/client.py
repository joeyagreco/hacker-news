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


def __is_valid_hacker_news_username(username: str) -> bool:
    """
    Validates if a given username is valid for Hacker News.
    For validation, per https://news.ycombinator.com/login (when you try to create a new username):
    'Usernames can only contain letters, digits, dashes and underscores, and should be between 2 and 15 characters long.'

    Returns True if the username is a valid Hacker News username, False otherwise.
    """
    # Check the length of the username
    if not (2 <= len(username) <= 15):
        return False

    # Check each character in the username
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    for char in username:
        if char not in valid_chars:
            return False

    return True


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
    if not __is_valid_hacker_news_username(username):
        raise ValueError("invalid username")
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
