# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.7
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.model_program_run_request import ModelProgramRunRequest  # noqa: E501
from carbon3d.rest import ApiException

class TestModelProgramRunRequest(unittest.TestCase):
    """ModelProgramRunRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelProgramRunRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.model_program_run_request.ModelProgramRunRequest()  # noqa: E501
        if include_optional :
            return ModelProgramRunRequest(
                model_program_uuid = '0', 
                parameters = {
                    'key' : '0'
                    }
            )
        else :
            return ModelProgramRunRequest(
                model_program_uuid = '0',
                parameters = {
                    'key' : '0'
                    },
        )

    def testModelProgramRunRequest(self):
        """Test ModelProgramRunRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
