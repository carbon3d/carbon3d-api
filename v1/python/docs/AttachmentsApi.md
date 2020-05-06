# carbon3d.AttachmentsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /attachments/{uuid} | Download a file attachment


# **get_attachment**
> get_attachment(uuid)

Download a file attachment

Downloads a single file attachment.

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
    api_instance = carbon3d.AttachmentsApi(api_client)
    uuid = 'uuid_example' # str | Attachment Uuid

    try:
        # Download a file attachment
        api_instance.get_attachment(uuid)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Attachment Uuid | 

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
**302** | Expected response to be a redirect to the file |  -  |
**404** | The file does not exist or can&#39;t be accessed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

