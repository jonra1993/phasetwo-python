# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import phasetwo_client
from phasetwo_client.paths.realm_orgs_org_id_idps_alias_mappers import post  # noqa: E501
from phasetwo_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRealmOrgsOrgIdIdpsAliasMappers(ApiTestMixin, unittest.TestCase):
    """
    RealmOrgsOrgIdIdpsAliasMappers unit test stubs
        Add a mapper to identity provider  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201
    response_body = ''




if __name__ == '__main__':
    unittest.main()
