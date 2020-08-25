# carbon3d.BuildsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build**](BuildsApi.md#get_build) | **GET** /builds/{uuid} | Fetch a build
[**get_builds**](BuildsApi.md#get_builds) | **GET** /builds | Fetch builds


# **get_build**
> Build get_build(uuid)

Fetch a build

Gets the details of a single build.

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
    api_instance = carbon3d.BuildsApi(api_client)
    uuid = 'uuid_example' # str | Build Uuid

    try:
        # Fetch a build
        api_response = api_instance.get_build(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildsApi->get_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Build Uuid | 

### Return type

[**Build**](Build.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The build does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds**
> BuildsResponse get_builds(limit, offset, name=name, revision=revision, status=status, created_before=created_before, created_after=created_after)

Fetch builds

Fetch a list of `build` entities (most recent first)

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
    api_instance = carbon3d.BuildsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)
name = ['name_example'] # list[str] | An array of build names (optional)
revision = ['revision_example'] # list[str] | An array of build revisions (optional)
status = 'status_example' # str | Status of the build (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Select build with creation date prior to param (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Select build with creation date after param (optional)

    try:
        # Fetch builds
        api_response = api_instance.get_builds(limit, offset, name=name, revision=revision, status=status, created_before=created_before, created_after=created_after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildsApi->get_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **offset** | **int**| Number of items to skip | [default to 0]
 **name** | [**list[str]**](str.md)| An array of build names | [optional] 
 **revision** | [**list[str]**](str.md)| An array of build revisions | [optional] 
 **status** | **str**| Status of the build | [optional] 
 **created_before** | **datetime**| Select build with creation date prior to param | [optional] 
 **created_after** | **datetime**| Select build with creation date after param | [optional] 

### Return type

[**BuildsResponse**](BuildsResponse.md)

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

