# coding: utf-8

"""
    Carbon API (Draft)

    An API to interact with Carbon's Manufacturing Cloud including 3D model upload, automated order processing and part history.  Getting started ---------------  - [Generate and download an API key](https://carbon3d.print.carbon3d.com/api_keys)   - Your API key and client secret will be downloaded into a secret.json file.  - [Use generated API key to generate a JWT token](/token_generator) from the api key.   - If your API key is revoked, this token will no longer work.  - Authorize with generated token  - Upload mesh files  - Create orders  - Monitor order status   # noqa: E501

    The version of the OpenAPI document: 1.0.0
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
        'files': 'list[BuildFiles]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'parts': 'parts',
        'files': 'files'
    }

    def __init__(self, uuid=None, parts=None, files=None, local_vars_configuration=None):  # noqa: E501
        """Build - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._parts = None
        self._files = None
        self.discriminator = None

        self.uuid = uuid
        self.parts = parts
        if files is not None:
            self.files = files

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
    def files(self):
        """Gets the files of this Build.  # noqa: E501


        :return: The files of this Build.  # noqa: E501
        :rtype: list[BuildFiles]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Build.


        :param files: The files of this Build.  # noqa: E501
        :type: list[BuildFiles]
        """

        self._files = files

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
