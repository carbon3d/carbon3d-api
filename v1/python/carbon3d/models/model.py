# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.7
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class Model(object):
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
        'filename': 'str',
        'application_id': 'int',
        'application_uuid': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'filename': 'filename',
        'application_id': 'application_id',
        'application_uuid': 'application_uuid'
    }

    def __init__(self, uuid=None, filename=None, application_id=None, application_uuid=None, local_vars_configuration=None):  # noqa: E501
        """Model - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._filename = None
        self._application_id = None
        self._application_uuid = None
        self.discriminator = None

        self.uuid = uuid
        self.filename = filename
        if application_id is not None:
            self.application_id = application_id
        if application_uuid is not None:
            self.application_uuid = application_uuid

    @property
    def uuid(self):
        """Gets the uuid of this Model.  # noqa: E501

        Generated unique identifier  # noqa: E501

        :return: The uuid of this Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Model.

        Generated unique identifier  # noqa: E501

        :param uuid: The uuid of this Model.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def filename(self):
        """Gets the filename of this Model.  # noqa: E501

        Filename of the model  # noqa: E501

        :return: The filename of this Model.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Model.

        Filename of the model  # noqa: E501

        :param filename: The filename of this Model.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and filename is None:  # noqa: E501
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def application_id(self):
        """Gets the application_id of this Model.  # noqa: E501

        Application ID  # noqa: E501

        :return: The application_id of this Model.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this Model.

        Application ID  # noqa: E501

        :param application_id: The application_id of this Model.  # noqa: E501
        :type: int
        """

        self._application_id = application_id

    @property
    def application_uuid(self):
        """Gets the application_uuid of this Model.  # noqa: E501

        Application UUID  # noqa: E501

        :return: The application_uuid of this Model.  # noqa: E501
        :rtype: str
        """
        return self._application_uuid

    @application_uuid.setter
    def application_uuid(self, application_uuid):
        """Sets the application_uuid of this Model.

        Application UUID  # noqa: E501

        :param application_uuid: The application_uuid of this Model.  # noqa: E501
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
        if not isinstance(other, Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Model):
            return True

        return self.to_dict() != other.to_dict()
