# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartGenealogyPrintInfo(object):
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
        'queued_at': 'datetime',
        'print_uuid': 'str',
        'printer_serial': 'str',
        'platform_serial': 'str',
        'cassette_serial': 'str',
        'resin_lot_number': 'str',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'error': 'str'
    }

    attribute_map = {
        'queued_at': 'queued_at',
        'print_uuid': 'print_uuid',
        'printer_serial': 'printer_serial',
        'platform_serial': 'platform_serial',
        'cassette_serial': 'cassette_serial',
        'resin_lot_number': 'resin_lot_number',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'error': 'error'
    }

    def __init__(self, queued_at=None, print_uuid=None, printer_serial=None, platform_serial=None, cassette_serial=None, resin_lot_number=None, started_at=None, finished_at=None, error=None, local_vars_configuration=None):  # noqa: E501
        """PartGenealogyPrintInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._queued_at = None
        self._print_uuid = None
        self._printer_serial = None
        self._platform_serial = None
        self._cassette_serial = None
        self._resin_lot_number = None
        self._started_at = None
        self._finished_at = None
        self._error = None
        self.discriminator = None

        if queued_at is not None:
            self.queued_at = queued_at
        if print_uuid is not None:
            self.print_uuid = print_uuid
        if printer_serial is not None:
            self.printer_serial = printer_serial
        if platform_serial is not None:
            self.platform_serial = platform_serial
        if cassette_serial is not None:
            self.cassette_serial = cassette_serial
        if resin_lot_number is not None:
            self.resin_lot_number = resin_lot_number
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if error is not None:
            self.error = error

    @property
    def queued_at(self):
        """Gets the queued_at of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The queued_at of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        """Sets the queued_at of this PartGenealogyPrintInfo.


        :param queued_at: The queued_at of this PartGenealogyPrintInfo.  # noqa: E501
        :type: datetime
        """

        self._queued_at = queued_at

    @property
    def print_uuid(self):
        """Gets the print_uuid of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The print_uuid of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: str
        """
        return self._print_uuid

    @print_uuid.setter
    def print_uuid(self, print_uuid):
        """Sets the print_uuid of this PartGenealogyPrintInfo.


        :param print_uuid: The print_uuid of this PartGenealogyPrintInfo.  # noqa: E501
        :type: str
        """

        self._print_uuid = print_uuid

    @property
    def printer_serial(self):
        """Gets the printer_serial of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The printer_serial of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: str
        """
        return self._printer_serial

    @printer_serial.setter
    def printer_serial(self, printer_serial):
        """Sets the printer_serial of this PartGenealogyPrintInfo.


        :param printer_serial: The printer_serial of this PartGenealogyPrintInfo.  # noqa: E501
        :type: str
        """

        self._printer_serial = printer_serial

    @property
    def platform_serial(self):
        """Gets the platform_serial of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The platform_serial of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: str
        """
        return self._platform_serial

    @platform_serial.setter
    def platform_serial(self, platform_serial):
        """Sets the platform_serial of this PartGenealogyPrintInfo.


        :param platform_serial: The platform_serial of this PartGenealogyPrintInfo.  # noqa: E501
        :type: str
        """

        self._platform_serial = platform_serial

    @property
    def cassette_serial(self):
        """Gets the cassette_serial of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The cassette_serial of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: str
        """
        return self._cassette_serial

    @cassette_serial.setter
    def cassette_serial(self, cassette_serial):
        """Sets the cassette_serial of this PartGenealogyPrintInfo.


        :param cassette_serial: The cassette_serial of this PartGenealogyPrintInfo.  # noqa: E501
        :type: str
        """

        self._cassette_serial = cassette_serial

    @property
    def resin_lot_number(self):
        """Gets the resin_lot_number of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The resin_lot_number of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: str
        """
        return self._resin_lot_number

    @resin_lot_number.setter
    def resin_lot_number(self, resin_lot_number):
        """Sets the resin_lot_number of this PartGenealogyPrintInfo.


        :param resin_lot_number: The resin_lot_number of this PartGenealogyPrintInfo.  # noqa: E501
        :type: str
        """

        self._resin_lot_number = resin_lot_number

    @property
    def started_at(self):
        """Gets the started_at of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The started_at of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this PartGenealogyPrintInfo.


        :param started_at: The started_at of this PartGenealogyPrintInfo.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The finished_at of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this PartGenealogyPrintInfo.


        :param finished_at: The finished_at of this PartGenealogyPrintInfo.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def error(self):
        """Gets the error of this PartGenealogyPrintInfo.  # noqa: E501


        :return: The error of this PartGenealogyPrintInfo.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PartGenealogyPrintInfo.


        :param error: The error of this PartGenealogyPrintInfo.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if not isinstance(other, PartGenealogyPrintInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartGenealogyPrintInfo):
            return True

        return self.to_dict() != other.to_dict()
