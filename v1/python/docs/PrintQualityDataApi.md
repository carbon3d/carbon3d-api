# carbon3d.PrintQualityDataApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_print_quality_data**](PrintQualityDataApi.md#get_print_quality_data) | **GET** /print_quality_data | List finished print&#39;s quality metrics


# **get_print_quality_data**
> PrintsDataQAResponse get_print_quality_data(print_ids)

List finished print's quality metrics

List quality assurance data for prints

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
    api_instance = carbon3d.PrintQualityDataApi(api_client)
    print_ids = ['print_ids_example'] # list[str] | Print ID

    try:
        # List finished print's quality metrics
        api_response = api_instance.get_print_quality_data(print_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintQualityDataApi->get_print_quality_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_ids** | [**list[str]**](str.md)| Print ID | 

### Return type

[**PrintsDataQAResponse**](PrintsDataQAResponse.md)

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

