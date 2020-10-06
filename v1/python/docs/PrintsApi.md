# carbon3d.PrintsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prints**](PrintsApi.md#get_prints) | **GET** /prints | List finished prints information


# **get_prints**
> PrintsResponse get_prints(limit, cursor=cursor, uuid=uuid, application_id=application_id, started_before=started_before, started_after=started_after, finished_before=finished_before, finished_after=finished_after, print_id=print_id, status=status, print_order_number=print_order_number, print_order_uuid=print_order_uuid, printer_serial=printer_serial, printer_name=printer_name, platform_serial=platform_serial, sort=sort)

List finished prints information

Fetch prints

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
cursor = '' # str | Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d) (optional) (default to '')
uuid = ['uuid_example'] # list[str] | An array of UUIDs (optional)
application_id = [56] # list[int] | An array of Application IDs (optional)
started_before = 'started_before_example' # str | Print started before timestamp (inclusive) (optional)
started_after = 'started_after_example' # str | Print started after timestamp (inclusive) (optional)
finished_before = 'finished_before_example' # str | Print finished before timestamp (inclusive) (optional)
finished_after = 'finished_after_example' # str | Print finished after timestamp (inclusive) (optional)
print_id = ['print_id_example'] # list[str] | An array of Print IDs (optional)
status = ['status_example'] # list[str] | An array of statuses (optional)
print_order_number = ['print_order_number_example'] # list[str] | An array of number(s) of the print_order submitted (optional)
print_order_uuid = ['print_order_uuid_example'] # list[str] | An array of UUID(s) of the print_order submitted (optional)
printer_serial = ['printer_serial_example'] # list[str] | An array of serials of the Printer(s) used to print (optional)
printer_name = ['printer_name_example'] # list[str] | An array of names of the Printer(s) used to print (optional)
platform_serial = ['platform_serial_example'] # list[str] | An array of names of the Printer(s) used to print (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `uuid`, `status`, `started_at`, `finished_at`, `print_order_number` (optional)

    try:
        # List finished prints information
        api_response = api_instance.get_prints(limit, cursor=cursor, uuid=uuid, application_id=application_id, started_before=started_before, started_after=started_after, finished_before=finished_before, finished_after=finished_after, print_id=print_id, status=status, print_order_number=print_order_number, print_order_uuid=print_order_uuid, printer_serial=printer_serial, printer_name=printer_name, platform_serial=platform_serial, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintsApi->get_prints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **cursor** | **str**| Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ&#x3D;d) | [optional] [default to &#39;&#39;]
 **uuid** | [**list[str]**](str.md)| An array of UUIDs | [optional] 
 **application_id** | [**list[int]**](int.md)| An array of Application IDs | [optional] 
 **started_before** | **str**| Print started before timestamp (inclusive) | [optional] 
 **started_after** | **str**| Print started after timestamp (inclusive) | [optional] 
 **finished_before** | **str**| Print finished before timestamp (inclusive) | [optional] 
 **finished_after** | **str**| Print finished after timestamp (inclusive) | [optional] 
 **print_id** | [**list[str]**](str.md)| An array of Print IDs | [optional] 
 **status** | [**list[str]**](str.md)| An array of statuses | [optional] 
 **print_order_number** | [**list[str]**](str.md)| An array of number(s) of the print_order submitted | [optional] 
 **print_order_uuid** | [**list[str]**](str.md)| An array of UUID(s) of the print_order submitted | [optional] 
 **printer_serial** | [**list[str]**](str.md)| An array of serials of the Printer(s) used to print | [optional] 
 **printer_name** | [**list[str]**](str.md)| An array of names of the Printer(s) used to print | [optional] 
 **platform_serial** | [**list[str]**](str.md)| An array of names of the Printer(s) used to print | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. Sortable fields are: &#x60;uuid&#x60;, &#x60;status&#x60;, &#x60;started_at&#x60;, &#x60;finished_at&#x60;, &#x60;print_order_number&#x60; | [optional] 

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

