# carbon3d.QueuesApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_printer_queues**](QueuesApi.md#get_printer_queues) | **GET** /printers/queues | Fetch all printers&#39; queues
[**update_printer_queue**](QueuesApi.md#update_printer_queue) | **PATCH** /printers/queues | Update a Printer queue


# **get_printer_queues**
> PrinterQueuesResponse get_printer_queues(printer_serial=printer_serial)

Fetch all printers' queues

Fetch all printers and their queues. Sorted in queue order (first queue item will print next).

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
    api_instance = carbon3d.QueuesApi(api_client)
    printer_serial = ['printer_serial_example'] # list[str] | Array of printer serials to limit the query (optional)

    try:
        # Fetch all printers' queues
        api_response = api_instance.get_printer_queues(printer_serial=printer_serial)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueuesApi->get_printer_queues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printer_serial** | [**list[str]**](str.md)| Array of printer serials to limit the query | [optional] 

### Return type

[**PrinterQueuesResponse**](PrinterQueuesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | No printer or queues were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_printer_queue**
> PrinterQueueUpdateResponse update_printer_queue(unknown_base_type=unknown_base_type)

Update a Printer queue

Updates queue(s) tied to print_uuids passed in request

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
    api_instance = carbon3d.QueuesApi(api_client)
    unknown_base_type = {"action_type":"PrinterQueueMoveRequest","printer_serial":"123","print_uuids":["edb4304f-1323-5d3d-9a87-2a0febc91948","abc4303f-9a87-5d3d-1323-2a0febc12345"],"index":0} # UNKNOWN_BASE_TYPE | An update operation to a printer queue. (optional)

    try:
        # Update a Printer queue
        api_response = api_instance.update_printer_queue(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueuesApi->update_printer_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| An update operation to a printer queue. | [optional] 

### Return type

[**PrinterQueueUpdateResponse**](PrinterQueueUpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a successful valid request |  -  |
**404** | Invalid uuid or printer target |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

