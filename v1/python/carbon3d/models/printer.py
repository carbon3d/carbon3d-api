# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.5
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class Printer(object):
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
        'name': 'str',
        'serial': 'str',
        'hw_type': 'str',
        'url': 'str',
        'updated_at': 'datetime',
        'status': 'PrinterStatus',
        'prints': 'PrinterPrints'
    }

    attribute_map = {
        'name': 'name',
        'serial': 'serial',
        'hw_type': 'hw_type',
        'url': 'url',
        'updated_at': 'updated_at',
        'status': 'status',
        'prints': 'prints'
    }

    def __init__(self, name=None, serial=None, hw_type=None, url=None, updated_at=None, status=None, prints=None, local_vars_configuration=None):  # noqa: E501
        """Printer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._serial = None
        self._hw_type = None
        self._url = None
        self._updated_at = None
        self._status = None
        self._prints = None
        self.discriminator = None

        self.name = name
        self.serial = serial
        self.hw_type = hw_type
        self.url = url
        self.updated_at = updated_at
        self.status = status
        self.prints = prints

    @property
    def name(self):
        """Gets the name of this Printer.  # noqa: E501


        :return: The name of this Printer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Printer.


        :param name: The name of this Printer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def serial(self):
        """Gets the serial of this Printer.  # noqa: E501


        :return: The serial of this Printer.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this Printer.


        :param serial: The serial of this Printer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and serial is None:  # noqa: E501
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def hw_type(self):
        """Gets the hw_type of this Printer.  # noqa: E501


        :return: The hw_type of this Printer.  # noqa: E501
        :rtype: str
        """
        return self._hw_type

    @hw_type.setter
    def hw_type(self, hw_type):
        """Sets the hw_type of this Printer.


        :param hw_type: The hw_type of this Printer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hw_type is None:  # noqa: E501
            raise ValueError("Invalid value for `hw_type`, must not be `None`")  # noqa: E501

        self._hw_type = hw_type

    @property
    def url(self):
        """Gets the url of this Printer.  # noqa: E501


        :return: The url of this Printer.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Printer.


        :param url: The url of this Printer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def updated_at(self):
        """Gets the updated_at of this Printer.  # noqa: E501


        :return: The updated_at of this Printer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Printer.


        :param updated_at: The updated_at of this Printer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this Printer.  # noqa: E501


        :return: The status of this Printer.  # noqa: E501
        :rtype: PrinterStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Printer.


        :param status: The status of this Printer.  # noqa: E501
        :type: PrinterStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def prints(self):
        """Gets the prints of this Printer.  # noqa: E501


        :return: The prints of this Printer.  # noqa: E501
        :rtype: PrinterPrints
        """
        return self._prints

    @prints.setter
    def prints(self, prints):
        """Sets the prints of this Printer.


        :param prints: The prints of this Printer.  # noqa: E501
        :type: PrinterPrints
        """
        if self.local_vars_configuration.client_side_validation and prints is None:  # noqa: E501
            raise ValueError("Invalid value for `prints`, must not be `None`")  # noqa: E501

        self._prints = prints

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
        if not isinstance(other, Printer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Printer):
            return True

        return self.to_dict() != other.to_dict()
