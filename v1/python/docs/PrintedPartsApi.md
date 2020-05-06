# carbon3d.PrintedPartsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_printed_part**](PrintedPartsApi.md#get_printed_part) | **GET** /printed_parts/{uuid} | Fetch a printed Part
[**get_printed_parts**](PrintedPartsApi.md#get_printed_parts) | **GET** /printed_parts | Fetch printed parts


# **get_printed_part**
> PrintedPart get_printed_part(uuid)

Fetch a printed Part

Fetch the details of a single PrintedPart.

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
    api_instance = carbon3d.PrintedPartsApi(api_client)
    uuid = 'uuid_example' # str | A unique identifier for a PrintedPart.

    try:
        # Fetch a printed Part
        api_response = api_instance.get_printed_part(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintedPartsApi->get_printed_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A unique identifier for a PrintedPart. | 

### Return type

[**PrintedPart**](PrintedPart.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The printed part does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_printed_parts**
> PrintedPartsResponse get_printed_parts(limit, offset, status=status, order_uuid=order_uuid, part_uuid=part_uuid, order_number=order_number, sort=sort)

Fetch printed parts

Gets a list of Part entities (most recent first)

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
    api_instance = carbon3d.PrintedPartsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)
status = carbon3d.PrintedPartStatus() # PrintedPartStatus | Current printed part status (optional)
order_uuid = 'order_uuid_example' # str | Order UUID (optional)
part_uuid = 'part_uuid_example' # str | Part UUID (optional)
order_number = 'order_number_example' # str | Customer-provided order number the printed parts belong to (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. (optional)

    try:
        # Fetch printed parts
        api_response = api_instance.get_printed_parts(limit, offset, status=status, order_uuid=order_uuid, part_uuid=part_uuid, order_number=order_number, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintedPartsApi->get_printed_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **offset** | **int**| Number of items to skip | [default to 0]
 **status** | [**PrintedPartStatus**](.md)| Current printed part status | [optional] 
 **order_uuid** | **str**| Order UUID | [optional] 
 **part_uuid** | **str**| Part UUID | [optional] 
 **order_number** | **str**| Customer-provided order number the printed parts belong to | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. | [optional] 

### Return type

[**PrintedPartsResponse**](PrintedPartsResponse.md)

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

