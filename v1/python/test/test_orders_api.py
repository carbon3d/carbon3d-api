# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.5
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.orders_api import OrdersApi  # noqa: E501
from carbon3d.rest import ApiException


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.orders_api.OrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_order(self):
        """Test case for create_order

        Create an Order  # noqa: E501
        """
        pass

    def test_delete_order(self):
        """Test case for delete_order

        Cancel an Order  # noqa: E501
        """
        pass

    def test_get_order(self):
        """Test case for get_order

        Get an Order  # noqa: E501
        """
        pass

    def test_get_orders(self):
        """Test case for get_orders

        Fetch orders  # noqa: E501
        """
        pass

    def test_update_order(self):
        """Test case for update_order

        Update an Order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
