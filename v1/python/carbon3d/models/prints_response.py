# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintsResponse(object):
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
        'prints': 'list[ModelPrint]',
        'total_count': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'prints': 'prints',
        'total_count': 'total_count',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, prints=None, total_count=None, offset=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """PrintsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._prints = None
        self._total_count = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if prints is not None:
            self.prints = prints
        if total_count is not None:
            self.total_count = total_count
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def prints(self):
        """Gets the prints of this PrintsResponse.  # noqa: E501


        :return: The prints of this PrintsResponse.  # noqa: E501
        :rtype: list[ModelPrint]
        """
        return self._prints

    @prints.setter
    def prints(self, prints):
        """Sets the prints of this PrintsResponse.


        :param prints: The prints of this PrintsResponse.  # noqa: E501
        :type: list[ModelPrint]
        """

        self._prints = prints

    @property
    def total_count(self):
        """Gets the total_count of this PrintsResponse.  # noqa: E501


        :return: The total_count of this PrintsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PrintsResponse.


        :param total_count: The total_count of this PrintsResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def offset(self):
        """Gets the offset of this PrintsResponse.  # noqa: E501


        :return: The offset of this PrintsResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PrintsResponse.


        :param offset: The offset of this PrintsResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PrintsResponse.  # noqa: E501


        :return: The limit of this PrintsResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PrintsResponse.


        :param limit: The limit of this PrintsResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

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
        if not isinstance(other, PrintsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintsResponse):
            return True

        return self.to_dict() != other.to_dict()
