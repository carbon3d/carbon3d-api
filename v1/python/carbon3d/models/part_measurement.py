# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartMeasurement(object):
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
        'printed_part_uuid': 'str',
        'part_measurement_template_uuid': 'str',
        'value': 'float',
        'category_value': 'str',
        'updated_at': 'datetime',
        'measurement_result': 'str',
        'zones': 'list[str]',
        'notes': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'printed_part_uuid': 'printed_part_uuid',
        'part_measurement_template_uuid': 'part_measurement_template_uuid',
        'value': 'value',
        'category_value': 'category_value',
        'updated_at': 'updated_at',
        'measurement_result': 'measurement_result',
        'zones': 'zones',
        'notes': 'notes'
    }

    def __init__(self, uuid=None, printed_part_uuid=None, part_measurement_template_uuid=None, value=None, category_value=None, updated_at=None, measurement_result=None, zones=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """PartMeasurement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._printed_part_uuid = None
        self._part_measurement_template_uuid = None
        self._value = None
        self._category_value = None
        self._updated_at = None
        self._measurement_result = None
        self._zones = None
        self._notes = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if printed_part_uuid is not None:
            self.printed_part_uuid = printed_part_uuid
        if part_measurement_template_uuid is not None:
            self.part_measurement_template_uuid = part_measurement_template_uuid
        self.value = value
        self.category_value = category_value
        if updated_at is not None:
            self.updated_at = updated_at
        if measurement_result is not None:
            self.measurement_result = measurement_result
        if zones is not None:
            self.zones = zones
        if notes is not None:
            self.notes = notes

    @property
    def uuid(self):
        """Gets the uuid of this PartMeasurement.  # noqa: E501

        The uuid of the part measurement  # noqa: E501

        :return: The uuid of this PartMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PartMeasurement.

        The uuid of the part measurement  # noqa: E501

        :param uuid: The uuid of this PartMeasurement.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def printed_part_uuid(self):
        """Gets the printed_part_uuid of this PartMeasurement.  # noqa: E501

        The uuid of the printed part  # noqa: E501

        :return: The printed_part_uuid of this PartMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._printed_part_uuid

    @printed_part_uuid.setter
    def printed_part_uuid(self, printed_part_uuid):
        """Sets the printed_part_uuid of this PartMeasurement.

        The uuid of the printed part  # noqa: E501

        :param printed_part_uuid: The printed_part_uuid of this PartMeasurement.  # noqa: E501
        :type: str
        """

        self._printed_part_uuid = printed_part_uuid

    @property
    def part_measurement_template_uuid(self):
        """Gets the part_measurement_template_uuid of this PartMeasurement.  # noqa: E501

        The uuid of the part measurement template  # noqa: E501

        :return: The part_measurement_template_uuid of this PartMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._part_measurement_template_uuid

    @part_measurement_template_uuid.setter
    def part_measurement_template_uuid(self, part_measurement_template_uuid):
        """Sets the part_measurement_template_uuid of this PartMeasurement.

        The uuid of the part measurement template  # noqa: E501

        :param part_measurement_template_uuid: The part_measurement_template_uuid of this PartMeasurement.  # noqa: E501
        :type: str
        """

        self._part_measurement_template_uuid = part_measurement_template_uuid

    @property
    def value(self):
        """Gets the value of this PartMeasurement.  # noqa: E501

        Numerical value of a measurement (e.g. 5, 131.24)  # noqa: E501

        :return: The value of this PartMeasurement.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PartMeasurement.

        Numerical value of a measurement (e.g. 5, 131.24)  # noqa: E501

        :param value: The value of this PartMeasurement.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def category_value(self):
        """Gets the category_value of this PartMeasurement.  # noqa: E501

        Category value of a measurement (e.g. tear, long, etc.)  # noqa: E501

        :return: The category_value of this PartMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._category_value

    @category_value.setter
    def category_value(self, category_value):
        """Sets the category_value of this PartMeasurement.

        Category value of a measurement (e.g. tear, long, etc.)  # noqa: E501

        :param category_value: The category_value of this PartMeasurement.  # noqa: E501
        :type: str
        """

        self._category_value = category_value

    @property
    def updated_at(self):
        """Gets the updated_at of this PartMeasurement.  # noqa: E501

        Time when the measurement was taken  # noqa: E501

        :return: The updated_at of this PartMeasurement.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PartMeasurement.

        Time when the measurement was taken  # noqa: E501

        :param updated_at: The updated_at of this PartMeasurement.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def measurement_result(self):
        """Gets the measurement_result of this PartMeasurement.  # noqa: E501

        Result of the measurement  # noqa: E501

        :return: The measurement_result of this PartMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._measurement_result

    @measurement_result.setter
    def measurement_result(self, measurement_result):
        """Sets the measurement_result of this PartMeasurement.

        Result of the measurement  # noqa: E501

        :param measurement_result: The measurement_result of this PartMeasurement.  # noqa: E501
        :type: str
        """
        allowed_values = ["pass", "fail", "flag", "incomplete"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and measurement_result not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `measurement_result` ({0}), must be one of {1}"  # noqa: E501
                .format(measurement_result, allowed_values)
            )

        self._measurement_result = measurement_result

    @property
    def zones(self):
        """Gets the zones of this PartMeasurement.  # noqa: E501

        Array of zones where category value applies (e.g. front, side)  # noqa: E501

        :return: The zones of this PartMeasurement.  # noqa: E501
        :rtype: list[str]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this PartMeasurement.

        Array of zones where category value applies (e.g. front, side)  # noqa: E501

        :param zones: The zones of this PartMeasurement.  # noqa: E501
        :type: list[str]
        """

        self._zones = zones

    @property
    def notes(self):
        """Gets the notes of this PartMeasurement.  # noqa: E501

        Notes associated with measurement  # noqa: E501

        :return: The notes of this PartMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PartMeasurement.

        Notes associated with measurement  # noqa: E501

        :param notes: The notes of this PartMeasurement.  # noqa: E501
        :type: str
        """

        self._notes = notes

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
        if not isinstance(other, PartMeasurement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartMeasurement):
            return True

        return self.to_dict() != other.to_dict()
