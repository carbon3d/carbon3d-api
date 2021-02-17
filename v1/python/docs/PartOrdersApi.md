# carbon3d.PartOrdersApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_part_order**](PartOrdersApi.md#create_part_order) | **POST** /part_orders | Create a PartOrder
[**delete_part_order**](PartOrdersApi.md#delete_part_order) | **DELETE** /part_orders/{uuid} | Cancel a PartOrder
[**get_part_order**](PartOrdersApi.md#get_part_order) | **GET** /part_orders/{uuid} | Get a PartOrder
[**get_part_orders**](PartOrdersApi.md#get_part_orders) | **GET** /part_orders | Fetch part orders
[**update_part_order**](PartOrdersApi.md#update_part_order) | **PATCH** /part_orders/{uuid} | Update a PartOrder


# **create_part_order**
> PartOrder create_part_order(part_order_request=part_order_request)

Create a PartOrder

Creates a new PartOrder.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.carbon3d.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = carbon3d.Configuration(
    host = "https://api.carbon3d.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = carbon3d.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PartOrdersApi(api_client)
    part_order_request = carbon3d.PartOrderRequest() # PartOrderRequest | A new PartOrder to be created. (optional)

    try:
        # Create a PartOrder
        api_response = api_instance.create_part_order(part_order_request=part_order_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartOrdersApi->create_part_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_order_request** | [**PartOrderRequest**](PartOrderRequest.md)| A new PartOrder to be created. | [optional] 

### Return type

[**PartOrder**](PartOrder.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_part_order**
> delete_part_order(uuid)

Cancel a PartOrder

Cancel an existing eligible PartOrder. Part orders may only be canceled while they are in 'open' status. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.carbon3d.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = carbon3d.Configuration(
    host = "https://api.carbon3d.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = carbon3d.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PartOrdersApi(api_client)
    uuid = 'uuid_example' # str | Carbon-generated part order UUID

    try:
        # Cancel a PartOrder
        api_instance.delete_part_order(uuid)
    except ApiException as e:
        print("Exception when calling PartOrdersApi->delete_part_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Carbon-generated part order UUID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Expected response to a valid request |  -  |
**400** | Invalid input |  -  |
**405** | PartOrder cannot be canceled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_part_order**
> PartOrder get_part_order(uuid)

Get a PartOrder

Gets the details of a single PartOrder.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.carbon3d.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = carbon3d.Configuration(
    host = "https://api.carbon3d.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = carbon3d.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PartOrdersApi(api_client)
    uuid = 'uuid_example' # str | Carbon-generated part order UUID

    try:
        # Get a PartOrder
        api_response = api_instance.get_part_order(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartOrdersApi->get_part_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Carbon-generated part order UUID | 

### Return type

[**PartOrder**](PartOrder.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The part order does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_part_orders**
> PartOrdersResponse get_part_orders(limit, cursor=cursor, uuid=uuid, application_id=application_id, application_uuid=application_uuid, updated_before=updated_before, updated_after=updated_after, status=status, part_order_number=part_order_number, sort=sort)

Fetch part orders

Fetch a list of `PartOrder` entities (most recent first)

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.carbon3d.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = carbon3d.Configuration(
    host = "https://api.carbon3d.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = carbon3d.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PartOrdersApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
cursor = '' # str | Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d) (optional) (default to '')
uuid = ['uuid_example'] # list[str] | An array of UUIDs (optional)
application_id = [56] # list[int] | An array of Application IDs (optional)
application_uuid = ['application_uuid_example'] # list[str] | An array of Application UUIDs (optional)
updated_before = '2013-10-20T19:20:30+01:00' # datetime | Updated before timestamp (exclusive) (optional)
updated_after = '2013-10-20T19:20:30+01:00' # datetime | Updated at or after timestamp (inclusive) (optional)
status = carbon3d.PartOrderStatus() # PartOrderStatus | PartOrder status (optional)
part_order_number = 'part_order_number_example' # str | Customer-provided part order number (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `updated_at`, `part_order_number`, `due_date`, `flushed_at` (optional)

    try:
        # Fetch part orders
        api_response = api_instance.get_part_orders(limit, cursor=cursor, uuid=uuid, application_id=application_id, application_uuid=application_uuid, updated_before=updated_before, updated_after=updated_after, status=status, part_order_number=part_order_number, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartOrdersApi->get_part_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **cursor** | **str**| Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ&#x3D;d) | [optional] [default to &#39;&#39;]
 **uuid** | [**list[str]**](str.md)| An array of UUIDs | [optional] 
 **application_id** | [**list[int]**](int.md)| An array of Application IDs | [optional] 
 **application_uuid** | [**list[str]**](str.md)| An array of Application UUIDs | [optional] 
 **updated_before** | **datetime**| Updated before timestamp (exclusive) | [optional] 
 **updated_after** | **datetime**| Updated at or after timestamp (inclusive) | [optional] 
 **status** | [**PartOrderStatus**](.md)| PartOrder status | [optional] 
 **part_order_number** | **str**| Customer-provided part order number | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. Sortable fields are: &#x60;uuid&#x60;, &#x60;updated_at&#x60;, &#x60;part_order_number&#x60;, &#x60;due_date&#x60;, &#x60;flushed_at&#x60; | [optional] 

### Return type

[**PartOrdersResponse**](PartOrdersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_part_order**
> PartOrder update_part_order(uuid, part_order_update_request=part_order_update_request)

Update a PartOrder

Updates parts of a single PartOrder.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.carbon3d.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = carbon3d.Configuration(
    host = "https://api.carbon3d.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = carbon3d.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PartOrdersApi(api_client)
    uuid = 'uuid_example' # str | Carbon-generated part order UUID
part_order_update_request = carbon3d.PartOrderUpdateRequest() # PartOrderUpdateRequest | Update an existing PartOrder. (optional)

    try:
        # Update a PartOrder
        api_response = api_instance.update_part_order(uuid, part_order_update_request=part_order_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartOrdersApi->update_part_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Carbon-generated part order UUID | 
 **part_order_update_request** | [**PartOrderUpdateRequest**](PartOrderUpdateRequest.md)| Update an existing PartOrder. | [optional] 

### Return type

[**PartOrder**](PartOrder.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The part order does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

