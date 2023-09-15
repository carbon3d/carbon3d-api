# PartOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_order_number** | **str** | Customer-provided part order number | 
**parts** | [**list[PartOrderRequestParts]**](PartOrderRequestParts.md) | Parts to be printed | 
**due_date** | **datetime** | Print due date, used to prioritize part orders for packing and printing | 
**flush** | **bool** | Push parts in a part order through the auto-packer. | [optional] 
**build_sop_uuid** | **str** | UUID of Build SOP from print.carbon3d.com/build_sops to use for optional automatic build generation parameters | [optional] 
**uuid** | **str** | UUID of the part order to create. If not provided, a UUID will be generated. | [optional] 
**packing_group** | **str** | Optional (case sensitive) string to identify part orders to be grouped together for packing. Part orders with no specified packing group are grouped together. A maximum of 40 total concurrent packing groups are permitted for &#39;open&#39; and &#39;processing&#39; PartOrders.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


