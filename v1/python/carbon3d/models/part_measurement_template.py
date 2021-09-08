# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PartMeasurementTemplate(object):
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
        'updated_at': 'datetime',
        'production_sop_name': 'str',
        'production_sop_version': 'float',
        'operation_name': 'str',
        'measurement_name': 'str',
        'zones': 'list[str]',
        'zones_enabled': 'bool',
        'required_level': 'str',
        'measurement_type': 'str',
        'units': 'str',
        'min': 'float',
        'max': 'float',
        'measurement_classification': 'str',
        'category_options': 'PartMeasurementTemplateCategoryOptions'
    }

    attribute_map = {
        'uuid': 'uuid',
        'updated_at': 'updated_at',
        'production_sop_name': 'production_sop_name',
        'production_sop_version': 'production_sop_version',
        'operation_name': 'operation_name',
        'measurement_name': 'measurement_name',
        'zones': 'zones',
        'zones_enabled': 'zones_enabled',
        'required_level': 'required_level',
        'measurement_type': 'measurement_type',
        'units': 'units',
        'min': 'min',
        'max': 'max',
        'measurement_classification': 'measurement_classification',
        'category_options': 'category_options'
    }

    def __init__(self, uuid=None, updated_at=None, production_sop_name=None, production_sop_version=None, operation_name=None, measurement_name=None, zones=None, zones_enabled=None, required_level=None, measurement_type=None, units=None, min=None, max=None, measurement_classification=None, category_options=None, local_vars_configuration=None):  # noqa: E501
        """PartMeasurementTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._updated_at = None
        self._production_sop_name = None
        self._production_sop_version = None
        self._operation_name = None
        self._measurement_name = None
        self._zones = None
        self._zones_enabled = None
        self._required_level = None
        self._measurement_type = None
        self._units = None
        self._min = None
        self._max = None
        self._measurement_classification = None
        self._category_options = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if updated_at is not None:
            self.updated_at = updated_at
        if production_sop_name is not None:
            self.production_sop_name = production_sop_name
        if production_sop_version is not None:
            self.production_sop_version = production_sop_version
        if operation_name is not None:
            self.operation_name = operation_name
        if measurement_name is not None:
            self.measurement_name = measurement_name
        if zones is not None:
            self.zones = zones
        if zones_enabled is not None:
            self.zones_enabled = zones_enabled
        if required_level is not None:
            self.required_level = required_level
        if measurement_type is not None:
            self.measurement_type = measurement_type
        self.units = units
        self.min = min
        self.max = max
        self.measurement_classification = measurement_classification
        self.category_options = category_options

    @property
    def uuid(self):
        """Gets the uuid of this PartMeasurementTemplate.  # noqa: E501

        The uuid of the part measurement  # noqa: E501

        :return: The uuid of this PartMeasurementTemplate.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PartMeasurementTemplate.

        The uuid of the part measurement  # noqa: E501

        :param uuid: The uuid of this PartMeasurementTemplate.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def updated_at(self):
        """Gets the updated_at of this PartMeasurementTemplate.  # noqa: E501


        :return: The updated_at of this PartMeasurementTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PartMeasurementTemplate.


        :param updated_at: The updated_at of this PartMeasurementTemplate.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def production_sop_name(self):
        """Gets the production_sop_name of this PartMeasurementTemplate.  # noqa: E501


        :return: The production_sop_name of this PartMeasurementTemplate.  # noqa: E501
        :rtype: str
        """
        return self._production_sop_name

    @production_sop_name.setter
    def production_sop_name(self, production_sop_name):
        """Sets the production_sop_name of this PartMeasurementTemplate.


        :param production_sop_name: The production_sop_name of this PartMeasurementTemplate.  # noqa: E501
        :type: str
        """

        self._production_sop_name = production_sop_name

    @property
    def production_sop_version(self):
        """Gets the production_sop_version of this PartMeasurementTemplate.  # noqa: E501


        :return: The production_sop_version of this PartMeasurementTemplate.  # noqa: E501
        :rtype: float
        """
        return self._production_sop_version

    @production_sop_version.setter
    def production_sop_version(self, production_sop_version):
        """Sets the production_sop_version of this PartMeasurementTemplate.


        :param production_sop_version: The production_sop_version of this PartMeasurementTemplate.  # noqa: E501
        :type: float
        """

        self._production_sop_version = production_sop_version

    @property
    def operation_name(self):
        """Gets the operation_name of this PartMeasurementTemplate.  # noqa: E501

        The operation during which this measurement is supposed to be taken  # noqa: E501

        :return: The operation_name of this PartMeasurementTemplate.  # noqa: E501
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        """Sets the operation_name of this PartMeasurementTemplate.

        The operation during which this measurement is supposed to be taken  # noqa: E501

        :param operation_name: The operation_name of this PartMeasurementTemplate.  # noqa: E501
        :type: str
        """

        self._operation_name = operation_name

    @property
    def measurement_name(self):
        """Gets the measurement_name of this PartMeasurementTemplate.  # noqa: E501


        :return: The measurement_name of this PartMeasurementTemplate.  # noqa: E501
        :rtype: str
        """
        return self._measurement_name

    @measurement_name.setter
    def measurement_name(self, measurement_name):
        """Sets the measurement_name of this PartMeasurementTemplate.


        :param measurement_name: The measurement_name of this PartMeasurementTemplate.  # noqa: E501
        :type: str
        """

        self._measurement_name = measurement_name

    @property
    def zones(self):
        """Gets the zones of this PartMeasurementTemplate.  # noqa: E501

        Options for zones that can be selected  # noqa: E501

        :return: The zones of this PartMeasurementTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this PartMeasurementTemplate.

        Options for zones that can be selected  # noqa: E501

        :param zones: The zones of this PartMeasurementTemplate.  # noqa: E501
        :type: list[str]
        """

        self._zones = zones

    @property
    def zones_enabled(self):
        """Gets the zones_enabled of this PartMeasurementTemplate.  # noqa: E501


        :return: The zones_enabled of this PartMeasurementTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._zones_enabled

    @zones_enabled.setter
    def zones_enabled(self, zones_enabled):
        """Sets the zones_enabled of this PartMeasurementTemplate.


        :param zones_enabled: The zones_enabled of this PartMeasurementTemplate.  # noqa: E501
        :type: bool
        """

        self._zones_enabled = zones_enabled

    @property
    def required_level(self):
        """Gets the required_level of this PartMeasurementTemplate.  # noqa: E501

        Requirement level of the measurement template  # noqa: E501

        :return: The required_level of this PartMeasurementTemplate.  # noqa: E501
        :rtype: str
        """
        return self._required_level

    @required_level.setter
    def required_level(self, required_level):
        """Sets the required_level of this PartMeasurementTemplate.

        Requirement level of the measurement template  # noqa: E501

        :param required_level: The required_level of this PartMeasurementTemplate.  # noqa: E501
        :type: str
        """
        allowed_values = ["required", "not_required", "required_for_failure"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and required_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `required_level` ({0}), must be one of {1}"  # noqa: E501
                .format(required_level, allowed_values)
            )

        self._required_level = required_level

    @property
    def measurement_type(self):
        """Gets the measurement_type of this PartMeasurementTemplate.  # noqa: E501


        :return: The measurement_type of this PartMeasurementTemplate.  # noqa: E501
        :rtype: str
        """
        return self._measurement_type

    @measurement_type.setter
    def measurement_type(self, measurement_type):
        """Sets the measurement_type of this PartMeasurementTemplate.


        :param measurement_type: The measurement_type of this PartMeasurementTemplate.  # noqa: E501
        :type: str
        """
        allowed_values = ["process", "value", "category"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and measurement_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `measurement_type` ({0}), must be one of {1}"  # noqa: E501
                .format(measurement_type, allowed_values)
            )

        self._measurement_type = measurement_type

    @property
    def units(self):
        """Gets the units of this PartMeasurementTemplate.  # noqa: E501


        :return: The units of this PartMeasurementTemplate.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this PartMeasurementTemplate.


        :param units: The units of this PartMeasurementTemplate.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def min(self):
        """Gets the min of this PartMeasurementTemplate.  # noqa: E501


        :return: The min of this PartMeasurementTemplate.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this PartMeasurementTemplate.


        :param min: The min of this PartMeasurementTemplate.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this PartMeasurementTemplate.  # noqa: E501


        :return: The max of this PartMeasurementTemplate.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this PartMeasurementTemplate.


        :param max: The max of this PartMeasurementTemplate.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def measurement_classification(self):
        """Gets the measurement_classification of this PartMeasurementTemplate.  # noqa: E501


        :return: The measurement_classification of this PartMeasurementTemplate.  # noqa: E501
        :rtype: str
        """
        return self._measurement_classification

    @measurement_classification.setter
    def measurement_classification(self, measurement_classification):
        """Sets the measurement_classification of this PartMeasurementTemplate.


        :param measurement_classification: The measurement_classification of this PartMeasurementTemplate.  # noqa: E501
        :type: str
        """

        self._measurement_classification = measurement_classification

    @property
    def category_options(self):
        """Gets the category_options of this PartMeasurementTemplate.  # noqa: E501


        :return: The category_options of this PartMeasurementTemplate.  # noqa: E501
        :rtype: PartMeasurementTemplateCategoryOptions
        """
        return self._category_options

    @category_options.setter
    def category_options(self, category_options):
        """Sets the category_options of this PartMeasurementTemplate.


        :param category_options: The category_options of this PartMeasurementTemplate.  # noqa: E501
        :type: PartMeasurementTemplateCategoryOptions
        """

        self._category_options = category_options

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
        if not isinstance(other, PartMeasurementTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartMeasurementTemplate):
            return True

        return self.to_dict() != other.to_dict()
