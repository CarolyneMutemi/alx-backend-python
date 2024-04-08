#!/usr/bin/env python3
"""
Testng the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
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

    @parameterized.expand([
        ("google", {"org_name": "google",
                    "repos_url": "https://github.com/googleURL"}),
        ("abc", {"org_name": "abc",
                 "repos_url": "https://github.com/abcURL"})
    ])
    def test_public_repos_url(self, name, payload):
        """
        Tests the GithubOrgClient._public_repos_url method.
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            organization = GithubOrgClient(name)
            self.assertEqual(organization._public_repos_url,
                             payload["repos_url"])
