# ModelProgramRun

Response containing the details about a model_program_run
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | status of the current operation | 
**progress** | **float** | current progress of the concerned operation as a number between 0 and 1 | 
**model_uuid** | **str** | uuid of the output model | [optional] 
**failure_message** | **str** | message in case of failure | [optional] 
**uuid** | **str** | uuid of the model program run | [optional] 
**operation_status** | [**list[ModelProgramOperation]**](ModelProgramOperation.md) | details about the statuses and outputs of named operations specified by the customer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


