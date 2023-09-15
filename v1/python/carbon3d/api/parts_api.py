# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.10
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


class PartsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_part(self, **kwargs):  # noqa: E501
        """Create a Part  # noqa: E501

        Create a part from a model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_part(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param PartRequest part_request: A new Part to be created.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Part
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_part_with_http_info(**kwargs)  # noqa: E501

    def create_part_with_http_info(self, **kwargs):  # noqa: E501
        """Create a Part  # noqa: E501

        Create a part from a model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_part_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param PartRequest part_request: A new Part to be created.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Part, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'part_request'
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
                    " to method create_part" % key
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
        if 'part_request' in local_var_params:
            body_params = local_var_params['part_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/parts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Part',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_part(self, uuid, **kwargs):  # noqa: E501
        """Fetch a Part  # noqa: E501

        Fetch the details of a single Part.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_part(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: A unique identifier for a Part. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Part
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_part_with_http_info(uuid, **kwargs)  # noqa: E501

    def get_part_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Fetch a Part  # noqa: E501

        Fetch the details of a single Part.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_part_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: A unique identifier for a Part. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Part, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_part" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uuid` when calling `get_part`")  # noqa: E501

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
            '/parts/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Part',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_parts(self, limit, **kwargs):  # noqa: E501
        """Fetch parts  # noqa: E501

        Gets a list of `Part` entities (most recent first)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parts(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param str cursor: Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d)
        :param list[str] uuid: An array of UUIDs
        :param list[str] application_uuid: An array of Application UUIDs
        :param datetime updated_before: Updated before timestamp (exclusive)
        :param datetime updated_after: Updated at or after timestamp (inclusive)
        :param list[str] model_uuid: A model_uuid or array of model_uuids
        :param list[str] sort: Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `updated_at`, `part_number`, `model_uuid`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PartsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_parts_with_http_info(limit, **kwargs)  # noqa: E501

    def get_parts_with_http_info(self, limit, **kwargs):  # noqa: E501
        """Fetch parts  # noqa: E501

        Gets a list of `Part` entities (most recent first)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parts_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param str cursor: Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d)
        :param list[str] uuid: An array of UUIDs
        :param list[str] application_uuid: An array of Application UUIDs
        :param datetime updated_before: Updated before timestamp (exclusive)
        :param datetime updated_after: Updated at or after timestamp (inclusive)
        :param list[str] model_uuid: A model_uuid or array of model_uuids
        :param list[str] sort: Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `updated_at`, `part_number`, `model_uuid`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PartsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'cursor',
            'uuid',
            'application_uuid',
            'updated_before',
            'updated_after',
            'model_uuid',
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
                    " to method get_parts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'limit' is set
        if self.api_client.client_side_validation and ('limit' not in local_var_params or  # noqa: E501
                                                        local_var_params['limit'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `limit` when calling `get_parts`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_parts`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_parts`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `get_parts`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `get_parts`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('application_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['application_uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `application_uuid` when calling `get_parts`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('application_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['application_uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `application_uuid` when calling `get_parts`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('model_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['model_uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `model_uuid` when calling `get_parts`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('model_uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['model_uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `model_uuid` when calling `get_parts`, number of items must be greater than or equal to `1`")  # noqa: E501
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
        if 'updated_before' in local_var_params and local_var_params['updated_before'] is not None:  # noqa: E501
            query_params.append(('updated_before', local_var_params['updated_before']))  # noqa: E501
        if 'updated_after' in local_var_params and local_var_params['updated_after'] is not None:  # noqa: E501
            query_params.append(('updated_after', local_var_params['updated_after']))  # noqa: E501
        if 'model_uuid' in local_var_params and local_var_params['model_uuid'] is not None:  # noqa: E501
            query_params.append(('model_uuid', local_var_params['model_uuid']))  # noqa: E501
            collection_formats['model_uuid'] = 'multi'  # noqa: E501
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
            '/parts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PartsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
