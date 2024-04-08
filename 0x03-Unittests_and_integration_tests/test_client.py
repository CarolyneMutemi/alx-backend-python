#!/usr/bin/python3
"""
Testng the client module.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Testing the GithubOrgClient class attributes.
    """

    @parameterized.expand([
        ("google", {"org_name": "google"}),
        ("abc", {"org_name": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org, payload, mock_get_json):
        """
        Testing the GithubOrgClient.org method.
        """
        organisation = GithubOrgClient(org)
        mock_get_json.return_value = payload
        self.assertEqual(organisation.org, payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
            )
        mock_get_json.resert_mock()
