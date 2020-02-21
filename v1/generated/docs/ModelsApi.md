# carbon3d.ModelsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_model**](ModelsApi.md#get_model) | **GET** /models/{uuid} | Get a model by UUID
[**get_models**](ModelsApi.md#get_models) | **GET** /models | Fetch models
[**upload_model**](ModelsApi.md#upload_model) | **POST** /models | Upload a model


# **get_model**
> Model get_model(uuid)

Get a model by UUID

Fetch a model by UUID

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
    api_instance = carbon3d.ModelsApi(api_client)
    uuid = 'uuid_example' # str | Model UUID

    try:
        # Get a model by UUID
        api_response = api_instance.get_model(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Model UUID | 

### Return type

[**Model**](Model.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The model does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> ModelsResponse get_models(limit, offset, filename=filename, sort=sort)

Fetch models

Fetch Models, filtered by the respective query parameters (most recent first)

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
    api_instance = carbon3d.ModelsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)
filename = 'filename_example' # str | Filename of the model (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. (optional)

    try:
        # Fetch models
        api_response = api_instance.get_models(limit, offset, filename=filename, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **offset** | **int**| Number of items to skip | [default to 0]
 **filename** | **str**| Filename of the model | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. | [optional] 

### Return type

[**ModelsResponse**](ModelsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_model**
> Model upload_model(filename, application_id=application_id, body=body)

Upload a model

Upload a new model

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
    api_instance = carbon3d.ModelsApi(api_client)
    filename = 'filename_example' # str | Filename of the model
application_id = 56 # int | Application ID (optional)
body = '/path/to/file' # file |  (optional)

    try:
        # Upload a model
        api_response = api_instance.upload_model(filename, application_id=application_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->upload_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename of the model | 
 **application_id** | **int**| Application ID | [optional] 
 **body** | **file**|  | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

