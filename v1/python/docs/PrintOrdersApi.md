# carbon3d.PrintOrdersApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_print_order**](PrintOrdersApi.md#create_print_order) | **POST** /print_orders | Create a PrintOrder
[**get_print_order**](PrintOrdersApi.md#get_print_order) | **GET** /print_orders/{uuid} | Get a PrintOrder
[**get_print_orders**](PrintOrdersApi.md#get_print_orders) | **GET** /print_orders | Fetch print orders
[**update_print_order**](PrintOrdersApi.md#update_print_order) | **PATCH** /print_orders/{uuid} | Update a PrintOrder


# **create_print_order**
> PrintOrder create_print_order(print_order_request=print_order_request)

Create a PrintOrder

Creates a new PrintOrder.

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
    api_instance = carbon3d.PrintOrdersApi(api_client)
    print_order_request = carbon3d.PrintOrderRequest() # PrintOrderRequest | A new PrintOrder to be created. (optional)

    try:
        # Create a PrintOrder
        api_response = api_instance.create_print_order(print_order_request=print_order_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintOrdersApi->create_print_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_order_request** | [**PrintOrderRequest**](PrintOrderRequest.md)| A new PrintOrder to be created. | [optional] 

### Return type

[**PrintOrder**](PrintOrder.md)

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

# **get_print_order**
> PrintOrder get_print_order(uuid)

Get a PrintOrder

Gets the details of a single PrintOrder.

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
    api_instance = carbon3d.PrintOrdersApi(api_client)
    uuid = 'uuid_example' # str | Carbon-generated print order UUID

    try:
        # Get a PrintOrder
        api_response = api_instance.get_print_order(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintOrdersApi->get_print_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Carbon-generated print order UUID | 

### Return type

[**PrintOrder**](PrintOrder.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The print order does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_print_orders**
> PrintOrdersResponse get_print_orders(limit, offset, print_order_number=print_order_number)

Fetch print orders

Fetch a list of `PrintOrder` entities (most recent first)

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
    api_instance = carbon3d.PrintOrdersApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)
print_order_number = 'print_order_number_example' # str | Customer-provided print order number (optional)

    try:
        # Fetch print orders
        api_response = api_instance.get_print_orders(limit, offset, print_order_number=print_order_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintOrdersApi->get_print_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **offset** | **int**| Number of items to skip | [default to 0]
 **print_order_number** | **str**| Customer-provided print order number | [optional] 

### Return type

[**PrintOrdersResponse**](PrintOrdersResponse.md)

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

# **update_print_order**
> PrintOrder update_print_order(uuid, print_order_update_request=print_order_update_request)

Update a PrintOrder

Updates information associated with a single PrintOrder.

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
    api_instance = carbon3d.PrintOrdersApi(api_client)
    uuid = 'uuid_example' # str | Carbon-generated print order UUID
print_order_update_request = carbon3d.PrintOrderUpdateRequest() # PrintOrderUpdateRequest | Update an existing PrintOrder. (optional)

    try:
        # Update a PrintOrder
        api_response = api_instance.update_print_order(uuid, print_order_update_request=print_order_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintOrdersApi->update_print_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Carbon-generated print order UUID | 
 **print_order_update_request** | [**PrintOrderUpdateRequest**](PrintOrderUpdateRequest.md)| Update an existing PrintOrder. | [optional] 

### Return type

[**PrintOrder**](PrintOrder.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The print order does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

