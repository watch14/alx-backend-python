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

    @patch.object(
            GithubOrgClient,
            '_public_repos_url',
            return_value='https://api.github.com/orgs/testorg/repos')
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        """Test public_repos method of GithubOrgClient"""
        payload = [{'name': 'repo1'}, {'name': 'repo2'}, {'name': 'repo3'}]
        mock_get_json.return_value = payload

        test_class = GithubOrgClient('testorg')
        repos = test_class.public_repos()

        self.assertEqual(repos, ['repo1', 'repo2', 'repo3'])

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/testorg/repos')


if __name__ == '__main__':
    unittest.main()
