# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.order_request_parts import OrderRequestParts  # noqa: E501
from carbon3d.rest import ApiException

class TestOrderRequestParts(unittest.TestCase):
    """OrderRequestParts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrderRequestParts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.order_request_parts.OrderRequestParts()  # noqa: E501
        if include_optional :
            return OrderRequestParts(
                uuid = '0'
            )
        else :
            return OrderRequestParts(
        )

    def testOrderRequestParts(self):
        """Test OrderRequestParts"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
