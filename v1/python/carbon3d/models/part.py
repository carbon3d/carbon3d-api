# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class Part(object):
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
        'uuid': 'str',
        'part_number': 'str',
        'model_uuid': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'part_number': 'part_number',
        'model_uuid': 'model_uuid'
    }

    def __init__(self, uuid=None, part_number=None, model_uuid=None, local_vars_configuration=None):  # noqa: E501
        """Part - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._part_number = None
        self._model_uuid = None
        self.discriminator = None

        self.uuid = uuid
        self.part_number = part_number
        self.model_uuid = model_uuid

    @property
    def uuid(self):
        """Gets the uuid of this Part.  # noqa: E501

        Part UUID  # noqa: E501

        :return: The uuid of this Part.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Part.

        Part UUID  # noqa: E501

        :param uuid: The uuid of this Part.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def part_number(self):
        """Gets the part_number of this Part.  # noqa: E501

        Part Number  # noqa: E501

        :return: The part_number of this Part.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this Part.

        Part Number  # noqa: E501

        :param part_number: The part_number of this Part.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and part_number is None:  # noqa: E501
            raise ValueError("Invalid value for `part_number`, must not be `None`")  # noqa: E501

        self._part_number = part_number

    @property
    def model_uuid(self):
        """Gets the model_uuid of this Part.  # noqa: E501

        Model UUID  # noqa: E501

        :return: The model_uuid of this Part.  # noqa: E501
        :rtype: str
        """
        return self._model_uuid

    @model_uuid.setter
    def model_uuid(self, model_uuid):
        """Sets the model_uuid of this Part.

        Model UUID  # noqa: E501

        :param model_uuid: The model_uuid of this Part.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and model_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `model_uuid`, must not be `None`")  # noqa: E501

        self._model_uuid = model_uuid

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
        if not isinstance(other, Part):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Part):
            return True

        return self.to_dict() != other.to_dict()
