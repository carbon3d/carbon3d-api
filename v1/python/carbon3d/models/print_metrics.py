# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.0.10
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintMetrics(object):
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
        'average_speed_mmhr': 'int',
        'consumed_resin_volume_ml': 'float',
        'minimum_required_resin_volume_ml': 'float',
        'estimated_total_resin_volume_ml': 'float',
        'measured_resin_volume_ml': 'float'
    }

    attribute_map = {
        'average_speed_mmhr': 'average_speed_mmhr',
        'consumed_resin_volume_ml': 'consumed_resin_volume_ml',
        'minimum_required_resin_volume_ml': 'minimum_required_resin_volume_ml',
        'estimated_total_resin_volume_ml': 'estimated_total_resin_volume_ml',
        'measured_resin_volume_ml': 'measured_resin_volume_ml'
    }

    def __init__(self, average_speed_mmhr=None, consumed_resin_volume_ml=None, minimum_required_resin_volume_ml=None, estimated_total_resin_volume_ml=None, measured_resin_volume_ml=None, local_vars_configuration=None):  # noqa: E501
        """PrintMetrics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._average_speed_mmhr = None
        self._consumed_resin_volume_ml = None
        self._minimum_required_resin_volume_ml = None
        self._estimated_total_resin_volume_ml = None
        self._measured_resin_volume_ml = None
        self.discriminator = None

        if average_speed_mmhr is not None:
            self.average_speed_mmhr = average_speed_mmhr
        if consumed_resin_volume_ml is not None:
            self.consumed_resin_volume_ml = consumed_resin_volume_ml
        if minimum_required_resin_volume_ml is not None:
            self.minimum_required_resin_volume_ml = minimum_required_resin_volume_ml
        if estimated_total_resin_volume_ml is not None:
            self.estimated_total_resin_volume_ml = estimated_total_resin_volume_ml
        if measured_resin_volume_ml is not None:
            self.measured_resin_volume_ml = measured_resin_volume_ml

    @property
    def average_speed_mmhr(self):
        """Gets the average_speed_mmhr of this PrintMetrics.  # noqa: E501


        :return: The average_speed_mmhr of this PrintMetrics.  # noqa: E501
        :rtype: int
        """
        return self._average_speed_mmhr

    @average_speed_mmhr.setter
    def average_speed_mmhr(self, average_speed_mmhr):
        """Sets the average_speed_mmhr of this PrintMetrics.


        :param average_speed_mmhr: The average_speed_mmhr of this PrintMetrics.  # noqa: E501
        :type: int
        """

        self._average_speed_mmhr = average_speed_mmhr

    @property
    def consumed_resin_volume_ml(self):
        """Gets the consumed_resin_volume_ml of this PrintMetrics.  # noqa: E501


        :return: The consumed_resin_volume_ml of this PrintMetrics.  # noqa: E501
        :rtype: float
        """
        return self._consumed_resin_volume_ml

    @consumed_resin_volume_ml.setter
    def consumed_resin_volume_ml(self, consumed_resin_volume_ml):
        """Sets the consumed_resin_volume_ml of this PrintMetrics.


        :param consumed_resin_volume_ml: The consumed_resin_volume_ml of this PrintMetrics.  # noqa: E501
        :type: float
        """

        self._consumed_resin_volume_ml = consumed_resin_volume_ml

    @property
    def minimum_required_resin_volume_ml(self):
        """Gets the minimum_required_resin_volume_ml of this PrintMetrics.  # noqa: E501


        :return: The minimum_required_resin_volume_ml of this PrintMetrics.  # noqa: E501
        :rtype: float
        """
        return self._minimum_required_resin_volume_ml

    @minimum_required_resin_volume_ml.setter
    def minimum_required_resin_volume_ml(self, minimum_required_resin_volume_ml):
        """Sets the minimum_required_resin_volume_ml of this PrintMetrics.


        :param minimum_required_resin_volume_ml: The minimum_required_resin_volume_ml of this PrintMetrics.  # noqa: E501
        :type: float
        """

        self._minimum_required_resin_volume_ml = minimum_required_resin_volume_ml

    @property
    def estimated_total_resin_volume_ml(self):
        """Gets the estimated_total_resin_volume_ml of this PrintMetrics.  # noqa: E501


        :return: The estimated_total_resin_volume_ml of this PrintMetrics.  # noqa: E501
        :rtype: float
        """
        return self._estimated_total_resin_volume_ml

    @estimated_total_resin_volume_ml.setter
    def estimated_total_resin_volume_ml(self, estimated_total_resin_volume_ml):
        """Sets the estimated_total_resin_volume_ml of this PrintMetrics.


        :param estimated_total_resin_volume_ml: The estimated_total_resin_volume_ml of this PrintMetrics.  # noqa: E501
        :type: float
        """

        self._estimated_total_resin_volume_ml = estimated_total_resin_volume_ml

    @property
    def measured_resin_volume_ml(self):
        """Gets the measured_resin_volume_ml of this PrintMetrics.  # noqa: E501


        :return: The measured_resin_volume_ml of this PrintMetrics.  # noqa: E501
        :rtype: float
        """
        return self._measured_resin_volume_ml

    @measured_resin_volume_ml.setter
    def measured_resin_volume_ml(self, measured_resin_volume_ml):
        """Sets the measured_resin_volume_ml of this PrintMetrics.


        :param measured_resin_volume_ml: The measured_resin_volume_ml of this PrintMetrics.  # noqa: E501
        :type: float
        """

        self._measured_resin_volume_ml = measured_resin_volume_ml

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
        if not isinstance(other, PrintMetrics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintMetrics):
            return True

        return self.to_dict() != other.to_dict()
