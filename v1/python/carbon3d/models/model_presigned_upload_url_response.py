# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.10
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class ModelPresignedUploadUrlResponse(object):
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
        'presigned_url': 'str',
        'model_uuid': 'str'
    }

    attribute_map = {
        'presigned_url': 'presigned_url',
        'model_uuid': 'model_uuid'
    }

    def __init__(self, presigned_url=None, model_uuid=None, local_vars_configuration=None):  # noqa: E501
        """ModelPresignedUploadUrlResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._presigned_url = None
        self._model_uuid = None
        self.discriminator = None

        self.presigned_url = presigned_url
        self.model_uuid = model_uuid

    @property
    def presigned_url(self):
        """Gets the presigned_url of this ModelPresignedUploadUrlResponse.  # noqa: E501

        Presigned URL to upload the model provided by AWS S3  # noqa: E501

        :return: The presigned_url of this ModelPresignedUploadUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._presigned_url

    @presigned_url.setter
    def presigned_url(self, presigned_url):
        """Sets the presigned_url of this ModelPresignedUploadUrlResponse.

        Presigned URL to upload the model provided by AWS S3  # noqa: E501

        :param presigned_url: The presigned_url of this ModelPresignedUploadUrlResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and presigned_url is None:  # noqa: E501
            raise ValueError("Invalid value for `presigned_url`, must not be `None`")  # noqa: E501

        self._presigned_url = presigned_url

    @property
    def model_uuid(self):
        """Gets the model_uuid of this ModelPresignedUploadUrlResponse.  # noqa: E501

        Model UUID to be uploaded.  # noqa: E501

        :return: The model_uuid of this ModelPresignedUploadUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._model_uuid

    @model_uuid.setter
    def model_uuid(self, model_uuid):
        """Sets the model_uuid of this ModelPresignedUploadUrlResponse.

        Model UUID to be uploaded.  # noqa: E501

        :param model_uuid: The model_uuid of this ModelPresignedUploadUrlResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and model_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `model_uuid`, must not be `None`")  # noqa: E501

        self._model_uuid = model_uuid

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
        if not isinstance(other, ModelPresignedUploadUrlResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelPresignedUploadUrlResponse):
            return True

        return self.to_dict() != other.to_dict()
