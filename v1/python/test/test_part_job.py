# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.6
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.part_job import PartJob  # noqa: E501
from carbon3d.rest import ApiException

class TestPartJob(unittest.TestCase):
    """PartJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartJob
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part_job.PartJob()  # noqa: E501
        if include_optional :
            return PartJob(
                uuid = 'ee1d009e-1af4-408c-bd52-18b41a4acd26', 
                part_uuid = 'ee1d009e-1af4-408c-bd52-18b41a4acd26', 
                status = 'waiting', 
                failure_reason = 'other', 
                model_uuid = 'ee1d009e-1af4-408c-bd52-18b41a4acd26', 
                model_program_uuid = '5fcb4d31-7f69-453b-95c0-9b91c107c8dc', 
                model_program_parameters = {"~MODEL_UUID~":"63db11ee-a130-4ddf-b3d2-ab2c5d1852ed"}, 
                build_sop_uuid = 'ee1d009e-1af4-408c-bd52-18b41a4acd26', 
                print_sop_uuid = 'ee1d009e-1af4-408c-bd52-18b41a4acd26', 
                group_name = 'case-1A', 
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                split_group = True
            )
        else :
            return PartJob(
                model_uuid = 'ee1d009e-1af4-408c-bd52-18b41a4acd26',
                model_program_uuid = '5fcb4d31-7f69-453b-95c0-9b91c107c8dc',
                model_program_parameters = {"~MODEL_UUID~":"63db11ee-a130-4ddf-b3d2-ab2c5d1852ed"},
                build_sop_uuid = 'ee1d009e-1af4-408c-bd52-18b41a4acd26',
                print_sop_uuid = 'ee1d009e-1af4-408c-bd52-18b41a4acd26',
                group_name = 'case-1A',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testPartJob(self):
        """Test PartJob"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
