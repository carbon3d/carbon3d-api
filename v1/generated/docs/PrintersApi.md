# carbon3d.PrintersApi

All URIs are relative to *https://api-sandbox.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_printer**](PrintersApi.md#get_printer) | **GET** /printers/{name} | Fetch a specific printer&#39;s status information
[**get_printers**](PrintersApi.md#get_printers) | **GET** /printers | Fetch all printer&#39;s status information


# **get_printer**
> Printer get_printer(name)

Fetch a specific printer's status information

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
    api_instance = carbon3d.PrintersApi(api_client)
    name = 'name_example' # str | e.g. L1001

    try:
        # Fetch a specific printer's status information
        api_response = api_instance.get_printer(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintersApi->get_printer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| e.g. L1001 | 

### Return type

[**Printer**](Printer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | Invalid printer name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_printers**
> PrintersResponse get_printers(limit, offset)

Fetch all printer's status information

Fetch all printers and their relevant attached information like status and sliding print window (past/current/next). Sorted by name, ascending.

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
    api_instance = carbon3d.PrintersApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)

    try:
        # Fetch all printer's status information
        api_response = api_instance.get_printers(limit, offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintersApi->get_printers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **offset** | **int**| Number of items to skip | [default to 0]

### Return type

[**PrintersResponse**](PrintersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | No printer was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

