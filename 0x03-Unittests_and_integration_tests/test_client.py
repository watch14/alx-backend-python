#!/usr/bin/env python3
"""Test cases for GithubOrgClient"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Testing Github Org Client"""

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """Test org method of GithubOrgClient"""
        test_class = GithubOrgClient(input)
        test_class.org()
        expected_url = f'https://api.github.com/orgs/{input}'
        mock_get_json.assert_called_once_with(expected_url)

    @patch.object(GithubOrgClient, 'org')
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property"""
        expected_payload = {'public_repos': 10}
        mock_org.return_value = expected_payload

        test_class = GithubOrgClient('testorg')
        expected_url = f'https://api.github.com/orgs/testorg/repos'
        self.assertEqual(test_class._public_repos_url, expected_url)


if __name__ == '__main__':
    unittest.main()
