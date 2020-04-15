# carbon3d.PrintsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prints**](PrintsApi.md#get_prints) | **GET** /prints | List finished prints information


# **get_prints**
> PrintsResponse get_prints(limit, offset, platform_serial=platform_serial)

List finished prints information

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

# Defining host is optional and default to https://api.carbon3d.com/v1
configuration.host = "https://api.carbon3d.com/v1"

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PrintsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)
platform_serial = 'platform_serial_example' # str | Platform used for print (optional)

    try:
        # List finished prints information
        api_response = api_instance.get_prints(limit, offset, platform_serial=platform_serial)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintsApi->get_prints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **offset** | **int**| Number of items to skip | [default to 0]
 **platform_serial** | **str**| Platform used for print | [optional] 

### Return type

[**PrintsResponse**](PrintsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

