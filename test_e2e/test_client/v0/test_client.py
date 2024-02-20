import time
import unittest

from hn_sdk.client.v0.client import get_item_by_id


class TestClient(unittest.TestCase):
    __DELAY_BETWEEN_TESTS = 0.25
    __RESPONSE_REQUIRED_KEYS = ["id"]
    __TEST_STORY_ID = 8863
    __TEST_COMMENT_ID = 2921983
    __TEST_ASK_ID = 121003
    __TEST_JOB_ID = 192327
    __TEST_POLL_ID = 126809
    __TEST_ITEM_PART_ID = 160705

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
