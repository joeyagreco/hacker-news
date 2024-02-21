import time
import unittest

from hn_sdk.client.v0.client import (
    get_ask_stories,
    get_best_stories,
    get_item_by_id,
    get_job_stories,
    get_max_item_id,
    get_new_stories,
    get_show_stories,
    get_top_stories,
    get_updates,
    get_user_by_username,
)


class TestClient(unittest.TestCase):
    __DELAY_BETWEEN_TESTS = 0.5
    __RESPONSE_REQUIRED_KEYS = ["id"]
    __TEST_STORY_ID = 8863
    __TEST_COMMENT_ID = 2921983
    __TEST_ASK_ID = 121003
    __TEST_JOB_ID = 192327
    __TEST_POLL_ID = 126809
    __TEST_ITEM_PART_ID = 160705
    __TEST_USERNAME = "jl"

    def setUp(self) -> None:
        # sleep before each test to avoid hitting rate limits.
        time.sleep(self.__DELAY_BETWEEN_TESTS)

    def __required_keys_in_response(self, response: dict) -> bool:
        """
        Checks for required keys in a response.
        """
        for key in self.__RESPONSE_REQUIRED_KEYS:
            if key not in response.keys():
                return False
        return True

    def test_get_item_by_id_item_id_not_int_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            get_item_by_id("foo")
        self.assertEqual("item id must be an integer", str(context.exception))

    def test_get_item_by_id_story(self):
        resp = get_item_by_id(self.__TEST_STORY_ID)
        self.assertIsInstance(resp, dict)
        self.assertTrue(self.__required_keys_in_response(resp))

    def test_get_item_by_id_comment(self):
        resp = get_item_by_id(self.__TEST_COMMENT_ID)
        self.assertIsInstance(resp, dict)
        self.assertTrue(self.__required_keys_in_response(resp))

    def test_get_item_by_id_ask(self):
        resp = get_item_by_id(self.__TEST_ASK_ID)
        self.assertIsInstance(resp, dict)
        self.assertTrue(self.__required_keys_in_response(resp))

    def test_get_item_by_id_job(self):
        resp = get_item_by_id(self.__TEST_JOB_ID)
        self.assertIsInstance(resp, dict)
        self.assertTrue(self.__required_keys_in_response(resp))

    def test_get_item_by_id_poll(self):
        resp = get_item_by_id(self.__TEST_POLL_ID)
        self.assertIsInstance(resp, dict)
        self.assertTrue(self.__required_keys_in_response(resp))

    def test_get_item_by_id_item_part(self):
        resp = get_item_by_id(self.__TEST_ITEM_PART_ID)
        self.assertIsInstance(resp, dict)
        self.assertTrue(self.__required_keys_in_response(resp))

    def test_get_user_by_username(self):
        resp = get_user_by_username(self.__TEST_USERNAME)
        self.assertIsInstance(resp, dict)
        self.assertTrue(self.__required_keys_in_response(resp))

    def test_get_user_by_username_invalid_username_raises_exception(self):
        # too short
        with self.assertRaises(ValueError) as context:
            get_user_by_username("a")
        self.assertEqual("invalid username", str(context.exception))
        # too long
        with self.assertRaises(ValueError) as context:
            get_user_by_username("a" * 16)
        self.assertEqual("invalid username", str(context.exception))
        # contains "/"
        with self.assertRaises(ValueError) as context:
            get_user_by_username("abc/")
        self.assertEqual("invalid username", str(context.exception))
        # contains "\"
        with self.assertRaises(ValueError) as context:
            get_user_by_username("abc\\")
        self.assertEqual("invalid username", str(context.exception))
        # contains "@"
        with self.assertRaises(ValueError) as context:
            get_user_by_username("abc@")
        self.assertEqual("invalid username", str(context.exception))
        # contains " "
        with self.assertRaises(ValueError) as context:
            get_user_by_username("abc ")
        self.assertEqual("invalid username", str(context.exception))

    def test_get_max_item_id(self):
        resp = get_max_item_id()
        self.assertIsInstance(resp, int)

    def test_get_top_stories(self):
        resp = get_top_stories()
        self.assertIsInstance(resp, list)
        # NOTE: can be up to 500
        self.assertTrue(len(resp) >= 1)
        self.assertIsInstance(resp[0], int)

    def test_get_new_stories(self):
        resp = get_new_stories()
        self.assertIsInstance(resp, list)
        # NOTE: can be up to 500
        self.assertTrue(len(resp) >= 1)
        self.assertIsInstance(resp[0], int)

    def test_get_best_stories(self):
        resp = get_best_stories()
        self.assertIsInstance(resp, list)
        # NOTE: can be up to 500
        self.assertTrue(len(resp) >= 1)
        self.assertIsInstance(resp[0], int)

    def test_get_ask_stories(self):
        resp = get_ask_stories()
        self.assertIsInstance(resp, list)
        # NOTE: can be up to 200
        self.assertTrue(len(resp) >= 1)
        self.assertIsInstance(resp[0], int)

    def test_get_show_stories(self):
        resp = get_show_stories()
        self.assertIsInstance(resp, list)
        # NOTE: can be up to 200
        self.assertTrue(len(resp) >= 1)
        self.assertIsInstance(resp[0], int)

    def test_get_job_stories(self):
        resp = get_job_stories()
        self.assertIsInstance(resp, list)
        # NOTE: can be up to 200
        self.assertTrue(len(resp) >= 1)
        self.assertIsInstance(resp[0], int)

    def test_get_updates(self):
        resp = get_updates()
        self.assertIsInstance(resp, dict)
        self.assertTrue("items" in resp.keys())
        self.assertIsInstance(resp["items"], list)
        self.assertTrue("profiles" in resp.keys())
        self.assertIsInstance(resp["profiles"], list)
