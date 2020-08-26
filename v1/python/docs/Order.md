# Order

An order to print parts
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Order UUID | [readonly] 
**status** | [**PartOrderStatus**](PartOrderStatus.md) |  | [optional] 
**order_number** | **str** | Customer-provided order number | 
**due_date** | **datetime** | Print due date, used to prioritize orders for packing and printing | 
**route_to** | **list[str]** | Section to route this order to (e.g. a rework line) | [optional] 
**printed_parts** | [**list[PrintedPartRef]**](PrintedPartRef.md) | Parts already printed or to be printed | 
**flushed_at** | **datetime** | When the order was flushed, or null if it has not been flushed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


