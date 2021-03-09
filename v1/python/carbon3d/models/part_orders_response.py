# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.9
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartOrdersResponse(object):
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
        'limit': 'int',
        'next_cursor': 'str',
        'total_count': 'int',
        'part_orders': 'list[PartOrdersResponsePartOrders]'
    }

    attribute_map = {
        'limit': 'limit',
        'next_cursor': 'next_cursor',
        'total_count': 'total_count',
        'part_orders': 'part_orders'
    }

    def __init__(self, limit=None, next_cursor=None, total_count=None, part_orders=None, local_vars_configuration=None):  # noqa: E501
        """PartOrdersResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._limit = None
        self._next_cursor = None
        self._total_count = None
        self._part_orders = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if next_cursor is not None:
            self.next_cursor = next_cursor
        if total_count is not None:
            self.total_count = total_count
        if part_orders is not None:
            self.part_orders = part_orders

    @property
    def limit(self):
        """Gets the limit of this PartOrdersResponse.  # noqa: E501

        Response limit  # noqa: E501

        :return: The limit of this PartOrdersResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PartOrdersResponse.

        Response limit  # noqa: E501

        :param limit: The limit of this PartOrdersResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next_cursor(self):
        """Gets the next_cursor of this PartOrdersResponse.  # noqa: E501

        The cursor that should used to retrieve the next page of results  # noqa: E501

        :return: The next_cursor of this PartOrdersResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, next_cursor):
        """Sets the next_cursor of this PartOrdersResponse.

        The cursor that should used to retrieve the next page of results  # noqa: E501

        :param next_cursor: The next_cursor of this PartOrdersResponse.  # noqa: E501
        :type: str
        """

        self._next_cursor = next_cursor

    @property
    def total_count(self):
        """Gets the total_count of this PartOrdersResponse.  # noqa: E501

        Total number of part orders matching the query  # noqa: E501

        :return: The total_count of this PartOrdersResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PartOrdersResponse.

        Total number of part orders matching the query  # noqa: E501

        :param total_count: The total_count of this PartOrdersResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def part_orders(self):
        """Gets the part_orders of this PartOrdersResponse.  # noqa: E501

        Part Orders  # noqa: E501

        :return: The part_orders of this PartOrdersResponse.  # noqa: E501
        :rtype: list[PartOrdersResponsePartOrders]
        """
        return self._part_orders

    @part_orders.setter
    def part_orders(self, part_orders):
        """Sets the part_orders of this PartOrdersResponse.

        Part Orders  # noqa: E501

        :param part_orders: The part_orders of this PartOrdersResponse.  # noqa: E501
        :type: list[PartOrdersResponsePartOrders]
        """

        self._part_orders = part_orders

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
        if not isinstance(other, PartOrdersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartOrdersResponse):
            return True

        return self.to_dict() != other.to_dict()
