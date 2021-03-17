# carbon3d.PartsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_part**](PartsApi.md#create_part) | **POST** /parts | Create a Part
[**get_part**](PartsApi.md#get_part) | **GET** /parts/{uuid} | Fetch a Part
[**get_parts**](PartsApi.md#get_parts) | **GET** /parts | Fetch parts


# **create_part**
> Part create_part(part_request=part_request)

Create a Part

Create a part from a model.

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
    api_instance = carbon3d.PartsApi(api_client)
    part_request = carbon3d.PartRequest() # PartRequest | A new Part to be created. (optional)

    try:
        # Create a Part
        api_response = api_instance.create_part(part_request=part_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartsApi->create_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_request** | [**PartRequest**](PartRequest.md)| A new Part to be created. | [optional] 

### Return type

[**Part**](Part.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_part**
> Part get_part(uuid)

Fetch a Part

Fetch the details of a single Part.

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
    api_instance = carbon3d.PartsApi(api_client)
    uuid = 'uuid_example' # str | A unique identifier for a Part.

    try:
        # Fetch a Part
        api_response = api_instance.get_part(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartsApi->get_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A unique identifier for a Part. | 

### Return type

[**Part**](Part.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The part does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parts**
> PartsResponse get_parts(limit, cursor=cursor, uuid=uuid, application_uuid=application_uuid, updated_before=updated_before, updated_after=updated_after, model_uuid=model_uuid, sort=sort)

Fetch parts

Gets a list of `Part` entities (most recent first)

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
    api_instance = carbon3d.PartsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
cursor = '' # str | Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d) (optional) (default to '')
uuid = ['uuid_example'] # list[str] | An array of UUIDs (optional)
application_uuid = ['application_uuid_example'] # list[str] | An array of Application UUIDs (optional)
updated_before = '2013-10-20T19:20:30+01:00' # datetime | Updated before timestamp (exclusive) (optional)
updated_after = '2013-10-20T19:20:30+01:00' # datetime | Updated at or after timestamp (inclusive) (optional)
model_uuid = ['model_uuid_example'] # list[str] | A model_uuid or array of model_uuids (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `updated_at`, `part_number`, `model_uuid` (optional)

    try:
        # Fetch parts
        api_response = api_instance.get_parts(limit, cursor=cursor, uuid=uuid, application_uuid=application_uuid, updated_before=updated_before, updated_after=updated_after, model_uuid=model_uuid, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartsApi->get_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **cursor** | **str**| Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ&#x3D;d) | [optional] [default to &#39;&#39;]
 **uuid** | [**list[str]**](str.md)| An array of UUIDs | [optional] 
 **application_uuid** | [**list[str]**](str.md)| An array of Application UUIDs | [optional] 
 **updated_before** | **datetime**| Updated before timestamp (exclusive) | [optional] 
 **updated_after** | **datetime**| Updated at or after timestamp (inclusive) | [optional] 
 **model_uuid** | [**list[str]**](str.md)| A model_uuid or array of model_uuids | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. Sortable fields are: &#x60;uuid&#x60;, &#x60;updated_at&#x60;, &#x60;part_number&#x60;, &#x60;model_uuid&#x60; | [optional] 

### Return type

[**PartsResponse**](PartsResponse.md)

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

