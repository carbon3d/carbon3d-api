# carbon3d.PartMeasurementTemplatesApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_part_measurement_templates**](PartMeasurementTemplatesApi.md#get_part_measurement_templates) | **GET** /part_measurement_templates | Fetch part measurement templates


# **get_part_measurement_templates**
> PartMeasurementTemplateResponse get_part_measurement_templates(limit, cursor=cursor, uuid=uuid, application_uuid=application_uuid, updated_before=updated_before, updated_after=updated_after, sort=sort)

Fetch part measurement templates

Gets a list of part measurement templates

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
    api_instance = carbon3d.PartMeasurementTemplatesApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
cursor = '' # str | Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d) (optional) (default to '')
uuid = ['uuid_example'] # list[str] | An array of UUIDs (optional)
application_uuid = ['application_uuid_example'] # list[str] | An array of Application UUIDs (optional)
updated_before = '2013-10-20T19:20:30+01:00' # datetime | Updated before timestamp (exclusive) (optional)
updated_after = '2013-10-20T19:20:30+01:00' # datetime | Updated at or after timestamp (inclusive) (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. (optional)

    try:
        # Fetch part measurement templates
        api_response = api_instance.get_part_measurement_templates(limit, cursor=cursor, uuid=uuid, application_uuid=application_uuid, updated_before=updated_before, updated_after=updated_after, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartMeasurementTemplatesApi->get_part_measurement_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **cursor** | **str**| Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ&#x3D;d) | [optional] [default to &#39;&#39;]
 **uuid** | [**list[str]**](str.md)| An array of UUIDs | [optional] 
 **application_uuid** | [**list[str]**](str.md)| An array of Application UUIDs | [optional] 
 **updated_before** | **datetime**| Updated before timestamp (exclusive) | [optional] 
 **updated_after** | **datetime**| Updated at or after timestamp (inclusive) | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. | [optional] 

### Return type

[**PartMeasurementTemplateResponse**](PartMeasurementTemplateResponse.md)

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

