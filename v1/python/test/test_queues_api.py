# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.17
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.queues_api import QueuesApi  # noqa: E501
from carbon3d.rest import ApiException


class TestQueuesApi(unittest.TestCase):
    """QueuesApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.queues_api.QueuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_printer_queues(self):
        """Test case for get_printer_queues

        Fetch all printers' queues  # noqa: E501
        """
        pass

    def test_update_printer_queue(self):
        """Test case for update_printer_queue

        Update a Printer queue  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
