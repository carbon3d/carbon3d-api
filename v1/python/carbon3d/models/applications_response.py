# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class ApplicationsResponse(object):
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
        'applications': 'list[Application]'
    }

    attribute_map = {
        'applications': 'applications'
    }

    def __init__(self, applications=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._applications = None
        self.discriminator = None

        self.applications = applications

    @property
    def applications(self):
        """Gets the applications of this ApplicationsResponse.  # noqa: E501


        :return: The applications of this ApplicationsResponse.  # noqa: E501
        :rtype: list[Application]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this ApplicationsResponse.


        :param applications: The applications of this ApplicationsResponse.  # noqa: E501
        :type: list[Application]
        """
        if self.local_vars_configuration.client_side_validation and applications is None:  # noqa: E501
            raise ValueError("Invalid value for `applications`, must not be `None`")  # noqa: E501

        self._applications = applications

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
        if not isinstance(other, ApplicationsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationsResponse):
            return True

        return self.to_dict() != other.to_dict()
