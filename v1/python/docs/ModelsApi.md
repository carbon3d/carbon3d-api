# carbon3d.ModelsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_model**](ModelsApi.md#download_model) | **GET** /models/{uuid}/download | Download a model by UUID
[**find_models**](ModelsApi.md#find_models) | **GET** /models | Fetch models
[**get_model**](ModelsApi.md#get_model) | **GET** /models/{uuid} | Get a model by UUID
[**get_presigned_upload_url**](ModelsApi.md#get_presigned_upload_url) | **POST** /models/presigned | Create presigned upload URL for a filename
[**resolve_presigned_model_upload**](ModelsApi.md#resolve_presigned_model_upload) | **POST** /models/presigned/resolve | Resolve presigned model upload
[**upload_model**](ModelsApi.md#upload_model) | **POST** /models | Upload a model


# **download_model**
> file download_model(uuid)

Download a model by UUID

Download a model by UUID

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
    api_instance = carbon3d.ModelsApi(api_client)
    uuid = 'uuid_example' # str | Model UUID

    try:
        # Download a model by UUID
        api_response = api_instance.download_model(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->download_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Model UUID | 

### Return type

**file**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File response after redirect |  -  |
**302** | Expected response to be a redirect to the file |  -  |
**404** | The model does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_models**
> ModelsResponse find_models(uuid=uuid, external_id=external_id)

Fetch models

Fetch Models using the given list of uuids and external_ids. At least one input array out of uuids and external_ids must be provided and the result is the union of all matching models found using given arrays.

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
    api_instance = carbon3d.ModelsApi(api_client)
    uuid = ['uuid_example'] # list[str] | An array of UUIDs (optional)
external_id = ['external_id_example'] # list[str] | An array of external ids (optional)

    try:
        # Fetch models
        api_response = api_instance.find_models(uuid=uuid, external_id=external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->find_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**list[str]**](str.md)| An array of UUIDs | [optional] 
 **external_id** | [**list[str]**](str.md)| An array of external ids | [optional] 

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_presigned_upload_url**
> ModelPresignedUploadUrlResponse get_presigned_upload_url(model_presigned_upload_url_request=model_presigned_upload_url_request)

Create presigned upload URL for a filename

Create presigned upload URL for a filename

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
    api_instance = carbon3d.ModelsApi(api_client)
    model_presigned_upload_url_request = carbon3d.ModelPresignedUploadUrlRequest() # ModelPresignedUploadUrlRequest | Create presigned upload URL for a filename. (optional)

    try:
        # Create presigned upload URL for a filename
        api_response = api_instance.get_presigned_upload_url(model_presigned_upload_url_request=model_presigned_upload_url_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->get_presigned_upload_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_presigned_upload_url_request** | [**ModelPresignedUploadUrlRequest**](ModelPresignedUploadUrlRequest.md)| Create presigned upload URL for a filename. | [optional] 

### Return type

[**ModelPresignedUploadUrlResponse**](ModelPresignedUploadUrlResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_presigned_model_upload**
> resolve_presigned_model_upload(model_resolve_upload_request=model_resolve_upload_request)

Resolve presigned model upload

Resolve presigned model upload

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
    api_instance = carbon3d.ModelsApi(api_client)
    model_resolve_upload_request = carbon3d.ModelResolveUploadRequest() # ModelResolveUploadRequest | Resolve presigned model upload (optional)

    try:
        # Resolve presigned model upload
        api_instance.resolve_presigned_model_upload(model_resolve_upload_request=model_resolve_upload_request)
    except ApiException as e:
        print("Exception when calling ModelsApi->resolve_presigned_model_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_resolve_upload_request** | [**ModelResolveUploadRequest**](ModelResolveUploadRequest.md)| Resolve presigned model upload | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_model**
> Model upload_model(filename, application_uuid=application_uuid, external_id=external_id, body=body)

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
    api_instance = carbon3d.ModelsApi(api_client)
    filename = 'filename_example' # str | Filename of the model - assumes .stl if no extension is given
application_uuid = 'application_uuid_example' # str | Application UUID (optional)
external_id = 'external_id_example' # str | User provided external id (optional)
body = '/path/to/file' # file |  (optional)

    try:
        # Upload a model
        api_response = api_instance.upload_model(filename, application_uuid=application_uuid, external_id=external_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->upload_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename of the model - assumes .stl if no extension is given | 
 **application_uuid** | **str**| Application UUID | [optional] 
 **external_id** | **str**| User provided external id | [optional] 
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

