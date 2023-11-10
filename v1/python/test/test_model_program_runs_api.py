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

import carbon3d
from carbon3d.api.model_program_runs_api import ModelProgramRunsApi  # noqa: E501
from carbon3d.rest import ApiException


class TestModelProgramRunsApi(unittest.TestCase):
    """ModelProgramRunsApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.model_program_runs_api.ModelProgramRunsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_model_program_run(self):
        """Test case for create_model_program_run

        Run a model program to alter your models  # noqa: E501
        """
        pass

    def test_create_model_program_run_typed_params(self):
        """Test case for create_model_program_run_typed_params

        Run a model program to alter your models with typed params  # noqa: E501
        """
        pass

    def test_get_model_program_run(self):
        """Test case for get_model_program_run

        Get a model program run by UUID  # noqa: E501
        """
        pass

    def test_get_model_program_runs(self):
        """Test case for get_model_program_runs

        Get a list of model program runs based on their uuids  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
