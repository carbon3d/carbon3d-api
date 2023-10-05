# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.12
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartRequest(object):
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
        'part_number': 'str',
        'model_uuid': 'str',
        'application_uuid': 'str'
    }

    attribute_map = {
        'part_number': 'part_number',
        'model_uuid': 'model_uuid',
        'application_uuid': 'application_uuid'
    }

    def __init__(self, part_number=None, model_uuid=None, application_uuid=None, local_vars_configuration=None):  # noqa: E501
        """PartRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._part_number = None
        self._model_uuid = None
        self._application_uuid = None
        self.discriminator = None

        self.part_number = part_number
        self.model_uuid = model_uuid
        if application_uuid is not None:
            self.application_uuid = application_uuid

    @property
    def part_number(self):
        """Gets the part_number of this PartRequest.  # noqa: E501

        Part Number (Must be Part Number that is associated with the specified Application)  # noqa: E501

        :return: The part_number of this PartRequest.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this PartRequest.

        Part Number (Must be Part Number that is associated with the specified Application)  # noqa: E501

        :param part_number: The part_number of this PartRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and part_number is None:  # noqa: E501
            raise ValueError("Invalid value for `part_number`, must not be `None`")  # noqa: E501

        self._part_number = part_number

    @property
    def model_uuid(self):
        """Gets the model_uuid of this PartRequest.  # noqa: E501

        Model UUID  # noqa: E501

        :return: The model_uuid of this PartRequest.  # noqa: E501
        :rtype: str
        """
        return self._model_uuid

    @model_uuid.setter
    def model_uuid(self, model_uuid):
        """Sets the model_uuid of this PartRequest.

        Model UUID  # noqa: E501

        :param model_uuid: The model_uuid of this PartRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and model_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `model_uuid`, must not be `None`")  # noqa: E501

        self._model_uuid = model_uuid

    @property
    def application_uuid(self):
        """Gets the application_uuid of this PartRequest.  # noqa: E501

        Application UUID  # noqa: E501

        :return: The application_uuid of this PartRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_uuid

    @application_uuid.setter
    def application_uuid(self, application_uuid):
        """Sets the application_uuid of this PartRequest.

        Application UUID  # noqa: E501

        :param application_uuid: The application_uuid of this PartRequest.  # noqa: E501
        :type: str
        """

        self._application_uuid = application_uuid

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
        if not isinstance(other, PartRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartRequest):
            return True

        return self.to_dict() != other.to_dict()
