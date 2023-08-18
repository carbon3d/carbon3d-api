# Build

A build containing one or more parts
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**packing_group** | **str** | Optional customer-provided part order packing group | [optional] 
**parts** | [**list[Part]**](Part.md) |  | 
**attachments** | [**list[BuildAttachments]**](BuildAttachments.md) |  | [optional] 
**name** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**application_uuid** | **str** | Application UUID | [optional] 
**part_orders** | [**list[BuildPartOrders]**](BuildPartOrders.md) |  | [optional] 
**created_at** | **datetime** | Timestamp at which the build was created. | [optional] 
**updated_at** | **datetime** | Timestamp at which the build was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


