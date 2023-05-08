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


class JobGroup(object):
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
        'build_sop_uuid': 'str',
        'print_sop_uuid': 'str',
        'group_name': 'str',
        'due_date': 'datetime',
        'split_group': 'bool'
    }

    attribute_map = {
        'build_sop_uuid': 'build_sop_uuid',
        'print_sop_uuid': 'print_sop_uuid',
        'group_name': 'group_name',
        'due_date': 'due_date',
        'split_group': 'split_group'
    }

    def __init__(self, build_sop_uuid=None, print_sop_uuid=None, group_name=None, due_date=None, split_group=True, local_vars_configuration=None):  # noqa: E501
        """JobGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build_sop_uuid = None
        self._print_sop_uuid = None
        self._group_name = None
        self._due_date = None
        self._split_group = None
        self.discriminator = None

        self.build_sop_uuid = build_sop_uuid
        self.print_sop_uuid = print_sop_uuid
        self.group_name = group_name
        self.due_date = due_date
        if split_group is not None:
            self.split_group = split_group

    @property
    def build_sop_uuid(self):
        """Gets the build_sop_uuid of this JobGroup.  # noqa: E501


        :return: The build_sop_uuid of this JobGroup.  # noqa: E501
        :rtype: str
        """
        return self._build_sop_uuid

    @build_sop_uuid.setter
    def build_sop_uuid(self, build_sop_uuid):
        """Sets the build_sop_uuid of this JobGroup.


        :param build_sop_uuid: The build_sop_uuid of this JobGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and build_sop_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `build_sop_uuid`, must not be `None`")  # noqa: E501

        self._build_sop_uuid = build_sop_uuid

    @property
    def print_sop_uuid(self):
        """Gets the print_sop_uuid of this JobGroup.  # noqa: E501


        :return: The print_sop_uuid of this JobGroup.  # noqa: E501
        :rtype: str
        """
        return self._print_sop_uuid

    @print_sop_uuid.setter
    def print_sop_uuid(self, print_sop_uuid):
        """Sets the print_sop_uuid of this JobGroup.


        :param print_sop_uuid: The print_sop_uuid of this JobGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and print_sop_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `print_sop_uuid`, must not be `None`")  # noqa: E501

        self._print_sop_uuid = print_sop_uuid

    @property
    def group_name(self):
        """Gets the group_name of this JobGroup.  # noqa: E501

        Group identifier  # noqa: E501

        :return: The group_name of this JobGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this JobGroup.

        Group identifier  # noqa: E501

        :param group_name: The group_name of this JobGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def due_date(self):
        """Gets the due_date of this JobGroup.  # noqa: E501

        Print due date, used to prioritize Part Jobs  # noqa: E501

        :return: The due_date of this JobGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this JobGroup.

        Print due date, used to prioritize Part Jobs  # noqa: E501

        :param due_date: The due_date of this JobGroup.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and due_date is None:  # noqa: E501
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def split_group(self):
        """Gets the split_group of this JobGroup.  # noqa: E501

        Allows a part_group to be split across multiple builds.  # noqa: E501

        :return: The split_group of this JobGroup.  # noqa: E501
        :rtype: bool
        """
        return self._split_group

    @split_group.setter
    def split_group(self, split_group):
        """Sets the split_group of this JobGroup.

        Allows a part_group to be split across multiple builds.  # noqa: E501

        :param split_group: The split_group of this JobGroup.  # noqa: E501
        :type: bool
        """

        self._split_group = split_group

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
        if not isinstance(other, JobGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobGroup):
            return True

        return self.to_dict() != other.to_dict()
