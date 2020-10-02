# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.5
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


class BuildsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_build(self, uuid, **kwargs):  # noqa: E501
        """Fetch a build  # noqa: E501

        Gets the details of a single build.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: Build Uuid (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_build_with_http_info(uuid, **kwargs)  # noqa: E501

    def get_build_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Fetch a build  # noqa: E501

        Gets the details of a single build.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uuid: Build Uuid (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Build, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_build" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uuid` when calling `get_build`")  # noqa: E501

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
            '/builds/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Build',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_builds(self, limit, **kwargs):  # noqa: E501
        """Fetch builds  # noqa: E501

        Fetch a list of `build` entities (most recent first)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_builds(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param str cursor: Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d)
        :param int offset: Number of items to skip
        :param list[str] uuid: An array of UUIDs
        :param list[int] application_id: An array of Application IDs
        :param datetime updated_before: Updated before time X
        :param datetime updated_after: Updated after time X
        :param datetime created_before: Select build with creation date prior to param
        :param datetime created_after: Select build with creation date after param
        :param list[str] name: An array of build names
        :param list[str] revision: An array of build revisions
        :param str status: Status of the build
        :param list[str] sort: Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `build_uuid`, `updated_at`, `status`, `created_at`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BuildsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_builds_with_http_info(limit, **kwargs)  # noqa: E501

    def get_builds_with_http_info(self, limit, **kwargs):  # noqa: E501
        """Fetch builds  # noqa: E501

        Fetch a list of `build` entities (most recent first)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_builds_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param str cursor: Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d)
        :param int offset: Number of items to skip
        :param list[str] uuid: An array of UUIDs
        :param list[int] application_id: An array of Application IDs
        :param datetime updated_before: Updated before time X
        :param datetime updated_after: Updated after time X
        :param datetime created_before: Select build with creation date prior to param
        :param datetime created_after: Select build with creation date after param
        :param list[str] name: An array of build names
        :param list[str] revision: An array of build revisions
        :param str status: Status of the build
        :param list[str] sort: Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `build_uuid`, `updated_at`, `status`, `created_at`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BuildsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'cursor',
            'offset',
            'uuid',
            'application_id',
            'updated_before',
            'updated_after',
            'created_before',
            'created_after',
            'name',
            'revision',
            'status',
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
                    " to method get_builds" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'limit' is set
        if self.api_client.client_side_validation and ('limit' not in local_var_params or  # noqa: E501
                                                        local_var_params['limit'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `limit` when calling `get_builds`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_builds`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_builds`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_builds`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `get_builds`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `get_builds`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('application_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['application_id']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `application_id` when calling `get_builds`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('application_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['application_id']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `application_id` when calling `get_builds`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['name']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `name` when calling `get_builds`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `name` when calling `get_builds`, number of items must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('revision' in local_var_params and  # noqa: E501
                                                        len(local_var_params['revision']) > 100):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `revision` when calling `get_builds`, number of items must be less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('revision' in local_var_params and  # noqa: E501
                                                        len(local_var_params['revision']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `revision` when calling `get_builds`, number of items must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
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
        if 'created_before' in local_var_params and local_var_params['created_before'] is not None:  # noqa: E501
            query_params.append(('created_before', local_var_params['created_before']))  # noqa: E501
        if 'created_after' in local_var_params and local_var_params['created_after'] is not None:  # noqa: E501
            query_params.append(('created_after', local_var_params['created_after']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
            collection_formats['name'] = 'multi'  # noqa: E501
        if 'revision' in local_var_params and local_var_params['revision'] is not None:  # noqa: E501
            query_params.append(('revision', local_var_params['revision']))  # noqa: E501
            collection_formats['revision'] = 'multi'  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
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
            '/builds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BuildsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
