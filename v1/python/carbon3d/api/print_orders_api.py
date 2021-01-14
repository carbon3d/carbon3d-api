# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.4
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


class PrintOrdersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_print_order(self, **kwargs):  # noqa: E501
        """Create a PrintOrder  # noqa: E501

        Creates a new PrintOrder.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_print_order(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param PrintOrderRequest print_order_request: A new PrintOrder to be created.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PrintOrder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_print_order_with_http_info(**kwargs)  # noqa: E501

    def create_print_order_with_http_info(self, **kwargs):  # noqa: E501
        """Create a PrintOrder  # noqa: E501

        Creates a new PrintOrder.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_print_order_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param PrintOrderRequest print_order_request: A new PrintOrder to be created.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PrintOrder, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'print_order_request'
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
                    " to method create_print_order" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'print_order_request' in local_var_params:
            body_params = local_var_params['print_order_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/print_orders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrintOrder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_print_order(self, uuid, **kwargs):  # noqa: E501
        """Get a PrintOrder  # noqa: E501

        Gets the details of a single PrintOrder.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_print_order(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: Carbon-generated print order UUID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PrintOrder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_print_order_with_http_info(uuid, **kwargs)  # noqa: E501

    def get_print_order_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Get a PrintOrder  # noqa: E501

        Gets the details of a single PrintOrder.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_print_order_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: Carbon-generated print order UUID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PrintOrder, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'uuid'
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
                    " to method get_print_order" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uuid` when calling `get_print_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []

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
            '/print_orders/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrintOrder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_print_orders(self, limit, **kwargs):  # noqa: E501
        """Fetch print orders  # noqa: E501

        Fetch a list of `PrintOrder` entities (most recent first)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_print_orders(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param str cursor: Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d)
        :param list[str] uuid: An array of UUIDs
        :param list[int] application_id: An array of Application IDs
        :param datetime updated_before: Updated before timestamp (exclusive)
        :param datetime updated_after: Updated at or after timestamp (inclusive)
        :param list[str] print_order_number: Customer-provided print order number
        :param list[str] printer_serial: An array of serials of the Printer(s) used to print
        :param list[str] printer_name: An array of names of the Printer(s) used to print
        :param list[str] sort: Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `updated_at`, `print_order_number`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PrintOrdersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_print_orders_with_http_info(limit, **kwargs)  # noqa: E501

    def get_print_orders_with_http_info(self, limit, **kwargs):  # noqa: E501
        """Fetch print orders  # noqa: E501

        Fetch a list of `PrintOrder` entities (most recent first)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_print_orders_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param str cursor: Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d)
        :param list[str] uuid: An array of UUIDs
        :param list[int] application_id: An array of Application IDs
        :param datetime updated_before: Updated before timestamp (exclusive)
        :param datetime updated_after: Updated at or after timestamp (inclusive)
        :param list[str] print_order_number: Customer-provided print order number
        :param list[str] printer_serial: An array of serials of the Printer(s) used to print
        :param list[str] printer_name: An array of names of the Printer(s) used to print
        :param list[str] sort: Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `updated_at`, `print_order_number`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PrintOrdersResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'cursor',
            'uuid',
            'application_id',
            'updated_before',
            'updated_after',
            'print_order_number',
            'printer_serial',
            'printer_name',
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
                    " to method get_print_orders" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'limit' is set
        if self.api_client.client_side_validation and ('limit' not in local_var_params or  # noqa: E501
                                                        local_var_params['limit'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `limit` when calling `get_print_orders`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_print_orders`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_print_orders`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `get_print_orders`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `get_print_orders`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('application_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['application_id']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `application_id` when calling `get_print_orders`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('application_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['application_id']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `application_id` when calling `get_print_orders`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('print_order_number' in local_var_params and  # noqa: E501
                                                        len(local_var_params['print_order_number']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `print_order_number` when calling `get_print_orders`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('print_order_number' in local_var_params and  # noqa: E501
                                                        len(local_var_params['print_order_number']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `print_order_number` when calling `get_print_orders`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('printer_serial' in local_var_params and  # noqa: E501
                                                        len(local_var_params['printer_serial']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `printer_serial` when calling `get_print_orders`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('printer_serial' in local_var_params and  # noqa: E501
                                                        len(local_var_params['printer_serial']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `printer_serial` when calling `get_print_orders`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('printer_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['printer_name']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `printer_name` when calling `get_print_orders`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('printer_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['printer_name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `printer_name` when calling `get_print_orders`, number of items must be greater than or equal to `1`")  # noqa: E501
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
        if 'application_id' in local_var_params and local_var_params['application_id'] is not None:  # noqa: E501
            query_params.append(('application_id', local_var_params['application_id']))  # noqa: E501
            collection_formats['application_id'] = 'multi'  # noqa: E501
        if 'updated_before' in local_var_params and local_var_params['updated_before'] is not None:  # noqa: E501
            query_params.append(('updated_before', local_var_params['updated_before']))  # noqa: E501
        if 'updated_after' in local_var_params and local_var_params['updated_after'] is not None:  # noqa: E501
            query_params.append(('updated_after', local_var_params['updated_after']))  # noqa: E501
        if 'print_order_number' in local_var_params and local_var_params['print_order_number'] is not None:  # noqa: E501
            query_params.append(('print_order_number', local_var_params['print_order_number']))  # noqa: E501
            collection_formats['print_order_number'] = 'multi'  # noqa: E501
        if 'printer_serial' in local_var_params and local_var_params['printer_serial'] is not None:  # noqa: E501
            query_params.append(('printer_serial', local_var_params['printer_serial']))  # noqa: E501
            collection_formats['printer_serial'] = 'multi'  # noqa: E501
        if 'printer_name' in local_var_params and local_var_params['printer_name'] is not None:  # noqa: E501
            query_params.append(('printer_name', local_var_params['printer_name']))  # noqa: E501
            collection_formats['printer_name'] = 'multi'  # noqa: E501
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
            '/print_orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrintOrdersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_print_order(self, uuid, **kwargs):  # noqa: E501
        """Update a PrintOrder  # noqa: E501

        Updates information associated with a single PrintOrder.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_print_order(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: Carbon-generated print order UUID (required)
        :param PrintOrderUpdateRequest print_order_update_request: Update an existing PrintOrder.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PrintOrder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_print_order_with_http_info(uuid, **kwargs)  # noqa: E501

    def update_print_order_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Update a PrintOrder  # noqa: E501

        Updates information associated with a single PrintOrder.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_print_order_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: Carbon-generated print order UUID (required)
        :param PrintOrderUpdateRequest print_order_update_request: Update an existing PrintOrder.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PrintOrder, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'uuid',
            'print_order_update_request'
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
                    " to method update_print_order" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uuid` when calling `update_print_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'print_order_update_request' in local_var_params:
            body_params = local_var_params['print_order_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/print_orders/{uuid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrintOrder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
