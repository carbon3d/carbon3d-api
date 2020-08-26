# PartOrder

A part order to print parts
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | PartOrder UUID | [readonly] 
**status** | [**PartOrderStatus**](PartOrderStatus.md) |  | [optional] 
**part_order_number** | **str** | Customer-provided part order number | [optional] 
**due_date** | **datetime** | Print due date, used to prioritize orders for packing and printing | 
**route_to** | **list[str]** | Section to route this part order to (e.g. a rework line) | [optional] 
**printed_parts** | [**list[PrintedPartRef]**](PrintedPartRef.md) | Parts already printed or to be printed | 
**flushed_at** | **datetime** | When the part order was flushed, or null if it has not been flushed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


