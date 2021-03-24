# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.model import Model  # noqa: E501
from carbon3d.rest import ApiException

class TestModel(unittest.TestCase):
    """Model unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Model
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.model.Model()  # noqa: E501
        if include_optional :
            return Model(
                uuid = '1cf34076-417e-489f-8863-3438facd4808', 
                filename = 'file.stl', 
                application_uuid = '6401c93f-f340-4da2-8784-bddd4065e75c'
            )
        else :
            return Model(
                uuid = '1cf34076-417e-489f-8863-3438facd4808',
                filename = 'file.stl',
        )

    def testModel(self):
        """Test Model"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
