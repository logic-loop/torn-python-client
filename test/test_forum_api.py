# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 1.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tornclient.api.forum_api import ForumApi


class TestForumApi(unittest.TestCase):
    """ForumApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ForumApi()

    def tearDown(self) -> None:
        pass

    def test_forum_categories_get(self) -> None:
        """Test case for forum_categories_get

        Get publicly available forum categories
        """
        pass

    def test_forum_category_ids_threads_get(self) -> None:
        """Test case for forum_category_ids_threads_get

        Get threads for specific public forum category or categories
        """
        pass

    def test_forum_get(self) -> None:
        """Test case for forum_get

        Get any Forum selection
        """
        pass

    def test_forum_lookup_get(self) -> None:
        """Test case for forum_lookup_get

        Get all available forum selections
        """
        pass

    def test_forum_thread_id_posts_get(self) -> None:
        """Test case for forum_thread_id_posts_get

        Get specific forum thread posts
        """
        pass

    def test_forum_thread_id_thread_get(self) -> None:
        """Test case for forum_thread_id_thread_get

        Get specific thread details
        """
        pass

    def test_forum_threads_get(self) -> None:
        """Test case for forum_threads_get

        Get threads across all forum categories
        """
        pass

    def test_forum_timestamp_get(self) -> None:
        """Test case for forum_timestamp_get

        Get current server time
        """
        pass


if __name__ == '__main__':
    unittest.main()
