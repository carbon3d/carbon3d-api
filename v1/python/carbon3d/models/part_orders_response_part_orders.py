# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartOrdersResponsePartOrders(object):
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
        'part_order_number': 'str',
        'printed_parts_count': 'int',
        'due_date': 'datetime',
        'flushed_at': 'datetime',
        'build_uuids': 'list[str]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'status': 'status',
        'part_order_number': 'part_order_number',
        'printed_parts_count': 'printed_parts_count',
        'due_date': 'due_date',
        'flushed_at': 'flushed_at',
        'build_uuids': 'build_uuids'
    }

    def __init__(self, uuid=None, status=None, part_order_number=None, printed_parts_count=None, due_date=None, flushed_at=None, build_uuids=None, local_vars_configuration=None):  # noqa: E501
        """PartOrdersResponsePartOrders - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._status = None
        self._part_order_number = None
        self._printed_parts_count = None
        self._due_date = None
        self._flushed_at = None
        self._build_uuids = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if part_order_number is not None:
            self.part_order_number = part_order_number
        if printed_parts_count is not None:
            self.printed_parts_count = printed_parts_count
        if due_date is not None:
            self.due_date = due_date
        if flushed_at is not None:
            self.flushed_at = flushed_at
        if build_uuids is not None:
            self.build_uuids = build_uuids

    @property
    def uuid(self):
        """Gets the uuid of this PartOrdersResponsePartOrders.  # noqa: E501

        PartOrder UUID  # noqa: E501

        :return: The uuid of this PartOrdersResponsePartOrders.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PartOrdersResponsePartOrders.

        PartOrder UUID  # noqa: E501

        :param uuid: The uuid of this PartOrdersResponsePartOrders.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this PartOrdersResponsePartOrders.  # noqa: E501


        :return: The status of this PartOrdersResponsePartOrders.  # noqa: E501
        :rtype: PartOrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PartOrdersResponsePartOrders.


        :param status: The status of this PartOrdersResponsePartOrders.  # noqa: E501
        :type: PartOrderStatus
        """

        self._status = status

    @property
    def part_order_number(self):
        """Gets the part_order_number of this PartOrdersResponsePartOrders.  # noqa: E501

        Customer-provided part order number  # noqa: E501

        :return: The part_order_number of this PartOrdersResponsePartOrders.  # noqa: E501
        :rtype: str
        """
        return self._part_order_number

    @part_order_number.setter
    def part_order_number(self, part_order_number):
        """Sets the part_order_number of this PartOrdersResponsePartOrders.

        Customer-provided part order number  # noqa: E501

        :param part_order_number: The part_order_number of this PartOrdersResponsePartOrders.  # noqa: E501
        :type: str
        """

        self._part_order_number = part_order_number

    @property
    def printed_parts_count(self):
        """Gets the printed_parts_count of this PartOrdersResponsePartOrders.  # noqa: E501

        Quantity of printed parts in the part order  # noqa: E501

        :return: The printed_parts_count of this PartOrdersResponsePartOrders.  # noqa: E501
        :rtype: int
        """
        return self._printed_parts_count

    @printed_parts_count.setter
    def printed_parts_count(self, printed_parts_count):
        """Sets the printed_parts_count of this PartOrdersResponsePartOrders.

        Quantity of printed parts in the part order  # noqa: E501

        :param printed_parts_count: The printed_parts_count of this PartOrdersResponsePartOrders.  # noqa: E501
        :type: int
        """

        self._printed_parts_count = printed_parts_count

    @property
    def due_date(self):
        """Gets the due_date of this PartOrdersResponsePartOrders.  # noqa: E501

        Print due date, used to prioritize part orders for packing and printing  # noqa: E501

        :return: The due_date of this PartOrdersResponsePartOrders.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PartOrdersResponsePartOrders.

        Print due date, used to prioritize part orders for packing and printing  # noqa: E501

        :param due_date: The due_date of this PartOrdersResponsePartOrders.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def flushed_at(self):
        """Gets the flushed_at of this PartOrdersResponsePartOrders.  # noqa: E501

        When the part order was flushed through the packer, or null if it is not flushed.  # noqa: E501

        :return: The flushed_at of this PartOrdersResponsePartOrders.  # noqa: E501
        :rtype: datetime
        """
        return self._flushed_at

    @flushed_at.setter
    def flushed_at(self, flushed_at):
        """Sets the flushed_at of this PartOrdersResponsePartOrders.

        When the part order was flushed through the packer, or null if it is not flushed.  # noqa: E501

        :param flushed_at: The flushed_at of this PartOrdersResponsePartOrders.  # noqa: E501
        :type: datetime
        """

        self._flushed_at = flushed_at

    @property
    def build_uuids(self):
        """Gets the build_uuids of this PartOrdersResponsePartOrders.  # noqa: E501

        Builds which contain printed parts from this part order.  # noqa: E501

        :return: The build_uuids of this PartOrdersResponsePartOrders.  # noqa: E501
        :rtype: list[str]
        """
        return self._build_uuids

    @build_uuids.setter
    def build_uuids(self, build_uuids):
        """Sets the build_uuids of this PartOrdersResponsePartOrders.

        Builds which contain printed parts from this part order.  # noqa: E501

        :param build_uuids: The build_uuids of this PartOrdersResponsePartOrders.  # noqa: E501
        :type: list[str]
        """

        self._build_uuids = build_uuids

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
        if not isinstance(other, PartOrdersResponsePartOrders):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartOrdersResponsePartOrders):
            return True

        return self.to_dict() != other.to_dict()
