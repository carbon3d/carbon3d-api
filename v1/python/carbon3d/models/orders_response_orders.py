# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class OrdersResponseOrders(object):
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
        'status': 'PartOrderStatus',
        'order_number': 'str',
        'printed_parts_count': 'int',
        'due_date': 'datetime',
        'route_to': 'list[str]',
        'flushed_at': 'datetime'
    }

    attribute_map = {
        'uuid': 'uuid',
        'status': 'status',
        'order_number': 'order_number',
        'printed_parts_count': 'printed_parts_count',
        'due_date': 'due_date',
        'route_to': 'route_to',
        'flushed_at': 'flushed_at'
    }

    def __init__(self, uuid=None, status=None, order_number=None, printed_parts_count=None, due_date=None, route_to=None, flushed_at=None, local_vars_configuration=None):  # noqa: E501
        """OrdersResponseOrders - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._status = None
        self._order_number = None
        self._printed_parts_count = None
        self._due_date = None
        self._route_to = None
        self._flushed_at = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if order_number is not None:
            self.order_number = order_number
        if printed_parts_count is not None:
            self.printed_parts_count = printed_parts_count
        if due_date is not None:
            self.due_date = due_date
        if route_to is not None:
            self.route_to = route_to
        if flushed_at is not None:
            self.flushed_at = flushed_at

    @property
    def uuid(self):
        """Gets the uuid of this OrdersResponseOrders.  # noqa: E501

        Order UUID  # noqa: E501

        :return: The uuid of this OrdersResponseOrders.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this OrdersResponseOrders.

        Order UUID  # noqa: E501

        :param uuid: The uuid of this OrdersResponseOrders.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this OrdersResponseOrders.  # noqa: E501


        :return: The status of this OrdersResponseOrders.  # noqa: E501
        :rtype: PartOrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrdersResponseOrders.


        :param status: The status of this OrdersResponseOrders.  # noqa: E501
        :type: PartOrderStatus
        """

        self._status = status

    @property
    def order_number(self):
        """Gets the order_number of this OrdersResponseOrders.  # noqa: E501

        Customer-provided order number  # noqa: E501

        :return: The order_number of this OrdersResponseOrders.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this OrdersResponseOrders.

        Customer-provided order number  # noqa: E501

        :param order_number: The order_number of this OrdersResponseOrders.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def printed_parts_count(self):
        """Gets the printed_parts_count of this OrdersResponseOrders.  # noqa: E501

        Quantity of printed parts in the order  # noqa: E501

        :return: The printed_parts_count of this OrdersResponseOrders.  # noqa: E501
        :rtype: int
        """
        return self._printed_parts_count

    @printed_parts_count.setter
    def printed_parts_count(self, printed_parts_count):
        """Sets the printed_parts_count of this OrdersResponseOrders.

        Quantity of printed parts in the order  # noqa: E501

        :param printed_parts_count: The printed_parts_count of this OrdersResponseOrders.  # noqa: E501
        :type: int
        """

        self._printed_parts_count = printed_parts_count

    @property
    def due_date(self):
        """Gets the due_date of this OrdersResponseOrders.  # noqa: E501

        Print due date, used to prioritize orders for packing and printing  # noqa: E501

        :return: The due_date of this OrdersResponseOrders.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this OrdersResponseOrders.

        Print due date, used to prioritize orders for packing and printing  # noqa: E501

        :param due_date: The due_date of this OrdersResponseOrders.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def route_to(self):
        """Gets the route_to of this OrdersResponseOrders.  # noqa: E501

        Section to route this order to (e.g. production, a rework line)  # noqa: E501

        :return: The route_to of this OrdersResponseOrders.  # noqa: E501
        :rtype: list[str]
        """
        return self._route_to

    @route_to.setter
    def route_to(self, route_to):
        """Sets the route_to of this OrdersResponseOrders.

        Section to route this order to (e.g. production, a rework line)  # noqa: E501

        :param route_to: The route_to of this OrdersResponseOrders.  # noqa: E501
        :type: list[str]
        """

        self._route_to = route_to

    @property
    def flushed_at(self):
        """Gets the flushed_at of this OrdersResponseOrders.  # noqa: E501

        When the order was flushed through the packer, or null if it is not flushed.  # noqa: E501

        :return: The flushed_at of this OrdersResponseOrders.  # noqa: E501
        :rtype: datetime
        """
        return self._flushed_at

    @flushed_at.setter
    def flushed_at(self, flushed_at):
        """Sets the flushed_at of this OrdersResponseOrders.

        When the order was flushed through the packer, or null if it is not flushed.  # noqa: E501

        :param flushed_at: The flushed_at of this OrdersResponseOrders.  # noqa: E501
        :type: datetime
        """

        self._flushed_at = flushed_at

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
        if not isinstance(other, OrdersResponseOrders):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrdersResponseOrders):
            return True

        return self.to_dict() != other.to_dict()
