# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.4.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrintedPart(object):
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
        'part_uuid': 'str',
        'model_uuid': 'str',
        'part_number': 'str',
        'build_uuid': 'str',
        'part_order_uuid': 'str',
        'part_order_number': 'str',
        'print_order_uuid': 'str',
        'print_order_number': 'str',
        'print_id': 'str',
        'project_blackline': 'float',
        'resin_cell_name': 'str',
        'resin_lot_number': 'str',
        'print_uuid': 'str',
        'serial_number': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'finished_at': 'datetime',
        'tags': 'PrintedPartTags',
        'status': 'PrintedPartStatus',
        'error': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'part_uuid': 'part_uuid',
        'model_uuid': 'model_uuid',
        'part_number': 'part_number',
        'build_uuid': 'build_uuid',
        'part_order_uuid': 'part_order_uuid',
        'part_order_number': 'part_order_number',
        'print_order_uuid': 'print_order_uuid',
        'print_order_number': 'print_order_number',
        'print_id': 'print_id',
        'project_blackline': 'project_blackline',
        'resin_cell_name': 'resin_cell_name',
        'resin_lot_number': 'resin_lot_number',
        'print_uuid': 'print_uuid',
        'serial_number': 'serial_number',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'finished_at': 'finished_at',
        'tags': 'tags',
        'status': 'status',
        'error': 'error'
    }

    def __init__(self, uuid=None, part_uuid=None, model_uuid=None, part_number=None, build_uuid=None, part_order_uuid=None, part_order_number=None, print_order_uuid=None, print_order_number=None, print_id=None, project_blackline=None, resin_cell_name=None, resin_lot_number=None, print_uuid=None, serial_number=None, created_at=None, updated_at=None, finished_at=None, tags=None, status=None, error=None, local_vars_configuration=None):  # noqa: E501
        """PrintedPart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._part_uuid = None
        self._model_uuid = None
        self._part_number = None
        self._build_uuid = None
        self._part_order_uuid = None
        self._part_order_number = None
        self._print_order_uuid = None
        self._print_order_number = None
        self._print_id = None
        self._project_blackline = None
        self._resin_cell_name = None
        self._resin_lot_number = None
        self._print_uuid = None
        self._serial_number = None
        self._created_at = None
        self._updated_at = None
        self._finished_at = None
        self._tags = None
        self._status = None
        self._error = None
        self.discriminator = None

        self.uuid = uuid
        self.part_uuid = part_uuid
        if model_uuid is not None:
            self.model_uuid = model_uuid
        if part_number is not None:
            self.part_number = part_number
        if build_uuid is not None:
            self.build_uuid = build_uuid
        if part_order_uuid is not None:
            self.part_order_uuid = part_order_uuid
        if part_order_number is not None:
            self.part_order_number = part_order_number
        if print_order_uuid is not None:
            self.print_order_uuid = print_order_uuid
        if print_order_number is not None:
            self.print_order_number = print_order_number
        if print_id is not None:
            self.print_id = print_id
        if project_blackline is not None:
            self.project_blackline = project_blackline
        if resin_cell_name is not None:
            self.resin_cell_name = resin_cell_name
        if resin_lot_number is not None:
            self.resin_lot_number = resin_lot_number
        if print_uuid is not None:
            self.print_uuid = print_uuid
        if serial_number is not None:
            self.serial_number = serial_number
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.finished_at = finished_at
        if tags is not None:
            self.tags = tags
        self.status = status
        if error is not None:
            self.error = error

    @property
    def uuid(self):
        """Gets the uuid of this PrintedPart.  # noqa: E501

        Printed Part UUID  # noqa: E501

        :return: The uuid of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PrintedPart.

        Printed Part UUID  # noqa: E501

        :param uuid: The uuid of this PrintedPart.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def part_uuid(self):
        """Gets the part_uuid of this PrintedPart.  # noqa: E501


        :return: The part_uuid of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._part_uuid

    @part_uuid.setter
    def part_uuid(self, part_uuid):
        """Sets the part_uuid of this PrintedPart.


        :param part_uuid: The part_uuid of this PrintedPart.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and part_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `part_uuid`, must not be `None`")  # noqa: E501

        self._part_uuid = part_uuid

    @property
    def model_uuid(self):
        """Gets the model_uuid of this PrintedPart.  # noqa: E501


        :return: The model_uuid of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._model_uuid

    @model_uuid.setter
    def model_uuid(self, model_uuid):
        """Sets the model_uuid of this PrintedPart.


        :param model_uuid: The model_uuid of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._model_uuid = model_uuid

    @property
    def part_number(self):
        """Gets the part_number of this PrintedPart.  # noqa: E501


        :return: The part_number of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this PrintedPart.


        :param part_number: The part_number of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def build_uuid(self):
        """Gets the build_uuid of this PrintedPart.  # noqa: E501


        :return: The build_uuid of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._build_uuid

    @build_uuid.setter
    def build_uuid(self, build_uuid):
        """Sets the build_uuid of this PrintedPart.


        :param build_uuid: The build_uuid of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._build_uuid = build_uuid

    @property
    def part_order_uuid(self):
        """Gets the part_order_uuid of this PrintedPart.  # noqa: E501


        :return: The part_order_uuid of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._part_order_uuid

    @part_order_uuid.setter
    def part_order_uuid(self, part_order_uuid):
        """Sets the part_order_uuid of this PrintedPart.


        :param part_order_uuid: The part_order_uuid of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._part_order_uuid = part_order_uuid

    @property
    def part_order_number(self):
        """Gets the part_order_number of this PrintedPart.  # noqa: E501


        :return: The part_order_number of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._part_order_number

    @part_order_number.setter
    def part_order_number(self, part_order_number):
        """Sets the part_order_number of this PrintedPart.


        :param part_order_number: The part_order_number of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._part_order_number = part_order_number

    @property
    def print_order_uuid(self):
        """Gets the print_order_uuid of this PrintedPart.  # noqa: E501


        :return: The print_order_uuid of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._print_order_uuid

    @print_order_uuid.setter
    def print_order_uuid(self, print_order_uuid):
        """Sets the print_order_uuid of this PrintedPart.


        :param print_order_uuid: The print_order_uuid of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._print_order_uuid = print_order_uuid

    @property
    def print_order_number(self):
        """Gets the print_order_number of this PrintedPart.  # noqa: E501


        :return: The print_order_number of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._print_order_number

    @print_order_number.setter
    def print_order_number(self, print_order_number):
        """Sets the print_order_number of this PrintedPart.


        :param print_order_number: The print_order_number of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._print_order_number = print_order_number

    @property
    def print_id(self):
        """Gets the print_id of this PrintedPart.  # noqa: E501


        :return: The print_id of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._print_id

    @print_id.setter
    def print_id(self, print_id):
        """Sets the print_id of this PrintedPart.


        :param print_id: The print_id of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._print_id = print_id

    @property
    def project_blackline(self):
        """Gets the project_blackline of this PrintedPart.  # noqa: E501


        :return: The project_blackline of this PrintedPart.  # noqa: E501
        :rtype: float
        """
        return self._project_blackline

    @project_blackline.setter
    def project_blackline(self, project_blackline):
        """Sets the project_blackline of this PrintedPart.


        :param project_blackline: The project_blackline of this PrintedPart.  # noqa: E501
        :type: float
        """

        self._project_blackline = project_blackline

    @property
    def resin_cell_name(self):
        """Gets the resin_cell_name of this PrintedPart.  # noqa: E501


        :return: The resin_cell_name of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._resin_cell_name

    @resin_cell_name.setter
    def resin_cell_name(self, resin_cell_name):
        """Sets the resin_cell_name of this PrintedPart.


        :param resin_cell_name: The resin_cell_name of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._resin_cell_name = resin_cell_name

    @property
    def resin_lot_number(self):
        """Gets the resin_lot_number of this PrintedPart.  # noqa: E501


        :return: The resin_lot_number of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._resin_lot_number

    @resin_lot_number.setter
    def resin_lot_number(self, resin_lot_number):
        """Sets the resin_lot_number of this PrintedPart.


        :param resin_lot_number: The resin_lot_number of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._resin_lot_number = resin_lot_number

    @property
    def print_uuid(self):
        """Gets the print_uuid of this PrintedPart.  # noqa: E501


        :return: The print_uuid of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._print_uuid

    @print_uuid.setter
    def print_uuid(self, print_uuid):
        """Sets the print_uuid of this PrintedPart.


        :param print_uuid: The print_uuid of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._print_uuid = print_uuid

    @property
    def serial_number(self):
        """Gets the serial_number of this PrintedPart.  # noqa: E501

        Only created after printing  # noqa: E501

        :return: The serial_number of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this PrintedPart.

        Only created after printing  # noqa: E501

        :param serial_number: The serial_number of this PrintedPart.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def created_at(self):
        """Gets the created_at of this PrintedPart.  # noqa: E501


        :return: The created_at of this PrintedPart.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PrintedPart.


        :param created_at: The created_at of this PrintedPart.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PrintedPart.  # noqa: E501


        :return: The updated_at of this PrintedPart.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PrintedPart.


        :param updated_at: The updated_at of this PrintedPart.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def finished_at(self):
        """Gets the finished_at of this PrintedPart.  # noqa: E501


        :return: The finished_at of this PrintedPart.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this PrintedPart.


        :param finished_at: The finished_at of this PrintedPart.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def tags(self):
        """Gets the tags of this PrintedPart.  # noqa: E501


        :return: The tags of this PrintedPart.  # noqa: E501
        :rtype: PrintedPartTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PrintedPart.


        :param tags: The tags of this PrintedPart.  # noqa: E501
        :type: PrintedPartTags
        """

        self._tags = tags

    @property
    def status(self):
        """Gets the status of this PrintedPart.  # noqa: E501


        :return: The status of this PrintedPart.  # noqa: E501
        :rtype: PrintedPartStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PrintedPart.


        :param status: The status of this PrintedPart.  # noqa: E501
        :type: PrintedPartStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def error(self):
        """Gets the error of this PrintedPart.  # noqa: E501

        Error message (if part could not be produced)  # noqa: E501

        :return: The error of this PrintedPart.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PrintedPart.

        Error message (if part could not be produced)  # noqa: E501

        :param error: The error of this PrintedPart.  # noqa: E501
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
        if not isinstance(other, PrintedPart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintedPart):
            return True

        return self.to_dict() != other.to_dict()
