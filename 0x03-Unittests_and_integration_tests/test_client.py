#!/usr/bin/env python3
"""
Testng the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
import client


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

    @parameterized.expand([
        ("google", "https://github.com/googleURL",
         {"repo1": {"name": "images"},
          "repo2": {"name": "videos"},
          "repo3": {"name": "map"}}),
        ("abc", "https://github.com/abcURL",
         {"repo1": {"name": "clients"},
          "repo2": {"name": "suppliers"},
          "repo3": {"name": "services"}})
    ])
    @patch("client.get_json")
    def test_public_repos(self, name, url, payload, mock_get_json):
        """
        Tests the TestGithubOrgClient.test_public_repos method.
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mocked_url:
            mocked_url.return_value = url
            mock_get_json.return_value = payload
            mocked_url.reset_mock()
            org = GithubOrgClient(name)
            repos_list = [payload[repo]["name"] for repo in payload]
            org.public_repos()
            org.public_repos()
            self.assertEqual(org.public_repos(), repos_list)
            mock_get_json.assert_called_once_with(url)
            mocked_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license")
    ])
    def test_has_license(self, repo, license_key):
        """
        Test the has_license static method.
        """
        try:
            self.assertTrue(GithubOrgClient.has_license(repo, license_key))
        except AssertionError:
            self.assertFalse(GithubOrgClient.has_license(repo, license_key))
