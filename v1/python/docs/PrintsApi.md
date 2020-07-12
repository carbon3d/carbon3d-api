# carbon3d.PrintsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prints**](PrintsApi.md#get_prints) | **GET** /prints | List finished prints information


# **get_prints**
> PrintsResponse get_prints(limit, offset, platform_serial=platform_serial, printer_serial=printer_serial, printer_name=printer_name, print_order_uuid=print_order_uuid, print_order_number=print_order_number, started_before=started_before, started_after=started_after, finished_before=finished_before, finished_after=finished_after)

List finished prints information

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
    api_instance = carbon3d.PrintsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)
platform_serial = 'platform_serial_example' # str | Platform used for print (optional)
printer_serial = 'printer_serial_example' # str | Serial of the Printer used to print (optional)
printer_name = 'printer_name_example' # str | Name of the Printer used to print (optional)
print_order_uuid = 'print_order_uuid_example' # str | UUID of the print_order submitted (optional)
print_order_number = 'print_order_number_example' # str | Number of the print_order submitted (optional)
started_before = 'started_before_example' # str | Print started before timestamp (inclusive) (optional)
started_after = 'started_after_example' # str | Print started after timestamp (inclusive) (optional)
finished_before = 'finished_before_example' # str | Print finished before timestamp (inclusive) (optional)
finished_after = 'finished_after_example' # str | Print finished after timestamp (inclusive) (optional)

    try:
        # List finished prints information
        api_response = api_instance.get_prints(limit, offset, platform_serial=platform_serial, printer_serial=printer_serial, printer_name=printer_name, print_order_uuid=print_order_uuid, print_order_number=print_order_number, started_before=started_before, started_after=started_after, finished_before=finished_before, finished_after=finished_after)
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
 **printer_serial** | **str**| Serial of the Printer used to print | [optional] 
 **printer_name** | **str**| Name of the Printer used to print | [optional] 
 **print_order_uuid** | **str**| UUID of the print_order submitted | [optional] 
 **print_order_number** | **str**| Number of the print_order submitted | [optional] 
 **started_before** | **str**| Print started before timestamp (inclusive) | [optional] 
 **started_after** | **str**| Print started after timestamp (inclusive) | [optional] 
 **finished_before** | **str**| Print finished before timestamp (inclusive) | [optional] 
 **finished_after** | **str**| Print finished after timestamp (inclusive) | [optional] 

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

