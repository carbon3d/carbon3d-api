# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.6
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartMeasurementTemplateCategoryOptions(object):
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
        'fail': 'list[str]',
        'flag': 'list[str]',
        '_pass': 'list[str]'
    }

    attribute_map = {
        'fail': 'fail',
        'flag': 'flag',
        '_pass': 'pass'
    }

    def __init__(self, fail=None, flag=None, _pass=None, local_vars_configuration=None):  # noqa: E501
        """PartMeasurementTemplateCategoryOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fail = None
        self._flag = None
        self.__pass = None
        self.discriminator = None

        if fail is not None:
            self.fail = fail
        if flag is not None:
            self.flag = flag
        if _pass is not None:
            self._pass = _pass

    @property
    def fail(self):
        """Gets the fail of this PartMeasurementTemplateCategoryOptions.  # noqa: E501


        :return: The fail of this PartMeasurementTemplateCategoryOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        """Sets the fail of this PartMeasurementTemplateCategoryOptions.


        :param fail: The fail of this PartMeasurementTemplateCategoryOptions.  # noqa: E501
        :type: list[str]
        """

        self._fail = fail

    @property
    def flag(self):
        """Gets the flag of this PartMeasurementTemplateCategoryOptions.  # noqa: E501


        :return: The flag of this PartMeasurementTemplateCategoryOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this PartMeasurementTemplateCategoryOptions.


        :param flag: The flag of this PartMeasurementTemplateCategoryOptions.  # noqa: E501
        :type: list[str]
        """

        self._flag = flag

    @property
    def _pass(self):
        """Gets the _pass of this PartMeasurementTemplateCategoryOptions.  # noqa: E501


        :return: The _pass of this PartMeasurementTemplateCategoryOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this PartMeasurementTemplateCategoryOptions.


        :param _pass: The _pass of this PartMeasurementTemplateCategoryOptions.  # noqa: E501
        :type: list[str]
        """

        self.__pass = _pass

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
        if not isinstance(other, PartMeasurementTemplateCategoryOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartMeasurementTemplateCategoryOptions):
            return True

        return self.to_dict() != other.to_dict()
