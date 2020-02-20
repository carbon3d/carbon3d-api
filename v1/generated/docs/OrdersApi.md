# carbon3d.OrdersApi

All URIs are relative to *https://api-sandbox.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](OrdersApi.md#create_order) | **POST** /orders | Create an Order
[**delete_order**](OrdersApi.md#delete_order) | **DELETE** /orders/{uuid} | Cancel an Order
[**get_order**](OrdersApi.md#get_order) | **GET** /orders/{uuid} | Get an Order
[**get_orders**](OrdersApi.md#get_orders) | **GET** /orders | Fetch orders


# **create_order**
> Order create_order(order_request=order_request)

Create an Order

Creates a new Order.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
configuration = carbon3d.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-sandbox.carbon3d.com/v1
configuration.host = "https://api-sandbox.carbon3d.com/v1"
# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.OrdersApi(api_client)
    order_request = carbon3d.OrderRequest() # OrderRequest | A new Order to be created. (optional)

    try:
        # Create an Order
        api_response = api_instance.create_order(order_request=order_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_request** | [**OrderRequest**](OrderRequest.md)| A new Order to be created. | [optional] 

### Return type

[**Order**](Order.md)

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

# **delete_order**
> delete_order(uuid)

Cancel an Order

Cancel an existing eligible Order. Orders may only be canceled while they are in 'open' status. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
configuration = carbon3d.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-sandbox.carbon3d.com/v1
configuration.host = "https://api-sandbox.carbon3d.com/v1"
# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.OrdersApi(api_client)
    uuid = 'uuid_example' # str | Carbon-generated order UUID

    try:
        # Cancel an Order
        api_instance.delete_order(uuid)
    except ApiException as e:
        print("Exception when calling OrdersApi->delete_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Carbon-generated order UUID | 

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
**405** | Order cannot be canceled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(uuid)

Get an Order

Gets the details of a single Order.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
configuration = carbon3d.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-sandbox.carbon3d.com/v1
configuration.host = "https://api-sandbox.carbon3d.com/v1"
# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.OrdersApi(api_client)
    uuid = 'uuid_example' # str | Carbon-generated order UUID

    try:
        # Get an Order
        api_response = api_instance.get_order(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Carbon-generated order UUID | 

### Return type

[**Order**](Order.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The order does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> OrdersResponse get_orders(limit, offset, status=status, order_number=order_number, sort=sort)

Fetch orders

Fetch a list of `Order` entities (most recent first)

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
configuration = carbon3d.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-sandbox.carbon3d.com/v1
configuration.host = "https://api-sandbox.carbon3d.com/v1"
# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.OrdersApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)
status = carbon3d.OrderStatus() # OrderStatus | Order status (optional)
order_number = 'order_number_example' # str | Customer-provided order number (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. (optional)

    try:
        # Fetch orders
        api_response = api_instance.get_orders(limit, offset, status=status, order_number=order_number, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **offset** | **int**| Number of items to skip | [default to 0]
 **status** | [**OrderStatus**](.md)| Order status | [optional] 
 **order_number** | **str**| Customer-provided order number | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. | [optional] 

### Return type

[**OrdersResponse**](OrdersResponse.md)

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
