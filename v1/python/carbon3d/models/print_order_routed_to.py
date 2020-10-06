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


class PrintOrderRoutedTo(object):
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
        'copies_queued': 'int',
        'copies_printed': 'int'
    }

    attribute_map = {
        'copies_queued': 'copies_queued',
        'copies_printed': 'copies_printed'
    }

    def __init__(self, copies_queued=None, copies_printed=None, local_vars_configuration=None):  # noqa: E501
        """PrintOrderRoutedTo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._copies_queued = None
        self._copies_printed = None
        self.discriminator = None

        if copies_queued is not None:
            self.copies_queued = copies_queued
        if copies_printed is not None:
            self.copies_printed = copies_printed

    @property
    def copies_queued(self):
        """Gets the copies_queued of this PrintOrderRoutedTo.  # noqa: E501


        :return: The copies_queued of this PrintOrderRoutedTo.  # noqa: E501
        :rtype: int
        """
        return self._copies_queued

    @copies_queued.setter
    def copies_queued(self, copies_queued):
        """Sets the copies_queued of this PrintOrderRoutedTo.


        :param copies_queued: The copies_queued of this PrintOrderRoutedTo.  # noqa: E501
        :type: int
        """

        self._copies_queued = copies_queued

    @property
    def copies_printed(self):
        """Gets the copies_printed of this PrintOrderRoutedTo.  # noqa: E501


        :return: The copies_printed of this PrintOrderRoutedTo.  # noqa: E501
        :rtype: int
        """
        return self._copies_printed

    @copies_printed.setter
    def copies_printed(self, copies_printed):
        """Sets the copies_printed of this PrintOrderRoutedTo.


        :param copies_printed: The copies_printed of this PrintOrderRoutedTo.  # noqa: E501
        :type: int
        """

        self._copies_printed = copies_printed

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
        if not isinstance(other, PrintOrderRoutedTo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintOrderRoutedTo):
            return True

        return self.to_dict() != other.to_dict()
