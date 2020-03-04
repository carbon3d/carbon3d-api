# OrdersResponseOrders

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Order UUID | [optional] 
**status** | [**OrderStatus**](OrderStatus.md) |  | [optional] 
**order_number** | **str** | Customer-provided order number | [optional] 
**printed_parts_count** | **int** | Quantity of printed parts in the order | [optional] 
**due_date** | **datetime** | Print due date, used to prioritize orders for packing and printing | [optional] 
**route_to** | **list[str]** | Section to route this order to (e.g. production, a rework line) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


