# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.17
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintOrderUpdateRequest(object):
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
        'print_order_number': 'str',
        'print_order_tags': 'dict(str, str)',
        'notes': 'str'
    }

    attribute_map = {
        'print_order_number': 'print_order_number',
        'print_order_tags': 'print_order_tags',
        'notes': 'notes'
    }

    def __init__(self, print_order_number=None, print_order_tags=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """PrintOrderUpdateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._print_order_number = None
        self._print_order_tags = None
        self._notes = None
        self.discriminator = None

        if print_order_number is not None:
            self.print_order_number = print_order_number
        if print_order_tags is not None:
            self.print_order_tags = print_order_tags
        if notes is not None:
            self.notes = notes

    @property
    def print_order_number(self):
        """Gets the print_order_number of this PrintOrderUpdateRequest.  # noqa: E501

        Customer-provided print order number  # noqa: E501

        :return: The print_order_number of this PrintOrderUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._print_order_number

    @print_order_number.setter
    def print_order_number(self, print_order_number):
        """Sets the print_order_number of this PrintOrderUpdateRequest.

        Customer-provided print order number  # noqa: E501

        :param print_order_number: The print_order_number of this PrintOrderUpdateRequest.  # noqa: E501
        :type: str
        """

        self._print_order_number = print_order_number

    @property
    def print_order_tags(self):
        """Gets the print_order_tags of this PrintOrderUpdateRequest.  # noqa: E501

        Key value pairs to be associated with print order  # noqa: E501

        :return: The print_order_tags of this PrintOrderUpdateRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._print_order_tags

    @print_order_tags.setter
    def print_order_tags(self, print_order_tags):
        """Sets the print_order_tags of this PrintOrderUpdateRequest.

        Key value pairs to be associated with print order  # noqa: E501

        :param print_order_tags: The print_order_tags of this PrintOrderUpdateRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._print_order_tags = print_order_tags

    @property
    def notes(self):
        """Gets the notes of this PrintOrderUpdateRequest.  # noqa: E501

        Notes associated with  # noqa: E501

        :return: The notes of this PrintOrderUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PrintOrderUpdateRequest.

        Notes associated with  # noqa: E501

        :param notes: The notes of this PrintOrderUpdateRequest.  # noqa: E501
        :type: str
        """

        self._notes = notes

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
        if not isinstance(other, PrintOrderUpdateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintOrderUpdateRequest):
            return True

        return self.to_dict() != other.to_dict()
