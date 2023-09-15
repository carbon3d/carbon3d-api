# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.10
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.models_api import ModelsApi  # noqa: E501
from carbon3d.rest import ApiException


class TestModelsApi(unittest.TestCase):
    """ModelsApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.models_api.ModelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_download_model(self):
        """Test case for download_model

        Download a model by UUID  # noqa: E501
        """
        pass

    def test_find_models(self):
        """Test case for find_models

        Fetch models  # noqa: E501
        """
        pass

    def test_get_model(self):
        """Test case for get_model

        Get a model by UUID  # noqa: E501
        """
        pass

    def test_get_presigned_upload_url(self):
        """Test case for get_presigned_upload_url

        Create presigned upload URL for a filename  # noqa: E501
        """
        pass

    def test_resolve_presigned_model_upload(self):
        """Test case for resolve_presigned_model_upload

        Resolve presigned model upload  # noqa: E501
        """
        pass

    def test_upload_model(self):
        """Test case for upload_model

        Upload a model  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
