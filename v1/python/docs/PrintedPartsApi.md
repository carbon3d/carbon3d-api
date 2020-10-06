# carbon3d.PrintedPartsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_printed_part**](PrintedPartsApi.md#get_printed_part) | **GET** /printed_parts/{uuid} | Fetch a printed Part
[**get_printed_parts**](PrintedPartsApi.md#get_printed_parts) | **GET** /printed_parts | Fetch printed parts


# **get_printed_part**
> PrintedPart get_printed_part(uuid)

Fetch a printed Part

Fetch the details of a single PrintedPart.

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
    api_instance = carbon3d.PrintedPartsApi(api_client)
    uuid = 'uuid_example' # str | A unique identifier for a PrintedPart.

    try:
        # Fetch a printed Part
        api_response = api_instance.get_printed_part(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintedPartsApi->get_printed_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A unique identifier for a PrintedPart. | 

### Return type

[**PrintedPart**](PrintedPart.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The printed part does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_printed_parts**
> PrintedPartsResponse get_printed_parts(limit, status=status, part_order_uuid=part_order_uuid, part_uuid=part_uuid, part_order_number=part_order_number, print_order_uuid=print_order_uuid, print_order_number=print_order_number, build_uuid=build_uuid, print_id=print_id, cursor=cursor, uuid=uuid, application_id=application_id, updated_before=updated_before, updated_after=updated_after, started_before=started_before, started_after=started_after, finished_before=finished_before, finished_after=finished_after, sort=sort)

Fetch printed parts

Gets a list of Part entities (most recent first)

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
    api_instance = carbon3d.PrintedPartsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
status = carbon3d.PrintedPartStatus() # PrintedPartStatus | Current printed part status (optional)
part_order_uuid = 'part_order_uuid_example' # str | PartOrder UUID (optional)
part_uuid = 'part_uuid_example' # str | Part UUID (optional)
part_order_number = 'part_order_number_example' # str | Customer-provided part order number the printed parts belong to (optional)
print_order_uuid = 'print_order_uuid_example' # str | Print Order UUID (optional)
print_order_number = 'print_order_number_example' # str | Customer-provided print order number that the printed parts belong to (optional)
build_uuid = 'build_uuid_example' # str | Build UUID (optional)
print_id = ['print_id_example'] # list[str] | An array of Print IDs. (optional)
cursor = '' # str | Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d) (optional) (default to '')
uuid = ['uuid_example'] # list[str] | An array of UUIDs (optional)
application_id = [56] # list[int] | An array of Application IDs (optional)
updated_before = '2013-10-20T19:20:30+01:00' # datetime | Updated before time X (optional)
updated_after = '2013-10-20T19:20:30+01:00' # datetime | Updated after time X (optional)
started_before = '2013-10-20T19:20:30+01:00' # datetime | Started before time X (optional)
started_after = '2013-10-20T19:20:30+01:00' # datetime | Started after time X (optional)
finished_before = '2013-10-20T19:20:30+01:00' # datetime | Finished before time X (optional)
finished_after = '2013-10-20T19:20:30+01:00' # datetime | Finished after time X (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `status`, `part_number` (optional)

    try:
        # Fetch printed parts
        api_response = api_instance.get_printed_parts(limit, status=status, part_order_uuid=part_order_uuid, part_uuid=part_uuid, part_order_number=part_order_number, print_order_uuid=print_order_uuid, print_order_number=print_order_number, build_uuid=build_uuid, print_id=print_id, cursor=cursor, uuid=uuid, application_id=application_id, updated_before=updated_before, updated_after=updated_after, started_before=started_before, started_after=started_after, finished_before=finished_before, finished_after=finished_after, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintedPartsApi->get_printed_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **status** | [**PrintedPartStatus**](.md)| Current printed part status | [optional] 
 **part_order_uuid** | **str**| PartOrder UUID | [optional] 
 **part_uuid** | **str**| Part UUID | [optional] 
 **part_order_number** | **str**| Customer-provided part order number the printed parts belong to | [optional] 
 **print_order_uuid** | **str**| Print Order UUID | [optional] 
 **print_order_number** | **str**| Customer-provided print order number that the printed parts belong to | [optional] 
 **build_uuid** | **str**| Build UUID | [optional] 
 **print_id** | [**list[str]**](str.md)| An array of Print IDs. | [optional] 
 **cursor** | **str**| Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ&#x3D;d) | [optional] [default to &#39;&#39;]
 **uuid** | [**list[str]**](str.md)| An array of UUIDs | [optional] 
 **application_id** | [**list[int]**](int.md)| An array of Application IDs | [optional] 
 **updated_before** | **datetime**| Updated before time X | [optional] 
 **updated_after** | **datetime**| Updated after time X | [optional] 
 **started_before** | **datetime**| Started before time X | [optional] 
 **started_after** | **datetime**| Started after time X | [optional] 
 **finished_before** | **datetime**| Finished before time X | [optional] 
 **finished_after** | **datetime**| Finished after time X | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. Sortable fields are: &#x60;status&#x60;, &#x60;part_number&#x60; | [optional] 

### Return type

[**PrintedPartsResponse**](PrintedPartsResponse.md)

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

