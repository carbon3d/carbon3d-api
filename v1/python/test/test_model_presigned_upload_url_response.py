# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.8
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.model_presigned_upload_url_response import ModelPresignedUploadUrlResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestModelPresignedUploadUrlResponse(unittest.TestCase):
    """ModelPresignedUploadUrlResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelPresignedUploadUrlResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.model_presigned_upload_url_response.ModelPresignedUploadUrlResponse()  # noqa: E501
        if include_optional :
            return ModelPresignedUploadUrlResponse(
                presigned_url = '0', 
                model_uuid = 'aaaaaaaa-f340-4da2-8784-bddd4065e75c'
            )
        else :
            return ModelPresignedUploadUrlResponse(
                presigned_url = '0',
                model_uuid = 'aaaaaaaa-f340-4da2-8784-bddd4065e75c',
        )

    def testModelPresignedUploadUrlResponse(self):
        """Test ModelPresignedUploadUrlResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
