#!/usr/bin/env python3
""" Parameterize and patch as decorators"""

from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """test_public_repos_url"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = TEST_PAYLOAD
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class._public_repos_url, TEST_PAYLOAD)
            mock_public_repos_url.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test_public_repos"""
        mock_get_json.return_value = TEST_PAYLOAD
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos(), TEST_PAYLOAD)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test/repos"
        )

    @parameterized.expand([
        ("google", "license"),
        ("abc", "license")
    ])
    def test_public_repos_with_license(self, org_name, license):
        """test_public_repos_with_license"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = TEST_PAYLOAD
            test_class = GithubOrgClient(org_name)
            self.assertEqual(test_class.public_repos(license), TEST_PAYLOAD)
            mock_public_repos_url.assert_called_once()
