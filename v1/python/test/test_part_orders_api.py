# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.12
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.part_orders_api import PartOrdersApi  # noqa: E501
from carbon3d.rest import ApiException


class TestPartOrdersApi(unittest.TestCase):
    """PartOrdersApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.part_orders_api.PartOrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_part_order(self):
        """Test case for create_part_order

        Create a PartOrder  # noqa: E501
        """
        pass

    def test_delete_part_order(self):
        """Test case for delete_part_order

        Cancel a PartOrder  # noqa: E501
        """
        pass

    def test_get_part_order(self):
        """Test case for get_part_order

        Get a PartOrder  # noqa: E501
        """
        pass

    def test_get_part_orders(self):
        """Test case for get_part_orders

        Fetch part orders  # noqa: E501
        """
        pass

    def test_update_part_order(self):
        """Test case for update_part_order

        Update a PartOrder  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
