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


class PrinterPrints(object):
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
        'last': 'PrintRef',
        'current': 'PrintRef',
        'next': 'PrintRef',
        'queue_length': 'int'
    }

    attribute_map = {
        'last': 'last',
        'current': 'current',
        'next': 'next',
        'queue_length': 'queue_length'
    }

    def __init__(self, last=None, current=None, next=None, queue_length=None, local_vars_configuration=None):  # noqa: E501
        """PrinterPrints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last = None
        self._current = None
        self._next = None
        self._queue_length = None
        self.discriminator = None

        if last is not None:
            self.last = last
        if current is not None:
            self.current = current
        if next is not None:
            self.next = next
        self.queue_length = queue_length

    @property
    def last(self):
        """Gets the last of this PrinterPrints.  # noqa: E501


        :return: The last of this PrinterPrints.  # noqa: E501
        :rtype: PrintRef
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this PrinterPrints.


        :param last: The last of this PrinterPrints.  # noqa: E501
        :type: PrintRef
        """

        self._last = last

    @property
    def current(self):
        """Gets the current of this PrinterPrints.  # noqa: E501


        :return: The current of this PrinterPrints.  # noqa: E501
        :rtype: PrintRef
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this PrinterPrints.


        :param current: The current of this PrinterPrints.  # noqa: E501
        :type: PrintRef
        """

        self._current = current

    @property
    def next(self):
        """Gets the next of this PrinterPrints.  # noqa: E501


        :return: The next of this PrinterPrints.  # noqa: E501
        :rtype: PrintRef
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PrinterPrints.


        :param next: The next of this PrinterPrints.  # noqa: E501
        :type: PrintRef
        """

        self._next = next

    @property
    def queue_length(self):
        """Gets the queue_length of this PrinterPrints.  # noqa: E501


        :return: The queue_length of this PrinterPrints.  # noqa: E501
        :rtype: int
        """
        return self._queue_length

    @queue_length.setter
    def queue_length(self, queue_length):
        """Sets the queue_length of this PrinterPrints.


        :param queue_length: The queue_length of this PrinterPrints.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and queue_length is None:  # noqa: E501
            raise ValueError("Invalid value for `queue_length`, must not be `None`")  # noqa: E501

        self._queue_length = queue_length

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
        if not isinstance(other, PrinterPrints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrinterPrints):
            return True

        return self.to_dict() != other.to_dict()
