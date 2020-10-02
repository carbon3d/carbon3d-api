# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.5
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintConfig(object):
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
        'resin_name': 'str',
        'print_profile': 'str',
        'release_film_nm': 'int',
        'slice_thickness_nm': 'int'
    }

    attribute_map = {
        'resin_name': 'resin_name',
        'print_profile': 'print_profile',
        'release_film_nm': 'release_film_nm',
        'slice_thickness_nm': 'slice_thickness_nm'
    }

    def __init__(self, resin_name=None, print_profile=None, release_film_nm=None, slice_thickness_nm=None, local_vars_configuration=None):  # noqa: E501
        """PrintConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resin_name = None
        self._print_profile = None
        self._release_film_nm = None
        self._slice_thickness_nm = None
        self.discriminator = None

        if resin_name is not None:
            self.resin_name = resin_name
        if print_profile is not None:
            self.print_profile = print_profile
        if release_film_nm is not None:
            self.release_film_nm = release_film_nm
        if slice_thickness_nm is not None:
            self.slice_thickness_nm = slice_thickness_nm

    @property
    def resin_name(self):
        """Gets the resin_name of this PrintConfig.  # noqa: E501


        :return: The resin_name of this PrintConfig.  # noqa: E501
        :rtype: str
        """
        return self._resin_name

    @resin_name.setter
    def resin_name(self, resin_name):
        """Sets the resin_name of this PrintConfig.


        :param resin_name: The resin_name of this PrintConfig.  # noqa: E501
        :type: str
        """

        self._resin_name = resin_name

    @property
    def print_profile(self):
        """Gets the print_profile of this PrintConfig.  # noqa: E501


        :return: The print_profile of this PrintConfig.  # noqa: E501
        :rtype: str
        """
        return self._print_profile

    @print_profile.setter
    def print_profile(self, print_profile):
        """Sets the print_profile of this PrintConfig.


        :param print_profile: The print_profile of this PrintConfig.  # noqa: E501
        :type: str
        """

        self._print_profile = print_profile

    @property
    def release_film_nm(self):
        """Gets the release_film_nm of this PrintConfig.  # noqa: E501


        :return: The release_film_nm of this PrintConfig.  # noqa: E501
        :rtype: int
        """
        return self._release_film_nm

    @release_film_nm.setter
    def release_film_nm(self, release_film_nm):
        """Sets the release_film_nm of this PrintConfig.


        :param release_film_nm: The release_film_nm of this PrintConfig.  # noqa: E501
        :type: int
        """

        self._release_film_nm = release_film_nm

    @property
    def slice_thickness_nm(self):
        """Gets the slice_thickness_nm of this PrintConfig.  # noqa: E501


        :return: The slice_thickness_nm of this PrintConfig.  # noqa: E501
        :rtype: int
        """
        return self._slice_thickness_nm

    @slice_thickness_nm.setter
    def slice_thickness_nm(self, slice_thickness_nm):
        """Sets the slice_thickness_nm of this PrintConfig.


        :param slice_thickness_nm: The slice_thickness_nm of this PrintConfig.  # noqa: E501
        :type: int
        """

        self._slice_thickness_nm = slice_thickness_nm

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
        if not isinstance(other, PrintConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintConfig):
            return True

        return self.to_dict() != other.to_dict()
