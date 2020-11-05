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


class PrintedPartRef(object):
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
        'uuid': 'str',
        'part_uuid': 'str',
        'status': 'PrintedPartStatus'
    }

    attribute_map = {
        'uuid': 'uuid',
        'part_uuid': 'part_uuid',
        'status': 'status'
    }

    def __init__(self, uuid=None, part_uuid=None, status=None, local_vars_configuration=None):  # noqa: E501
        """PrintedPartRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._part_uuid = None
        self._status = None
        self.discriminator = None

        self.uuid = uuid
        self.part_uuid = part_uuid
        self.status = status

    @property
    def uuid(self):
        """Gets the uuid of this PrintedPartRef.  # noqa: E501

        Printed Part UUID  # noqa: E501

        :return: The uuid of this PrintedPartRef.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PrintedPartRef.

        Printed Part UUID  # noqa: E501

        :param uuid: The uuid of this PrintedPartRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def part_uuid(self):
        """Gets the part_uuid of this PrintedPartRef.  # noqa: E501

        Part UUID  # noqa: E501

        :return: The part_uuid of this PrintedPartRef.  # noqa: E501
        :rtype: str
        """
        return self._part_uuid

    @part_uuid.setter
    def part_uuid(self, part_uuid):
        """Sets the part_uuid of this PrintedPartRef.

        Part UUID  # noqa: E501

        :param part_uuid: The part_uuid of this PrintedPartRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and part_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `part_uuid`, must not be `None`")  # noqa: E501

        self._part_uuid = part_uuid

    @property
    def status(self):
        """Gets the status of this PrintedPartRef.  # noqa: E501


        :return: The status of this PrintedPartRef.  # noqa: E501
        :rtype: PrintedPartStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PrintedPartRef.


        :param status: The status of this PrintedPartRef.  # noqa: E501
        :type: PrintedPartStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, PrintedPartRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintedPartRef):
            return True

        return self.to_dict() != other.to_dict()
