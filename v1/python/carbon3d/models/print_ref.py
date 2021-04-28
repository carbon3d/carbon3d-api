# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintRef(object):
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
        'name': 'str',
        'print_id': 'str',
        'build_uuid': 'str',
        'finished_at': 'datetime',
        'started_at': 'datetime',
        'remaining_sec': 'int'
    }

    attribute_map = {
        'name': 'name',
        'print_id': 'print_id',
        'build_uuid': 'build_uuid',
        'finished_at': 'finished_at',
        'started_at': 'started_at',
        'remaining_sec': 'remaining_sec'
    }

    def __init__(self, name=None, print_id=None, build_uuid=None, finished_at=None, started_at=None, remaining_sec=None, local_vars_configuration=None):  # noqa: E501
        """PrintRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._print_id = None
        self._build_uuid = None
        self._finished_at = None
        self._started_at = None
        self._remaining_sec = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if print_id is not None:
            self.print_id = print_id
        if build_uuid is not None:
            self.build_uuid = build_uuid
        if finished_at is not None:
            self.finished_at = finished_at
        if started_at is not None:
            self.started_at = started_at
        if remaining_sec is not None:
            self.remaining_sec = remaining_sec

    @property
    def name(self):
        """Gets the name of this PrintRef.  # noqa: E501


        :return: The name of this PrintRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrintRef.


        :param name: The name of this PrintRef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def print_id(self):
        """Gets the print_id of this PrintRef.  # noqa: E501


        :return: The print_id of this PrintRef.  # noqa: E501
        :rtype: str
        """
        return self._print_id

    @print_id.setter
    def print_id(self, print_id):
        """Sets the print_id of this PrintRef.


        :param print_id: The print_id of this PrintRef.  # noqa: E501
        :type: str
        """

        self._print_id = print_id

    @property
    def build_uuid(self):
        """Gets the build_uuid of this PrintRef.  # noqa: E501


        :return: The build_uuid of this PrintRef.  # noqa: E501
        :rtype: str
        """
        return self._build_uuid

    @build_uuid.setter
    def build_uuid(self, build_uuid):
        """Sets the build_uuid of this PrintRef.


        :param build_uuid: The build_uuid of this PrintRef.  # noqa: E501
        :type: str
        """

        self._build_uuid = build_uuid

    @property
    def finished_at(self):
        """Gets the finished_at of this PrintRef.  # noqa: E501


        :return: The finished_at of this PrintRef.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this PrintRef.


        :param finished_at: The finished_at of this PrintRef.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def started_at(self):
        """Gets the started_at of this PrintRef.  # noqa: E501


        :return: The started_at of this PrintRef.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this PrintRef.


        :param started_at: The started_at of this PrintRef.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def remaining_sec(self):
        """Gets the remaining_sec of this PrintRef.  # noqa: E501

        Estimated time until expected print completion (in seconds)  # noqa: E501

        :return: The remaining_sec of this PrintRef.  # noqa: E501
        :rtype: int
        """
        return self._remaining_sec

    @remaining_sec.setter
    def remaining_sec(self, remaining_sec):
        """Sets the remaining_sec of this PrintRef.

        Estimated time until expected print completion (in seconds)  # noqa: E501

        :param remaining_sec: The remaining_sec of this PrintRef.  # noqa: E501
        :type: int
        """

        self._remaining_sec = remaining_sec

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
        if not isinstance(other, PrintRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintRef):
            return True

        return self.to_dict() != other.to_dict()
