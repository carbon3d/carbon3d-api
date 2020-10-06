# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintedPartTags(object):
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
        'part_number': 'dict(str, str)',
        'part': 'dict(str, str)',
        'printed_part': 'dict(str, str)'
    }

    attribute_map = {
        'part_number': 'part_number',
        'part': 'part',
        'printed_part': 'printed_part'
    }

    def __init__(self, part_number=None, part=None, printed_part=None, local_vars_configuration=None):  # noqa: E501
        """PrintedPartTags - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._part_number = None
        self._part = None
        self._printed_part = None
        self.discriminator = None

        if part_number is not None:
            self.part_number = part_number
        if part is not None:
            self.part = part
        if printed_part is not None:
            self.printed_part = printed_part

    @property
    def part_number(self):
        """Gets the part_number of this PrintedPartTags.  # noqa: E501

        Key value pairs to be associated with part number  # noqa: E501

        :return: The part_number of this PrintedPartTags.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this PrintedPartTags.

        Key value pairs to be associated with part number  # noqa: E501

        :param part_number: The part_number of this PrintedPartTags.  # noqa: E501
        :type: dict(str, str)
        """

        self._part_number = part_number

    @property
    def part(self):
        """Gets the part of this PrintedPartTags.  # noqa: E501

        Key value pairs to be associated with part  # noqa: E501

        :return: The part of this PrintedPartTags.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._part

    @part.setter
    def part(self, part):
        """Sets the part of this PrintedPartTags.

        Key value pairs to be associated with part  # noqa: E501

        :param part: The part of this PrintedPartTags.  # noqa: E501
        :type: dict(str, str)
        """

        self._part = part

    @property
    def printed_part(self):
        """Gets the printed_part of this PrintedPartTags.  # noqa: E501

        Key value pairs to be associated with printed part  # noqa: E501

        :return: The printed_part of this PrintedPartTags.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._printed_part

    @printed_part.setter
    def printed_part(self, printed_part):
        """Sets the printed_part of this PrintedPartTags.

        Key value pairs to be associated with printed part  # noqa: E501

        :param printed_part: The printed_part of this PrintedPartTags.  # noqa: E501
        :type: dict(str, str)
        """

        self._printed_part = printed_part

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
        if not isinstance(other, PrintedPartTags):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintedPartTags):
            return True

        return self.to_dict() != other.to_dict()
