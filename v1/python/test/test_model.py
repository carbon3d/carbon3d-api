# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.16
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
                external_id = '3ec320f4-f248-11ed-a05b-0242ac120003', 
                application_uuid = '6401c93f-f340-4da2-8784-bddd4065e75c', 
                description = 'Sample model description', 
                file_size_bytes = 1024, 
                updated_at = '2017-07-21T17:32:28Z', 
                created_at = '2017-07-21T17:32:28Z', 
                created_by = 'John Doe'
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
