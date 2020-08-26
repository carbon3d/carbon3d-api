# ModelPrint

Represents the print of a build
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**print_id** | **str** |  | [optional] 
**build_uuid** | **str** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**remaining_sec** | **int** | Estimated time until expected print completion (in seconds) | [optional] 
**printed_by** | **str** |  | [optional] 
**print_order_uuid** | **str** |  | [optional] 
**print_order_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**origin** | [**PrintOrigin**](PrintOrigin.md) |  | [optional] 
**config** | [**PrintConfig**](PrintConfig.md) |  | [optional] 
**metrics** | [**PrintMetrics**](PrintMetrics.md) |  | [optional] 
**feedback** | [**PrintFeedback**](PrintFeedback.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


