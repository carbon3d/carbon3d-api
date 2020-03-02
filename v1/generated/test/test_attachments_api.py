# coding: utf-8

"""
    Carbon API

    An API to interact with Carbon's Manufacturing Cloud including 3D model upload, automated order processing and part history.  Getting started ---------------  - [Generate and download an API key](https://print.carbon3d.com/api_keys)   - Your API key and client secret will be downloaded into a secret.json file.  - [Use generated API key to generate a JWT token](/token_generator) from the api key.   - If your API key is revoked, this token will no longer work.  - Authorize with generated token  - Upload mesh files  - Create orders  - Monitor order status   # noqa: E501

    The version of the OpenAPI document: 0.0.3
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
