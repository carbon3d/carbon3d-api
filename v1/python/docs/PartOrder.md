# PartOrder

A part order to print parts
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | PartOrder UUID | [readonly] 
**status** | [**PartOrderStatus**](PartOrderStatus.md) |  | [optional] 
**part_order_number** | **str** | Customer-provided part order number | [optional] 
**due_date** | **datetime** | Print due date, used to prioritize part orders for packing and printing | 
**printed_parts** | [**list[PrintedPartRef]**](PrintedPartRef.md) | Parts already printed or to be printed | 
**flushed_at** | **datetime** | When the part order was flushed, or null if it has not been flushed | [optional] 
**build_uuids** | **list[str]** | Builds which contain printed parts from this part order. | [optional] 
**build_sop_uuid** | **str** | UUID of Build SOP from print.carbon3d.com/build_sops to use for optional automatic build generation parameters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


