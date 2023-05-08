# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.6
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from carbon3d.api_client import ApiClient
from carbon3d.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PrintsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_prints(self, limit, **kwargs):  # noqa: E501
        """List finished prints information  # noqa: E501

        Fetch prints  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prints(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param str cursor: Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d)
        :param list[str] uuid: An array of UUIDs
        :param list[str] application_uuid: An array of Application UUIDs
        :param str started_before: Print started before timestamp (exclusive)
        :param str started_after: Print started at or after timestamp (inclusive)
        :param str finished_before: Print finished before timestamp (exclusive)
        :param str finished_after: Print finished at or after timestamp (inclusive)
        :param list[str] print_id: An array of Print IDs
        :param list[str] status: An array of statuses.
        :param list[str] print_order_number: An array of number(s) of the print_order submitted
        :param list[str] print_order_uuid: An array of UUID(s) of the print_order submitted
        :param list[str] printer_serial: An array of serials of the Printer(s) used to print
        :param list[str] build_uuid: An array of Build UUIDs
        :param list[str] printer_name: An array of names of the Printer(s) used to print
        :param list[str] platform_serial: An array of serials of the Platform(s) used to print
        :param list[str] sort: Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `status`, `started_at`, `finished_at`, `print_order_number`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PrintsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_prints_with_http_info(limit, **kwargs)  # noqa: E501

    def get_prints_with_http_info(self, limit, **kwargs):  # noqa: E501
        """List finished prints information  # noqa: E501

        Fetch prints  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prints_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param str cursor: Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d)
        :param list[str] uuid: An array of UUIDs
        :param list[str] application_uuid: An array of Application UUIDs
        :param str started_before: Print started before timestamp (exclusive)
        :param str started_after: Print started at or after timestamp (inclusive)
        :param str finished_before: Print finished before timestamp (exclusive)
        :param str finished_after: Print finished at or after timestamp (inclusive)
        :param list[str] print_id: An array of Print IDs
        :param list[str] status: An array of statuses.
        :param list[str] print_order_number: An array of number(s) of the print_order submitted
        :param list[str] print_order_uuid: An array of UUID(s) of the print_order submitted
        :param list[str] printer_serial: An array of serials of the Printer(s) used to print
        :param list[str] build_uuid: An array of Build UUIDs
        :param list[str] printer_name: An array of names of the Printer(s) used to print
        :param list[str] platform_serial: An array of serials of the Platform(s) used to print
        :param list[str] sort: Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `status`, `started_at`, `finished_at`, `print_order_number`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PrintsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'cursor',
            'uuid',
            'application_uuid',
            'started_before',
            'started_after',
            'finished_before',
            'finished_after',
            'print_id',
            'status',
            'print_order_number',
            'print_order_uuid',
            'printer_serial',
            'build_uuid',
            'printer_name',
            'platform_serial',
            'sort'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prints" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'limit' is set
        if self.api_client.client_side_validation and ('limit' not in local_var_params or  # noqa: E501
                                                        local_var_params['limit'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `limit` when calling `get_prints`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_prints`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_prints`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('application_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['application_uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `application_uuid` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('application_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['application_uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `application_uuid` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('print_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['print_id']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `print_id` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('print_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['print_id']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `print_id` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('status' in local_var_params and  # noqa: E501
                                                        len(local_var_params['status']) > 5):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `status` when calling `get_prints`, number of items must be less than or equal to `5`")  # noqa: E501
        if self.api_client.client_side_validation and ('status' in local_var_params and  # noqa: E501
                                                        len(local_var_params['status']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `status` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('print_order_number' in local_var_params and  # noqa: E501
                                                        len(local_var_params['print_order_number']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `print_order_number` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('print_order_number' in local_var_params and  # noqa: E501
                                                        len(local_var_params['print_order_number']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `print_order_number` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('print_order_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['print_order_uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `print_order_uuid` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('print_order_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['print_order_uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `print_order_uuid` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('printer_serial' in local_var_params and  # noqa: E501
                                                        len(local_var_params['printer_serial']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `printer_serial` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('printer_serial' in local_var_params and  # noqa: E501
                                                        len(local_var_params['printer_serial']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `printer_serial` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('build_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['build_uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `build_uuid` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('build_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['build_uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `build_uuid` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('printer_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['printer_name']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `printer_name` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('printer_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['printer_name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `printer_name` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('platform_serial' in local_var_params and  # noqa: E501
                                                        len(local_var_params['platform_serial']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `platform_serial` when calling `get_prints`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('platform_serial' in local_var_params and  # noqa: E501
                                                        len(local_var_params['platform_serial']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `platform_serial` when calling `get_prints`, number of items must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if 'uuid' in local_var_params and local_var_params['uuid'] is not None:  # noqa: E501
            query_params.append(('uuid', local_var_params['uuid']))  # noqa: E501
            collection_formats['uuid'] = 'multi'  # noqa: E501
        if 'application_uuid' in local_var_params and local_var_params['application_uuid'] is not None:  # noqa: E501
            query_params.append(('application_uuid', local_var_params['application_uuid']))  # noqa: E501
            collection_formats['application_uuid'] = 'multi'  # noqa: E501
        if 'started_before' in local_var_params and local_var_params['started_before'] is not None:  # noqa: E501
            query_params.append(('started_before', local_var_params['started_before']))  # noqa: E501
        if 'started_after' in local_var_params and local_var_params['started_after'] is not None:  # noqa: E501
            query_params.append(('started_after', local_var_params['started_after']))  # noqa: E501
        if 'finished_before' in local_var_params and local_var_params['finished_before'] is not None:  # noqa: E501
            query_params.append(('finished_before', local_var_params['finished_before']))  # noqa: E501
        if 'finished_after' in local_var_params and local_var_params['finished_after'] is not None:  # noqa: E501
            query_params.append(('finished_after', local_var_params['finished_after']))  # noqa: E501
        if 'print_id' in local_var_params and local_var_params['print_id'] is not None:  # noqa: E501
            query_params.append(('print_id', local_var_params['print_id']))  # noqa: E501
            collection_formats['print_id'] = 'multi'  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
            collection_formats['status'] = 'multi'  # noqa: E501
        if 'print_order_number' in local_var_params and local_var_params['print_order_number'] is not None:  # noqa: E501
            query_params.append(('print_order_number', local_var_params['print_order_number']))  # noqa: E501
            collection_formats['print_order_number'] = 'multi'  # noqa: E501
        if 'print_order_uuid' in local_var_params and local_var_params['print_order_uuid'] is not None:  # noqa: E501
            query_params.append(('print_order_uuid', local_var_params['print_order_uuid']))  # noqa: E501
            collection_formats['print_order_uuid'] = 'multi'  # noqa: E501
        if 'printer_serial' in local_var_params and local_var_params['printer_serial'] is not None:  # noqa: E501
            query_params.append(('printer_serial', local_var_params['printer_serial']))  # noqa: E501
            collection_formats['printer_serial'] = 'multi'  # noqa: E501
        if 'build_uuid' in local_var_params and local_var_params['build_uuid'] is not None:  # noqa: E501
            query_params.append(('build_uuid', local_var_params['build_uuid']))  # noqa: E501
            collection_formats['build_uuid'] = 'multi'  # noqa: E501
        if 'printer_name' in local_var_params and local_var_params['printer_name'] is not None:  # noqa: E501
            query_params.append(('printer_name', local_var_params['printer_name']))  # noqa: E501
            collection_formats['printer_name'] = 'multi'  # noqa: E501
        if 'platform_serial' in local_var_params and local_var_params['platform_serial'] is not None:  # noqa: E501
            query_params.append(('platform_serial', local_var_params['platform_serial']))  # noqa: E501
            collection_formats['platform_serial'] = 'multi'  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/prints', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrintsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
