# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.5
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartGenealogyBuildInfo(object):
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
        'build_uuid': 'str',
        'traveler_url': 'str',
        'slice_video_url': 'str',
        'error': 'str'
    }

    attribute_map = {
        'build_uuid': 'build_uuid',
        'traveler_url': 'traveler_url',
        'slice_video_url': 'slice_video_url',
        'error': 'error'
    }

    def __init__(self, build_uuid=None, traveler_url=None, slice_video_url=None, error=None, local_vars_configuration=None):  # noqa: E501
        """PartGenealogyBuildInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build_uuid = None
        self._traveler_url = None
        self._slice_video_url = None
        self._error = None
        self.discriminator = None

        if build_uuid is not None:
            self.build_uuid = build_uuid
        if traveler_url is not None:
            self.traveler_url = traveler_url
        if slice_video_url is not None:
            self.slice_video_url = slice_video_url
        if error is not None:
            self.error = error

    @property
    def build_uuid(self):
        """Gets the build_uuid of this PartGenealogyBuildInfo.  # noqa: E501


        :return: The build_uuid of this PartGenealogyBuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._build_uuid

    @build_uuid.setter
    def build_uuid(self, build_uuid):
        """Sets the build_uuid of this PartGenealogyBuildInfo.


        :param build_uuid: The build_uuid of this PartGenealogyBuildInfo.  # noqa: E501
        :type: str
        """

        self._build_uuid = build_uuid

    @property
    def traveler_url(self):
        """Gets the traveler_url of this PartGenealogyBuildInfo.  # noqa: E501


        :return: The traveler_url of this PartGenealogyBuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._traveler_url

    @traveler_url.setter
    def traveler_url(self, traveler_url):
        """Sets the traveler_url of this PartGenealogyBuildInfo.


        :param traveler_url: The traveler_url of this PartGenealogyBuildInfo.  # noqa: E501
        :type: str
        """

        self._traveler_url = traveler_url

    @property
    def slice_video_url(self):
        """Gets the slice_video_url of this PartGenealogyBuildInfo.  # noqa: E501


        :return: The slice_video_url of this PartGenealogyBuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._slice_video_url

    @slice_video_url.setter
    def slice_video_url(self, slice_video_url):
        """Sets the slice_video_url of this PartGenealogyBuildInfo.


        :param slice_video_url: The slice_video_url of this PartGenealogyBuildInfo.  # noqa: E501
        :type: str
        """

        self._slice_video_url = slice_video_url

    @property
    def error(self):
        """Gets the error of this PartGenealogyBuildInfo.  # noqa: E501


        :return: The error of this PartGenealogyBuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PartGenealogyBuildInfo.


        :param error: The error of this PartGenealogyBuildInfo.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if not isinstance(other, PartGenealogyBuildInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartGenealogyBuildInfo):
            return True

        return self.to_dict() != other.to_dict()
