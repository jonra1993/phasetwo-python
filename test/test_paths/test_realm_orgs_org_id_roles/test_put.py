# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import phasetwo
from phasetwo.paths.realm_orgs_org_id_roles import put  # noqa: E501
from phasetwo import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRealmOrgsOrgIdRoles(ApiTestMixin, unittest.TestCase):
    """
    RealmOrgsOrgIdRoles unit test stubs
        Create new roles for this organization  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 207






if __name__ == '__main__':
    unittest.main()
