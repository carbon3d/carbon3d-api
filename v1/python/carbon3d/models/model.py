# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.12
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
        'external_id': 'str',
        'application_uuid': 'str',
        'description': 'str',
        'file_size_bytes': 'int',
        'updated_at': 'str',
        'created_at': 'str',
        'created_by': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'filename': 'filename',
        'external_id': 'external_id',
        'application_uuid': 'application_uuid',
        'description': 'description',
        'file_size_bytes': 'file_size_bytes',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'created_by': 'created_by'
    }

    def __init__(self, uuid=None, filename=None, external_id=None, application_uuid=None, description=None, file_size_bytes=None, updated_at=None, created_at=None, created_by=None, local_vars_configuration=None):  # noqa: E501
        """Model - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._filename = None
        self._external_id = None
        self._application_uuid = None
        self._description = None
        self._file_size_bytes = None
        self._updated_at = None
        self._created_at = None
        self._created_by = None
        self.discriminator = None

        self.uuid = uuid
        self.filename = filename
        if external_id is not None:
            self.external_id = external_id
        if application_uuid is not None:
            self.application_uuid = application_uuid
        if description is not None:
            self.description = description
        if file_size_bytes is not None:
            self.file_size_bytes = file_size_bytes
        if updated_at is not None:
            self.updated_at = updated_at
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by

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
    def external_id(self):
        """Gets the external_id of this Model.  # noqa: E501

        External id provided by user  # noqa: E501

        :return: The external_id of this Model.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Model.

        External id provided by user  # noqa: E501

        :param external_id: The external_id of this Model.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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

    @property
    def description(self):
        """Gets the description of this Model.  # noqa: E501

        Description of the model  # noqa: E501

        :return: The description of this Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Model.

        Description of the model  # noqa: E501

        :param description: The description of this Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_size_bytes(self):
        """Gets the file_size_bytes of this Model.  # noqa: E501

        Model file size in bytes  # noqa: E501

        :return: The file_size_bytes of this Model.  # noqa: E501
        :rtype: int
        """
        return self._file_size_bytes

    @file_size_bytes.setter
    def file_size_bytes(self, file_size_bytes):
        """Sets the file_size_bytes of this Model.

        Model file size in bytes  # noqa: E501

        :param file_size_bytes: The file_size_bytes of this Model.  # noqa: E501
        :type: int
        """

        self._file_size_bytes = file_size_bytes

    @property
    def updated_at(self):
        """Gets the updated_at of this Model.  # noqa: E501

        Timestamp at which the model was last updated  # noqa: E501

        :return: The updated_at of this Model.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Model.

        Timestamp at which the model was last updated  # noqa: E501

        :param updated_at: The updated_at of this Model.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this Model.  # noqa: E501

        Timestamp at which the model was created  # noqa: E501

        :return: The created_at of this Model.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Model.

        Timestamp at which the model was created  # noqa: E501

        :param created_at: The created_at of this Model.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Model.  # noqa: E501

        Name of the model creator  # noqa: E501

        :return: The created_by of this Model.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Model.

        Name of the model creator  # noqa: E501

        :param created_by: The created_by of this Model.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

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
