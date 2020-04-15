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
configuration = carbon3d.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.carbon3d.com/v1
configuration.host = "https://api.carbon3d.com/v1"

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

