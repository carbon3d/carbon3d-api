# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.16
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class ModelProgramRunTypedRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'model_program_uuid': 'str',
        'parameters': 'list[OneOfStringParameterIntegerParameterDoubleParameter]'
    }

    attribute_map = {
        'model_program_uuid': 'model_program_uuid',
        'parameters': 'parameters'
    }

    def __init__(self, model_program_uuid=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """ModelProgramRunTypedRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_program_uuid = None
        self._parameters = None
        self.discriminator = None

        self.model_program_uuid = model_program_uuid
        self.parameters = parameters

    @property
    def model_program_uuid(self):
        """Gets the model_program_uuid of this ModelProgramRunTypedRequest.  # noqa: E501

        uuid for a model program  # noqa: E501

        :return: The model_program_uuid of this ModelProgramRunTypedRequest.  # noqa: E501
        :rtype: str
        """
        return self._model_program_uuid

    @model_program_uuid.setter
    def model_program_uuid(self, model_program_uuid):
        """Sets the model_program_uuid of this ModelProgramRunTypedRequest.

        uuid for a model program  # noqa: E501

        :param model_program_uuid: The model_program_uuid of this ModelProgramRunTypedRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and model_program_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `model_program_uuid`, must not be `None`")  # noqa: E501

        self._model_program_uuid = model_program_uuid

    @property
    def parameters(self):
        """Gets the parameters of this ModelProgramRunTypedRequest.  # noqa: E501

        parameters for the model program  # noqa: E501

        :return: The parameters of this ModelProgramRunTypedRequest.  # noqa: E501
        :rtype: list[OneOfStringParameterIntegerParameterDoubleParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ModelProgramRunTypedRequest.

        parameters for the model program  # noqa: E501

        :param parameters: The parameters of this ModelProgramRunTypedRequest.  # noqa: E501
        :type: list[OneOfStringParameterIntegerParameterDoubleParameter]
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelProgramRunTypedRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelProgramRunTypedRequest):
            return True

        return self.to_dict() != other.to_dict()
