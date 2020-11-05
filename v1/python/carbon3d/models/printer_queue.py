# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrinterQueue(object):
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
        'printer_serial': 'str',
        'updated_at': 'datetime',
        'print_uuids': 'list[str]'
    }

    attribute_map = {
        'printer_serial': 'printer_serial',
        'updated_at': 'updated_at',
        'print_uuids': 'print_uuids'
    }

    def __init__(self, printer_serial=None, updated_at=None, print_uuids=None, local_vars_configuration=None):  # noqa: E501
        """PrinterQueue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._printer_serial = None
        self._updated_at = None
        self._print_uuids = None
        self.discriminator = None

        if printer_serial is not None:
            self.printer_serial = printer_serial
        if updated_at is not None:
            self.updated_at = updated_at
        if print_uuids is not None:
            self.print_uuids = print_uuids

    @property
    def printer_serial(self):
        """Gets the printer_serial of this PrinterQueue.  # noqa: E501


        :return: The printer_serial of this PrinterQueue.  # noqa: E501
        :rtype: str
        """
        return self._printer_serial

    @printer_serial.setter
    def printer_serial(self, printer_serial):
        """Sets the printer_serial of this PrinterQueue.


        :param printer_serial: The printer_serial of this PrinterQueue.  # noqa: E501
        :type: str
        """

        self._printer_serial = printer_serial

    @property
    def updated_at(self):
        """Gets the updated_at of this PrinterQueue.  # noqa: E501


        :return: The updated_at of this PrinterQueue.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PrinterQueue.


        :param updated_at: The updated_at of this PrinterQueue.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def print_uuids(self):
        """Gets the print_uuids of this PrinterQueue.  # noqa: E501


        :return: The print_uuids of this PrinterQueue.  # noqa: E501
        :rtype: list[str]
        """
        return self._print_uuids

    @print_uuids.setter
    def print_uuids(self, print_uuids):
        """Sets the print_uuids of this PrinterQueue.


        :param print_uuids: The print_uuids of this PrinterQueue.  # noqa: E501
        :type: list[str]
        """

        self._print_uuids = print_uuids

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
        if not isinstance(other, PrinterQueue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrinterQueue):
            return True

        return self.to_dict() != other.to_dict()
