# carbon3d.PartJobsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_part_jobs**](PartJobsApi.md#create_part_jobs) | **POST** /part_jobs/bulk | Submit multiple parts for manufacturing
[**get_part_jobs**](PartJobsApi.md#get_part_jobs) | **GET** /part_jobs | Fetch Part Jobs


# **create_part_jobs**
> list[PartJob] create_part_jobs(part_job_bulk_request=part_job_bulk_request)

Submit multiple parts for manufacturing

Creates new Part Jobs. Note, PartJobs submitted may not immediately appear during fetch.

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
    api_instance = carbon3d.PartJobsApi(api_client)
    part_job_bulk_request = {"parts":[{"model_uuid":"ee1d009e-1af4-408c-bd52-18b41a4acd26"}],"build_sop_uuid":"ee1d009e-1af4-408c-bd52-18b41a4acd26","print_sop_uuid":"ee1d009e-1af4-408c-bd52-18b41a4acd26","group_name":"case-1A","due_date":"2023-04-18T03:57:12.081Z"} # PartJobBulkRequest | New part jobs to be created (optional)

    try:
        # Submit multiple parts for manufacturing
        api_response = api_instance.create_part_jobs(part_job_bulk_request=part_job_bulk_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartJobsApi->create_part_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_job_bulk_request** | [**PartJobBulkRequest**](PartJobBulkRequest.md)| New part jobs to be created | [optional] 

### Return type

[**list[PartJob]**](PartJob.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request. Items are returned in the same order in which they were submitted |  -  |
**400** | Invalid input |  -  |
**500** | Some or all of the part jobs failed to be created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_part_jobs**
> PartJobsResponse get_part_jobs(limit, cursor=cursor, uuid=uuid)

Fetch Part Jobs

Fetch a list of `Part Job` entities (most recent first)

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
    api_instance = carbon3d.PartJobsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
cursor = '' # str | Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ=d) (optional) (default to '')
uuid = ['uuid_example'] # list[str] | An array of UUIDs (optional)

    try:
        # Fetch Part Jobs
        api_response = api_instance.get_part_jobs(limit, cursor=cursor, uuid=uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartJobsApi->get_part_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **cursor** | **str**| Cursor for paginating through data (e.g. dXNlcjpXMDdRQ1JQQTQ&#x3D;d) | [optional] [default to &#39;&#39;]
 **uuid** | [**list[str]**](str.md)| An array of UUIDs | [optional] 

### Return type

[**PartJobsResponse**](PartJobsResponse.md)

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

