# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.6
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartOrder(object):
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
        'due_date': 'datetime',
        'printed_parts': 'list[PrintedPartRef]',
        'flushed_at': 'datetime',
        'build_uuids': 'list[str]',
        'build_sop_uuid': 'str',
        'packing_group': 'str',
        'application_uuid': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'status': 'status',
        'part_order_number': 'part_order_number',
        'due_date': 'due_date',
        'printed_parts': 'printed_parts',
        'flushed_at': 'flushed_at',
        'build_uuids': 'build_uuids',
        'build_sop_uuid': 'build_sop_uuid',
        'packing_group': 'packing_group',
        'application_uuid': 'application_uuid'
    }

    def __init__(self, uuid=None, status=None, part_order_number=None, due_date=None, printed_parts=None, flushed_at=None, build_uuids=None, build_sop_uuid=None, packing_group=None, application_uuid=None, local_vars_configuration=None):  # noqa: E501
        """PartOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._status = None
        self._part_order_number = None
        self._due_date = None
        self._printed_parts = None
        self._flushed_at = None
        self._build_uuids = None
        self._build_sop_uuid = None
        self._packing_group = None
        self._application_uuid = None
        self.discriminator = None

        self.uuid = uuid
        if status is not None:
            self.status = status
        if part_order_number is not None:
            self.part_order_number = part_order_number
        self.due_date = due_date
        self.printed_parts = printed_parts
        if flushed_at is not None:
            self.flushed_at = flushed_at
        if build_uuids is not None:
            self.build_uuids = build_uuids
        if build_sop_uuid is not None:
            self.build_sop_uuid = build_sop_uuid
        if packing_group is not None:
            self.packing_group = packing_group
        if application_uuid is not None:
            self.application_uuid = application_uuid

    @property
    def uuid(self):
        """Gets the uuid of this PartOrder.  # noqa: E501

        PartOrder UUID  # noqa: E501

        :return: The uuid of this PartOrder.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PartOrder.

        PartOrder UUID  # noqa: E501

        :param uuid: The uuid of this PartOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this PartOrder.  # noqa: E501


        :return: The status of this PartOrder.  # noqa: E501
        :rtype: PartOrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PartOrder.


        :param status: The status of this PartOrder.  # noqa: E501
        :type: PartOrderStatus
        """

        self._status = status

    @property
    def part_order_number(self):
        """Gets the part_order_number of this PartOrder.  # noqa: E501

        Customer-provided part order number  # noqa: E501

        :return: The part_order_number of this PartOrder.  # noqa: E501
        :rtype: str
        """
        return self._part_order_number

    @part_order_number.setter
    def part_order_number(self, part_order_number):
        """Sets the part_order_number of this PartOrder.

        Customer-provided part order number  # noqa: E501

        :param part_order_number: The part_order_number of this PartOrder.  # noqa: E501
        :type: str
        """

        self._part_order_number = part_order_number

    @property
    def due_date(self):
        """Gets the due_date of this PartOrder.  # noqa: E501

        Print due date, used to prioritize part orders for packing and printing  # noqa: E501

        :return: The due_date of this PartOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PartOrder.

        Print due date, used to prioritize part orders for packing and printing  # noqa: E501

        :param due_date: The due_date of this PartOrder.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and due_date is None:  # noqa: E501
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def printed_parts(self):
        """Gets the printed_parts of this PartOrder.  # noqa: E501

        Parts already printed or to be printed  # noqa: E501

        :return: The printed_parts of this PartOrder.  # noqa: E501
        :rtype: list[PrintedPartRef]
        """
        return self._printed_parts

    @printed_parts.setter
    def printed_parts(self, printed_parts):
        """Sets the printed_parts of this PartOrder.

        Parts already printed or to be printed  # noqa: E501

        :param printed_parts: The printed_parts of this PartOrder.  # noqa: E501
        :type: list[PrintedPartRef]
        """
        if self.local_vars_configuration.client_side_validation and printed_parts is None:  # noqa: E501
            raise ValueError("Invalid value for `printed_parts`, must not be `None`")  # noqa: E501

        self._printed_parts = printed_parts

    @property
    def flushed_at(self):
        """Gets the flushed_at of this PartOrder.  # noqa: E501

        When the part order was flushed, or null if it has not been flushed  # noqa: E501

        :return: The flushed_at of this PartOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._flushed_at

    @flushed_at.setter
    def flushed_at(self, flushed_at):
        """Sets the flushed_at of this PartOrder.

        When the part order was flushed, or null if it has not been flushed  # noqa: E501

        :param flushed_at: The flushed_at of this PartOrder.  # noqa: E501
        :type: datetime
        """

        self._flushed_at = flushed_at

    @property
    def build_uuids(self):
        """Gets the build_uuids of this PartOrder.  # noqa: E501

        Builds which contain printed parts from this part order.  # noqa: E501

        :return: The build_uuids of this PartOrder.  # noqa: E501
        :rtype: list[str]
        """
        return self._build_uuids

    @build_uuids.setter
    def build_uuids(self, build_uuids):
        """Sets the build_uuids of this PartOrder.

        Builds which contain printed parts from this part order.  # noqa: E501

        :param build_uuids: The build_uuids of this PartOrder.  # noqa: E501
        :type: list[str]
        """

        self._build_uuids = build_uuids

    @property
    def build_sop_uuid(self):
        """Gets the build_sop_uuid of this PartOrder.  # noqa: E501

        UUID of Build SOP from print.carbon3d.com/build_sops to use for optional automatic build generation parameters  # noqa: E501

        :return: The build_sop_uuid of this PartOrder.  # noqa: E501
        :rtype: str
        """
        return self._build_sop_uuid

    @build_sop_uuid.setter
    def build_sop_uuid(self, build_sop_uuid):
        """Sets the build_sop_uuid of this PartOrder.

        UUID of Build SOP from print.carbon3d.com/build_sops to use for optional automatic build generation parameters  # noqa: E501

        :param build_sop_uuid: The build_sop_uuid of this PartOrder.  # noqa: E501
        :type: str
        """

        self._build_sop_uuid = build_sop_uuid

    @property
    def packing_group(self):
        """Gets the packing_group of this PartOrder.  # noqa: E501

        Optional (case sensitive) string to identify part orders to be grouped together for packing. Part orders with no specified packing group are grouped together. A maximum of 40 total concurrent packing groups are permitted for 'open' and 'processing' PartOrders.   # noqa: E501

        :return: The packing_group of this PartOrder.  # noqa: E501
        :rtype: str
        """
        return self._packing_group

    @packing_group.setter
    def packing_group(self, packing_group):
        """Sets the packing_group of this PartOrder.

        Optional (case sensitive) string to identify part orders to be grouped together for packing. Part orders with no specified packing group are grouped together. A maximum of 40 total concurrent packing groups are permitted for 'open' and 'processing' PartOrders.   # noqa: E501

        :param packing_group: The packing_group of this PartOrder.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                packing_group is not None and len(packing_group) > 32):
            raise ValueError("Invalid value for `packing_group`, length must be less than or equal to `32`")  # noqa: E501

        self._packing_group = packing_group

    @property
    def application_uuid(self):
        """Gets the application_uuid of this PartOrder.  # noqa: E501

        Application UUID  # noqa: E501

        :return: The application_uuid of this PartOrder.  # noqa: E501
        :rtype: str
        """
        return self._application_uuid

    @application_uuid.setter
    def application_uuid(self, application_uuid):
        """Sets the application_uuid of this PartOrder.

        Application UUID  # noqa: E501

        :param application_uuid: The application_uuid of this PartOrder.  # noqa: E501
        :type: str
        """

        self._application_uuid = application_uuid

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
        if not isinstance(other, PartOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartOrder):
            return True

        return self.to_dict() != other.to_dict()
