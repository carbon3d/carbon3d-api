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


class PrintFeedback(object):
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
        'feedback_rating': 'float',
        'feedback_message': 'str'
    }

    attribute_map = {
        'feedback_rating': 'feedback_rating',
        'feedback_message': 'feedback_message'
    }

    def __init__(self, feedback_rating=None, feedback_message=None, local_vars_configuration=None):  # noqa: E501
        """PrintFeedback - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._feedback_rating = None
        self._feedback_message = None
        self.discriminator = None

        if feedback_rating is not None:
            self.feedback_rating = feedback_rating
        if feedback_message is not None:
            self.feedback_message = feedback_message

    @property
    def feedback_rating(self):
        """Gets the feedback_rating of this PrintFeedback.  # noqa: E501


        :return: The feedback_rating of this PrintFeedback.  # noqa: E501
        :rtype: float
        """
        return self._feedback_rating

    @feedback_rating.setter
    def feedback_rating(self, feedback_rating):
        """Sets the feedback_rating of this PrintFeedback.


        :param feedback_rating: The feedback_rating of this PrintFeedback.  # noqa: E501
        :type: float
        """

        self._feedback_rating = feedback_rating

    @property
    def feedback_message(self):
        """Gets the feedback_message of this PrintFeedback.  # noqa: E501


        :return: The feedback_message of this PrintFeedback.  # noqa: E501
        :rtype: str
        """
        return self._feedback_message

    @feedback_message.setter
    def feedback_message(self, feedback_message):
        """Sets the feedback_message of this PrintFeedback.


        :param feedback_message: The feedback_message of this PrintFeedback.  # noqa: E501
        :type: str
        """

        self._feedback_message = feedback_message

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
        if not isinstance(other, PrintFeedback):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintFeedback):
            return True

        return self.to_dict() != other.to_dict()
