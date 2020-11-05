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


class PrinterQueueUpdateResponse(object):
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
        'uuids': 'list[str]',
        'code': 'int',
        'message': 'str'
    }

    attribute_map = {
        'uuids': 'uuids',
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, uuids=None, code=None, message=None, local_vars_configuration=None):  # noqa: E501
        """PrinterQueueUpdateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuids = None
        self._code = None
        self._message = None
        self.discriminator = None

        if uuids is not None:
            self.uuids = uuids
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message

    @property
    def uuids(self):
        """Gets the uuids of this PrinterQueueUpdateResponse.  # noqa: E501


        :return: The uuids of this PrinterQueueUpdateResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._uuids

    @uuids.setter
    def uuids(self, uuids):
        """Sets the uuids of this PrinterQueueUpdateResponse.


        :param uuids: The uuids of this PrinterQueueUpdateResponse.  # noqa: E501
        :type: list[str]
        """

        self._uuids = uuids

    @property
    def code(self):
        """Gets the code of this PrinterQueueUpdateResponse.  # noqa: E501

        0 means success, 1 for partial success (e.g: 1 uuid deleted, 1 not found), 2 is for error state (the request did not proceed)  # noqa: E501

        :return: The code of this PrinterQueueUpdateResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PrinterQueueUpdateResponse.

        0 means success, 1 for partial success (e.g: 1 uuid deleted, 1 not found), 2 is for error state (the request did not proceed)  # noqa: E501

        :param code: The code of this PrinterQueueUpdateResponse.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self):
        """Gets the message of this PrinterQueueUpdateResponse.  # noqa: E501


        :return: The message of this PrinterQueueUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PrinterQueueUpdateResponse.


        :param message: The message of this PrinterQueueUpdateResponse.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, PrinterQueueUpdateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrinterQueueUpdateResponse):
            return True

        return self.to_dict() != other.to_dict()
