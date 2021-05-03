# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.3
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class ModelPrint(object):
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
        'name': 'str',
        'print_id': 'str',
        'uuid': 'str',
        'build_uuid': 'str',
        'finished_at': 'datetime',
        'started_at': 'datetime',
        'remaining_sec': 'int',
        'printed_by': 'str',
        'print_order_uuid': 'str',
        'print_order_number': 'str',
        'status': 'str',
        'origin': 'PrintOrigin',
        'config': 'PrintConfig',
        'metrics': 'PrintMetrics',
        'feedback': 'PrintFeedback'
    }

    attribute_map = {
        'name': 'name',
        'print_id': 'print_id',
        'uuid': 'uuid',
        'build_uuid': 'build_uuid',
        'finished_at': 'finished_at',
        'started_at': 'started_at',
        'remaining_sec': 'remaining_sec',
        'printed_by': 'printed_by',
        'print_order_uuid': 'print_order_uuid',
        'print_order_number': 'print_order_number',
        'status': 'status',
        'origin': 'origin',
        'config': 'config',
        'metrics': 'metrics',
        'feedback': 'feedback'
    }

    def __init__(self, name=None, print_id=None, uuid=None, build_uuid=None, finished_at=None, started_at=None, remaining_sec=None, printed_by=None, print_order_uuid=None, print_order_number=None, status=None, origin=None, config=None, metrics=None, feedback=None, local_vars_configuration=None):  # noqa: E501
        """ModelPrint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._print_id = None
        self._uuid = None
        self._build_uuid = None
        self._finished_at = None
        self._started_at = None
        self._remaining_sec = None
        self._printed_by = None
        self._print_order_uuid = None
        self._print_order_number = None
        self._status = None
        self._origin = None
        self._config = None
        self._metrics = None
        self._feedback = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if print_id is not None:
            self.print_id = print_id
        if uuid is not None:
            self.uuid = uuid
        if build_uuid is not None:
            self.build_uuid = build_uuid
        if finished_at is not None:
            self.finished_at = finished_at
        if started_at is not None:
            self.started_at = started_at
        if remaining_sec is not None:
            self.remaining_sec = remaining_sec
        if printed_by is not None:
            self.printed_by = printed_by
        if print_order_uuid is not None:
            self.print_order_uuid = print_order_uuid
        if print_order_number is not None:
            self.print_order_number = print_order_number
        if status is not None:
            self.status = status
        if origin is not None:
            self.origin = origin
        if config is not None:
            self.config = config
        if metrics is not None:
            self.metrics = metrics
        if feedback is not None:
            self.feedback = feedback

    @property
    def name(self):
        """Gets the name of this ModelPrint.  # noqa: E501


        :return: The name of this ModelPrint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelPrint.


        :param name: The name of this ModelPrint.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def print_id(self):
        """Gets the print_id of this ModelPrint.  # noqa: E501


        :return: The print_id of this ModelPrint.  # noqa: E501
        :rtype: str
        """
        return self._print_id

    @print_id.setter
    def print_id(self, print_id):
        """Sets the print_id of this ModelPrint.


        :param print_id: The print_id of this ModelPrint.  # noqa: E501
        :type: str
        """

        self._print_id = print_id

    @property
    def uuid(self):
        """Gets the uuid of this ModelPrint.  # noqa: E501


        :return: The uuid of this ModelPrint.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ModelPrint.


        :param uuid: The uuid of this ModelPrint.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def build_uuid(self):
        """Gets the build_uuid of this ModelPrint.  # noqa: E501


        :return: The build_uuid of this ModelPrint.  # noqa: E501
        :rtype: str
        """
        return self._build_uuid

    @build_uuid.setter
    def build_uuid(self, build_uuid):
        """Sets the build_uuid of this ModelPrint.


        :param build_uuid: The build_uuid of this ModelPrint.  # noqa: E501
        :type: str
        """

        self._build_uuid = build_uuid

    @property
    def finished_at(self):
        """Gets the finished_at of this ModelPrint.  # noqa: E501


        :return: The finished_at of this ModelPrint.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this ModelPrint.


        :param finished_at: The finished_at of this ModelPrint.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def started_at(self):
        """Gets the started_at of this ModelPrint.  # noqa: E501


        :return: The started_at of this ModelPrint.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this ModelPrint.


        :param started_at: The started_at of this ModelPrint.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def remaining_sec(self):
        """Gets the remaining_sec of this ModelPrint.  # noqa: E501

        Estimated time until expected print completion (in seconds)  # noqa: E501

        :return: The remaining_sec of this ModelPrint.  # noqa: E501
        :rtype: int
        """
        return self._remaining_sec

    @remaining_sec.setter
    def remaining_sec(self, remaining_sec):
        """Sets the remaining_sec of this ModelPrint.

        Estimated time until expected print completion (in seconds)  # noqa: E501

        :param remaining_sec: The remaining_sec of this ModelPrint.  # noqa: E501
        :type: int
        """

        self._remaining_sec = remaining_sec

    @property
    def printed_by(self):
        """Gets the printed_by of this ModelPrint.  # noqa: E501


        :return: The printed_by of this ModelPrint.  # noqa: E501
        :rtype: str
        """
        return self._printed_by

    @printed_by.setter
    def printed_by(self, printed_by):
        """Sets the printed_by of this ModelPrint.


        :param printed_by: The printed_by of this ModelPrint.  # noqa: E501
        :type: str
        """

        self._printed_by = printed_by

    @property
    def print_order_uuid(self):
        """Gets the print_order_uuid of this ModelPrint.  # noqa: E501


        :return: The print_order_uuid of this ModelPrint.  # noqa: E501
        :rtype: str
        """
        return self._print_order_uuid

    @print_order_uuid.setter
    def print_order_uuid(self, print_order_uuid):
        """Sets the print_order_uuid of this ModelPrint.


        :param print_order_uuid: The print_order_uuid of this ModelPrint.  # noqa: E501
        :type: str
        """

        self._print_order_uuid = print_order_uuid

    @property
    def print_order_number(self):
        """Gets the print_order_number of this ModelPrint.  # noqa: E501


        :return: The print_order_number of this ModelPrint.  # noqa: E501
        :rtype: str
        """
        return self._print_order_number

    @print_order_number.setter
    def print_order_number(self, print_order_number):
        """Sets the print_order_number of this ModelPrint.


        :param print_order_number: The print_order_number of this ModelPrint.  # noqa: E501
        :type: str
        """

        self._print_order_number = print_order_number

    @property
    def status(self):
        """Gets the status of this ModelPrint.  # noqa: E501


        :return: The status of this ModelPrint.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelPrint.


        :param status: The status of this ModelPrint.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def origin(self):
        """Gets the origin of this ModelPrint.  # noqa: E501


        :return: The origin of this ModelPrint.  # noqa: E501
        :rtype: PrintOrigin
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this ModelPrint.


        :param origin: The origin of this ModelPrint.  # noqa: E501
        :type: PrintOrigin
        """

        self._origin = origin

    @property
    def config(self):
        """Gets the config of this ModelPrint.  # noqa: E501


        :return: The config of this ModelPrint.  # noqa: E501
        :rtype: PrintConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ModelPrint.


        :param config: The config of this ModelPrint.  # noqa: E501
        :type: PrintConfig
        """

        self._config = config

    @property
    def metrics(self):
        """Gets the metrics of this ModelPrint.  # noqa: E501


        :return: The metrics of this ModelPrint.  # noqa: E501
        :rtype: PrintMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ModelPrint.


        :param metrics: The metrics of this ModelPrint.  # noqa: E501
        :type: PrintMetrics
        """

        self._metrics = metrics

    @property
    def feedback(self):
        """Gets the feedback of this ModelPrint.  # noqa: E501


        :return: The feedback of this ModelPrint.  # noqa: E501
        :rtype: PrintFeedback
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """Sets the feedback of this ModelPrint.


        :param feedback: The feedback of this ModelPrint.  # noqa: E501
        :type: PrintFeedback
        """

        self._feedback = feedback

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
        if not isinstance(other, ModelPrint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelPrint):
            return True

        return self.to_dict() != other.to_dict()
