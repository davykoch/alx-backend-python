#!/usr/bin/env python3
"""
Module for integration testing of the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test class for GithubOrgClient.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the integration tests.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function for mocking requests.get"""
            if url.endswith("/orgs/google"):
                return unittest.mock.Mock(json=lambda: cls.org_payload)
            elif url.endswith("/orgs/google/repos"):
                return unittest.mock.Mock(json=lambda: cls.repos_payload)
            return unittest.mock.Mock(json=lambda: {})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method for the integration tests.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Integration test for the public_repos method.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Integration test for the public_repos method with a license filter.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
