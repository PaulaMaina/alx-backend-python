#!/usr/bin/env python3
"""Module for testing the client module"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from typing import Dict
from unittest.mock import MagicMock, Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrgClient tests"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, resp: Dict, mocked_fn: MagicMock) -> None:
        """org tests"""
        mocked_fn.return_value = MagicMock(return_value=resp)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), resp)
        mocked_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org),
        )

    def test_public_repos_url(self) -> None:
        """public_repos_url tests"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mockOrg:
            mockOrg.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )


@patch("client.get_json")
def test_public_repos(self, get_json_mock: MAgicMock) -> None:
    """public_repos tests"""
    test_payload = {
        'repos_url': "https://api.github.com/users/google/repos",
        'repos': [
            {
                "id": 7697149,
                "name": "episodes.dart",
                "private": False,
                "owner": {
                    "login": "google",
                    "id": 1342004,
                },
                "fork": False,
                "url": "https://api.github.com/repos/google/episodes.dart",
                "created_at": "2013-01-19T00:31:37Z",
                "updated_at": "2019-09-23T11:53:58Z",
                "has_issues": True,
                "forks": 22,
                "default_branch": "master",
            },
            {
                "id": 8566972,
                "name": "kratu",
                "private": False,
                "owner": {
                    "login": "google",
                    "id": 1342004,
                },
                "fork": False,
                "url": "https://api.github.com/repos/google/kratu",
                "created_at": "2013-03-04T22:52:33Z",
                "updated_at": "2019-11-15T22:22:16Z",
                "has_issues": True,
                "forks": 32,
                "default_branch": "master",
            },
        ]
    }
    get_json_mock.return_value = test_payload["repos"]
    with patch(
        "client.GithubOrgClient._public_repos_url",
        new_callable=PropertyMock,
    ) as pulic_repos_mock:
        public_repos_mock.return_value = test_payload["repos_url"]
        self.assertEqual(
             GithubOrgClient("google").public_repos(),
             ["episodes.dart", "kratu"],
        )
        public_repos_mock.assert_called_once()
        get_json_mock.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """has_license test"""
        org_client = GithubOrgClient("google")
        client_license = org_client.has_license(repo, key)
        self.assertEqual(client_license, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithbuOrgClient(unittest.TestCase):
    """Integrations tests for GithubOrgClient"""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets fixtures up before running the tests"""
        payload_route = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in payload_route:
                return Mock(**{'json.return_value': payload_route[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """public_repos tests"""
        self.assertEqual(
            GithubOrgClient("google").public_repos()
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Test public_repos iwth a license"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Deletes class fixtures after running tests"""
        cls.get_patcher.stop()
