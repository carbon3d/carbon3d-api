# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.models_response import ModelsResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestModelsResponse(unittest.TestCase):
    """ModelsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.models_response.ModelsResponse()  # noqa: E501
        if include_optional :
            return ModelsResponse(
                limit = 56, 
                next_cursor = 'dXNlcjpXMDdRQ1JQQTQ=', 
                total_count = 56, 
                models = [
                    carbon3d.models.model.Model(
                        uuid = '1cf34076-417e-489f-8863-3438facd4808', 
                        filename = 'file.stl', 
                        application_uuid = '6401c93f-f340-4da2-8784-bddd4065e75c', )
                    ]
            )
        else :
            return ModelsResponse(
        )

    def testModelsResponse(self):
        """Test ModelsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
