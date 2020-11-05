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


class PrinterQueueMoveRequest(object):
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
        'action_type': 'str',
        'printer_serial': 'str',
        'index': 'int',
        'print_uuids': 'list[str]'
    }

    attribute_map = {
        'action_type': 'action_type',
        'printer_serial': 'printer_serial',
        'index': 'index',
        'print_uuids': 'print_uuids'
    }

    def __init__(self, action_type=None, printer_serial=None, index=None, print_uuids=None, local_vars_configuration=None):  # noqa: E501
        """PrinterQueueMoveRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action_type = None
        self._printer_serial = None
        self._index = None
        self._print_uuids = None
        self.discriminator = None

        self.action_type = action_type
        self.printer_serial = printer_serial
        self.index = index
        self.print_uuids = print_uuids

    @property
    def action_type(self):
        """Gets the action_type of this PrinterQueueMoveRequest.  # noqa: E501


        :return: The action_type of this PrinterQueueMoveRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this PrinterQueueMoveRequest.


        :param action_type: The action_type of this PrinterQueueMoveRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action_type is None:  # noqa: E501
            raise ValueError("Invalid value for `action_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PrinterQueueMoveRequest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def printer_serial(self):
        """Gets the printer_serial of this PrinterQueueMoveRequest.  # noqa: E501

        Target printer for the move operation  # noqa: E501

        :return: The printer_serial of this PrinterQueueMoveRequest.  # noqa: E501
        :rtype: str
        """
        return self._printer_serial

    @printer_serial.setter
    def printer_serial(self, printer_serial):
        """Sets the printer_serial of this PrinterQueueMoveRequest.

        Target printer for the move operation  # noqa: E501

        :param printer_serial: The printer_serial of this PrinterQueueMoveRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and printer_serial is None:  # noqa: E501
            raise ValueError("Invalid value for `printer_serial`, must not be `None`")  # noqa: E501

        self._printer_serial = printer_serial

    @property
    def index(self):
        """Gets the index of this PrinterQueueMoveRequest.  # noqa: E501

        Target index for given uuids on target printer queue. If given 0, places the first uuid at the top of the queue, followed by other param uuids and the rest of the existing queue. If index provided is higher than the max index of the queue, add uuid(s) to the end. Use '-1' to express 'end of queue'.  # noqa: E501

        :return: The index of this PrinterQueueMoveRequest.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this PrinterQueueMoveRequest.

        Target index for given uuids on target printer queue. If given 0, places the first uuid at the top of the queue, followed by other param uuids and the rest of the existing queue. If index provided is higher than the max index of the queue, add uuid(s) to the end. Use '-1' to express 'end of queue'.  # noqa: E501

        :param index: The index of this PrinterQueueMoveRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def print_uuids(self):
        """Gets the print_uuids of this PrinterQueueMoveRequest.  # noqa: E501


        :return: The print_uuids of this PrinterQueueMoveRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._print_uuids

    @print_uuids.setter
    def print_uuids(self, print_uuids):
        """Sets the print_uuids of this PrinterQueueMoveRequest.


        :param print_uuids: The print_uuids of this PrinterQueueMoveRequest.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and print_uuids is None:  # noqa: E501
            raise ValueError("Invalid value for `print_uuids`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, PrinterQueueMoveRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrinterQueueMoveRequest):
            return True

        return self.to_dict() != other.to_dict()
