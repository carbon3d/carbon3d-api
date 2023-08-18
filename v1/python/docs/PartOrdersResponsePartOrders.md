# PartOrdersResponsePartOrders

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | PartOrder UUID | [optional] 
**status** | [**PartOrderStatus**](PartOrderStatus.md) |  | [optional] 
**part_order_number** | **str** | Customer-provided part order number | [optional] 
**printed_parts_count** | **int** | Quantity of printed parts in the part order | [optional] 
**due_date** | **datetime** | Print due date, used to prioritize part orders for packing and printing | [optional] 
**flushed_at** | **datetime** | When the part order was flushed through the packer, or null if it is not flushed. | [optional] 
**build_uuids** | **list[str]** | Builds which contain printed parts from this part order. | [optional] 
**build_sop_uuid** | **str** | UUID of Build SOP to use for auto layout parameters, from print.carbon3d.com/build_sops | [optional] 
**packing_group** | **str** | Optional string to identify part orders to be grouped together for packing. | [optional] 
**application_uuid** | **str** | Application UUID | [optional] 
**created_at** | **datetime** | Timestamp at which the part order was created. | [optional] 
**updated_at** | **datetime** | Timestamp at which the part order was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


