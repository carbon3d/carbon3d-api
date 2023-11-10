# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.16
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartOrderRequest(object):
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
        'part_order_number': 'str',
        'parts': 'list[PartOrderRequestParts]',
        'due_date': 'datetime',
        'flush': 'bool',
        'build_sop_uuid': 'str',
        'uuid': 'str',
        'packing_group': 'str'
    }

    attribute_map = {
        'part_order_number': 'part_order_number',
        'parts': 'parts',
        'due_date': 'due_date',
        'flush': 'flush',
        'build_sop_uuid': 'build_sop_uuid',
        'uuid': 'uuid',
        'packing_group': 'packing_group'
    }

    def __init__(self, part_order_number=None, parts=None, due_date=None, flush=None, build_sop_uuid=None, uuid=None, packing_group=None, local_vars_configuration=None):  # noqa: E501
        """PartOrderRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._part_order_number = None
        self._parts = None
        self._due_date = None
        self._flush = None
        self._build_sop_uuid = None
        self._uuid = None
        self._packing_group = None
        self.discriminator = None

        self.part_order_number = part_order_number
        self.parts = parts
        self.due_date = due_date
        if flush is not None:
            self.flush = flush
        if build_sop_uuid is not None:
            self.build_sop_uuid = build_sop_uuid
        if uuid is not None:
            self.uuid = uuid
        if packing_group is not None:
            self.packing_group = packing_group

    @property
    def part_order_number(self):
        """Gets the part_order_number of this PartOrderRequest.  # noqa: E501

        Customer-provided part order number  # noqa: E501

        :return: The part_order_number of this PartOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._part_order_number

    @part_order_number.setter
    def part_order_number(self, part_order_number):
        """Sets the part_order_number of this PartOrderRequest.

        Customer-provided part order number  # noqa: E501

        :param part_order_number: The part_order_number of this PartOrderRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and part_order_number is None:  # noqa: E501
            raise ValueError("Invalid value for `part_order_number`, must not be `None`")  # noqa: E501

        self._part_order_number = part_order_number

    @property
    def parts(self):
        """Gets the parts of this PartOrderRequest.  # noqa: E501

        Parts to be printed  # noqa: E501

        :return: The parts of this PartOrderRequest.  # noqa: E501
        :rtype: list[PartOrderRequestParts]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this PartOrderRequest.

        Parts to be printed  # noqa: E501

        :param parts: The parts of this PartOrderRequest.  # noqa: E501
        :type: list[PartOrderRequestParts]
        """
        if self.local_vars_configuration.client_side_validation and parts is None:  # noqa: E501
            raise ValueError("Invalid value for `parts`, must not be `None`")  # noqa: E501

        self._parts = parts

    @property
    def due_date(self):
        """Gets the due_date of this PartOrderRequest.  # noqa: E501

        Print due date, used to prioritize part orders for packing and printing  # noqa: E501

        :return: The due_date of this PartOrderRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PartOrderRequest.

        Print due date, used to prioritize part orders for packing and printing  # noqa: E501

        :param due_date: The due_date of this PartOrderRequest.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and due_date is None:  # noqa: E501
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def flush(self):
        """Gets the flush of this PartOrderRequest.  # noqa: E501

        Push parts in a part order through the auto-packer.  # noqa: E501

        :return: The flush of this PartOrderRequest.  # noqa: E501
        :rtype: bool
        """
        return self._flush

    @flush.setter
    def flush(self, flush):
        """Sets the flush of this PartOrderRequest.

        Push parts in a part order through the auto-packer.  # noqa: E501

        :param flush: The flush of this PartOrderRequest.  # noqa: E501
        :type: bool
        """

        self._flush = flush

    @property
    def build_sop_uuid(self):
        """Gets the build_sop_uuid of this PartOrderRequest.  # noqa: E501

        UUID of Build SOP from print.carbon3d.com/build_sops to use for optional automatic build generation parameters  # noqa: E501

        :return: The build_sop_uuid of this PartOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._build_sop_uuid

    @build_sop_uuid.setter
    def build_sop_uuid(self, build_sop_uuid):
        """Sets the build_sop_uuid of this PartOrderRequest.

        UUID of Build SOP from print.carbon3d.com/build_sops to use for optional automatic build generation parameters  # noqa: E501

        :param build_sop_uuid: The build_sop_uuid of this PartOrderRequest.  # noqa: E501
        :type: str
        """

        self._build_sop_uuid = build_sop_uuid

    @property
    def uuid(self):
        """Gets the uuid of this PartOrderRequest.  # noqa: E501

        UUID of the part order to create. If not provided, a UUID will be generated.  # noqa: E501

        :return: The uuid of this PartOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PartOrderRequest.

        UUID of the part order to create. If not provided, a UUID will be generated.  # noqa: E501

        :param uuid: The uuid of this PartOrderRequest.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def packing_group(self):
        """Gets the packing_group of this PartOrderRequest.  # noqa: E501

        Optional (case sensitive) string to identify part orders to be grouped together for packing. Part orders with no specified packing group are grouped together. A maximum of 40 total concurrent packing groups are permitted for 'open' and 'processing' PartOrders.   # noqa: E501

        :return: The packing_group of this PartOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._packing_group

    @packing_group.setter
    def packing_group(self, packing_group):
        """Sets the packing_group of this PartOrderRequest.

        Optional (case sensitive) string to identify part orders to be grouped together for packing. Part orders with no specified packing group are grouped together. A maximum of 40 total concurrent packing groups are permitted for 'open' and 'processing' PartOrders.   # noqa: E501

        :param packing_group: The packing_group of this PartOrderRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                packing_group is not None and len(packing_group) > 32):
            raise ValueError("Invalid value for `packing_group`, length must be less than or equal to `32`")  # noqa: E501

        self._packing_group = packing_group

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
        if not isinstance(other, PartOrderRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartOrderRequest):
            return True

        return self.to_dict() != other.to_dict()
