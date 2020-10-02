# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.5
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintOrigin(object):
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
        'cassette_serial': 'str',
        'cassette_nfc_uid': 'str',
        'platform_serial': 'str',
        'platform_nfc_uid': 'str',
        'printer_serial': 'str',
        'software_version': 'str'
    }

    attribute_map = {
        'cassette_serial': 'cassette_serial',
        'cassette_nfc_uid': 'cassette_nfc_uid',
        'platform_serial': 'platform_serial',
        'platform_nfc_uid': 'platform_nfc_uid',
        'printer_serial': 'printer_serial',
        'software_version': 'software_version'
    }

    def __init__(self, cassette_serial=None, cassette_nfc_uid=None, platform_serial=None, platform_nfc_uid=None, printer_serial=None, software_version=None, local_vars_configuration=None):  # noqa: E501
        """PrintOrigin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cassette_serial = None
        self._cassette_nfc_uid = None
        self._platform_serial = None
        self._platform_nfc_uid = None
        self._printer_serial = None
        self._software_version = None
        self.discriminator = None

        if cassette_serial is not None:
            self.cassette_serial = cassette_serial
        if cassette_nfc_uid is not None:
            self.cassette_nfc_uid = cassette_nfc_uid
        if platform_serial is not None:
            self.platform_serial = platform_serial
        if platform_nfc_uid is not None:
            self.platform_nfc_uid = platform_nfc_uid
        if printer_serial is not None:
            self.printer_serial = printer_serial
        if software_version is not None:
            self.software_version = software_version

    @property
    def cassette_serial(self):
        """Gets the cassette_serial of this PrintOrigin.  # noqa: E501


        :return: The cassette_serial of this PrintOrigin.  # noqa: E501
        :rtype: str
        """
        return self._cassette_serial

    @cassette_serial.setter
    def cassette_serial(self, cassette_serial):
        """Sets the cassette_serial of this PrintOrigin.


        :param cassette_serial: The cassette_serial of this PrintOrigin.  # noqa: E501
        :type: str
        """

        self._cassette_serial = cassette_serial

    @property
    def cassette_nfc_uid(self):
        """Gets the cassette_nfc_uid of this PrintOrigin.  # noqa: E501


        :return: The cassette_nfc_uid of this PrintOrigin.  # noqa: E501
        :rtype: str
        """
        return self._cassette_nfc_uid

    @cassette_nfc_uid.setter
    def cassette_nfc_uid(self, cassette_nfc_uid):
        """Sets the cassette_nfc_uid of this PrintOrigin.


        :param cassette_nfc_uid: The cassette_nfc_uid of this PrintOrigin.  # noqa: E501
        :type: str
        """

        self._cassette_nfc_uid = cassette_nfc_uid

    @property
    def platform_serial(self):
        """Gets the platform_serial of this PrintOrigin.  # noqa: E501


        :return: The platform_serial of this PrintOrigin.  # noqa: E501
        :rtype: str
        """
        return self._platform_serial

    @platform_serial.setter
    def platform_serial(self, platform_serial):
        """Sets the platform_serial of this PrintOrigin.


        :param platform_serial: The platform_serial of this PrintOrigin.  # noqa: E501
        :type: str
        """

        self._platform_serial = platform_serial

    @property
    def platform_nfc_uid(self):
        """Gets the platform_nfc_uid of this PrintOrigin.  # noqa: E501


        :return: The platform_nfc_uid of this PrintOrigin.  # noqa: E501
        :rtype: str
        """
        return self._platform_nfc_uid

    @platform_nfc_uid.setter
    def platform_nfc_uid(self, platform_nfc_uid):
        """Sets the platform_nfc_uid of this PrintOrigin.


        :param platform_nfc_uid: The platform_nfc_uid of this PrintOrigin.  # noqa: E501
        :type: str
        """

        self._platform_nfc_uid = platform_nfc_uid

    @property
    def printer_serial(self):
        """Gets the printer_serial of this PrintOrigin.  # noqa: E501


        :return: The printer_serial of this PrintOrigin.  # noqa: E501
        :rtype: str
        """
        return self._printer_serial

    @printer_serial.setter
    def printer_serial(self, printer_serial):
        """Sets the printer_serial of this PrintOrigin.


        :param printer_serial: The printer_serial of this PrintOrigin.  # noqa: E501
        :type: str
        """

        self._printer_serial = printer_serial

    @property
    def software_version(self):
        """Gets the software_version of this PrintOrigin.  # noqa: E501


        :return: The software_version of this PrintOrigin.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this PrintOrigin.


        :param software_version: The software_version of this PrintOrigin.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

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
        if not isinstance(other, PrintOrigin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintOrigin):
            return True

        return self.to_dict() != other.to_dict()
