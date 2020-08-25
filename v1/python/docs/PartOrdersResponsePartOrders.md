# PartOrdersResponsePartOrders

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | PartOrder UUID | [optional] 
**status** | [**PartOrderStatus**](PartOrderStatus.md) |  | [optional] 
**part_order_number** | **str** | Customer-provided part order number | [optional] 
**printed_parts_count** | **int** | Quantity of printed parts in the part order | [optional] 
**due_date** | **datetime** | Print due date, used to prioritize part orders for packing and printing | [optional] 
**route_to** | **list[str]** | Section to route this part order to (e.g. production, a rework line) | [optional] 
**flushed_at** | **datetime** | When the part order was flushed through the packer, or null if it is not flushed. | [optional] 
**part_uuids** | **list[str]** | List of part_uuids for given order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


