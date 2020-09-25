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
        'serial_number': 'str',
        'tags': 'PrintedPartTags',
        'status': 'PrintedPartStatus',
        'genealogy': 'PartGenealogy',
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
        'serial_number': 'serial_number',
        'tags': 'tags',
        'status': 'status',
        'genealogy': 'genealogy',
        'error': 'error'
    }

    def __init__(self, uuid=None, part_uuid=None, model_uuid=None, part_number=None, build_uuid=None, part_order_uuid=None, part_order_number=None, print_order_uuid=None, print_order_number=None, print_id=None, serial_number=None, tags=None, status=None, genealogy=None, error=None, local_vars_configuration=None):  # noqa: E501
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
        self._serial_number = None
        self._tags = None
        self._status = None
        self._genealogy = None
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
        if serial_number is not None:
            self.serial_number = serial_number
        if tags is not None:
            self.tags = tags
        self.status = status
        self.genealogy = genealogy
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
    def genealogy(self):
        """Gets the genealogy of this PrintedPart.  # noqa: E501


        :return: The genealogy of this PrintedPart.  # noqa: E501
        :rtype: PartGenealogy
        """
        return self._genealogy

    @genealogy.setter
    def genealogy(self, genealogy):
        """Sets the genealogy of this PrintedPart.


        :param genealogy: The genealogy of this PrintedPart.  # noqa: E501
        :type: PartGenealogy
        """

        self._genealogy = genealogy

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
