# OrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_number** | **str** | Customer-provided order number | 
**parts** | [**list[OrderRequestParts]**](OrderRequestParts.md) | Parts to be printed | 
**due_date** | **datetime** | Print due date, used to prioritize orders for packing and printing | 
**route_to** | **list[str]** | Section(s) to route this order to (e.g. a rework line) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


