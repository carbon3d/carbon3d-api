# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.3
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrinterQueueDeleteRequest(object):
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
        'print_uuids': 'list[str]'
    }

    attribute_map = {
        'action_type': 'action_type',
        'print_uuids': 'print_uuids'
    }

    def __init__(self, action_type=None, print_uuids=None, local_vars_configuration=None):  # noqa: E501
        """PrinterQueueDeleteRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action_type = None
        self._print_uuids = None
        self.discriminator = None

        self.action_type = action_type
        self.print_uuids = print_uuids

    @property
    def action_type(self):
        """Gets the action_type of this PrinterQueueDeleteRequest.  # noqa: E501


        :return: The action_type of this PrinterQueueDeleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this PrinterQueueDeleteRequest.


        :param action_type: The action_type of this PrinterQueueDeleteRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action_type is None:  # noqa: E501
            raise ValueError("Invalid value for `action_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PrinterQueueDeleteRequest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def print_uuids(self):
        """Gets the print_uuids of this PrinterQueueDeleteRequest.  # noqa: E501


        :return: The print_uuids of this PrinterQueueDeleteRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._print_uuids

    @print_uuids.setter
    def print_uuids(self, print_uuids):
        """Sets the print_uuids of this PrinterQueueDeleteRequest.


        :param print_uuids: The print_uuids of this PrinterQueueDeleteRequest.  # noqa: E501
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
        if not isinstance(other, PrinterQueueDeleteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrinterQueueDeleteRequest):
            return True

        return self.to_dict() != other.to_dict()
