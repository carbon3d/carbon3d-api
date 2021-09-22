# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.5
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.attachments_api import AttachmentsApi  # noqa: E501
from carbon3d.rest import ApiException


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.attachments_api.AttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        Download a file attachment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
