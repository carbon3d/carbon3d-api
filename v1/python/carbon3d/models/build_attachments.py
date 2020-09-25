# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class BuildAttachments(object):
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
        'filename': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'filename': 'filename',
        'uuid': 'uuid'
    }

    def __init__(self, filename=None, uuid=None, local_vars_configuration=None):  # noqa: E501
        """BuildAttachments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._filename = None
        self._uuid = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if uuid is not None:
            self.uuid = uuid

    @property
    def filename(self):
        """Gets the filename of this BuildAttachments.  # noqa: E501

        Name of the file attachment  # noqa: E501

        :return: The filename of this BuildAttachments.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BuildAttachments.

        Name of the file attachment  # noqa: E501

        :param filename: The filename of this BuildAttachments.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def uuid(self):
        """Gets the uuid of this BuildAttachments.  # noqa: E501

        uuid of the file, download it with /attachments/:uuid  # noqa: E501

        :return: The uuid of this BuildAttachments.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this BuildAttachments.

        uuid of the file, download it with /attachments/:uuid  # noqa: E501

        :param uuid: The uuid of this BuildAttachments.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, BuildAttachments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuildAttachments):
            return True

        return self.to_dict() != other.to_dict()
