# carbon3d.ModelProgramRunsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model_program_run**](ModelProgramRunsApi.md#create_model_program_run) | **POST** /model_program_runs | Run a model program to alter your models
[**get_model_program_run**](ModelProgramRunsApi.md#get_model_program_run) | **GET** /model_program_runs/{uuid} | Get a model program run by UUID


# **create_model_program_run**
> ModelProgramRun create_model_program_run(model_program_run_request=model_program_run_request)

Run a model program to alter your models

Create a new model program run

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
    api_instance = carbon3d.ModelProgramRunsApi(api_client)
    model_program_run_request = carbon3d.ModelProgramRunRequest() # ModelProgramRunRequest |  (optional)

    try:
        # Run a model program to alter your models
        api_response = api_instance.create_model_program_run(model_program_run_request=model_program_run_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelProgramRunsApi->create_model_program_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_program_run_request** | [**ModelProgramRunRequest**](ModelProgramRunRequest.md)|  | [optional] 

### Return type

[**ModelProgramRun**](ModelProgramRun.md)

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

# **get_model_program_run**
> ModelProgramRun get_model_program_run(uuid)

Get a model program run by UUID

Fetch the output of a model program run request

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
    api_instance = carbon3d.ModelProgramRunsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the Model Program Run for which you want to fetch outputs

    try:
        # Get a model program run by UUID
        api_response = api_instance.get_model_program_run(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelProgramRunsApi->get_model_program_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the Model Program Run for which you want to fetch outputs | 

### Return type

[**ModelProgramRun**](ModelProgramRun.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The model program run does not exist |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

