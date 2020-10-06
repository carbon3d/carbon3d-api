# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class Build(object):
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
        'parts': 'list[Part]',
        'attachments': 'list[BuildAttachments]',
        'name': 'str',
        'revision': 'str',
        'status': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'parts': 'parts',
        'attachments': 'attachments',
        'name': 'name',
        'revision': 'revision',
        'status': 'status'
    }

    def __init__(self, uuid=None, parts=None, attachments=None, name=None, revision=None, status=None, local_vars_configuration=None):  # noqa: E501
        """Build - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._parts = None
        self._attachments = None
        self._name = None
        self._revision = None
        self._status = None
        self.discriminator = None

        self.uuid = uuid
        self.parts = parts
        if attachments is not None:
            self.attachments = attachments
        if name is not None:
            self.name = name
        if revision is not None:
            self.revision = revision
        if status is not None:
            self.status = status

    @property
    def uuid(self):
        """Gets the uuid of this Build.  # noqa: E501


        :return: The uuid of this Build.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Build.


        :param uuid: The uuid of this Build.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def parts(self):
        """Gets the parts of this Build.  # noqa: E501


        :return: The parts of this Build.  # noqa: E501
        :rtype: list[Part]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this Build.


        :param parts: The parts of this Build.  # noqa: E501
        :type: list[Part]
        """
        if self.local_vars_configuration.client_side_validation and parts is None:  # noqa: E501
            raise ValueError("Invalid value for `parts`, must not be `None`")  # noqa: E501

        self._parts = parts

    @property
    def attachments(self):
        """Gets the attachments of this Build.  # noqa: E501


        :return: The attachments of this Build.  # noqa: E501
        :rtype: list[BuildAttachments]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Build.


        :param attachments: The attachments of this Build.  # noqa: E501
        :type: list[BuildAttachments]
        """

        self._attachments = attachments

    @property
    def name(self):
        """Gets the name of this Build.  # noqa: E501


        :return: The name of this Build.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Build.


        :param name: The name of this Build.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def revision(self):
        """Gets the revision of this Build.  # noqa: E501


        :return: The revision of this Build.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Build.


        :param revision: The revision of this Build.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def status(self):
        """Gets the status of this Build.  # noqa: E501


        :return: The status of this Build.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Build.


        :param status: The status of this Build.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unreleased", "Validation", "Released", "Obsolete"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

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
        if not isinstance(other, Build):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Build):
            return True

        return self.to_dict() != other.to_dict()
