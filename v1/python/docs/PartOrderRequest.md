# PartOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_order_number** | **str** | Customer-provided part order number | 
**parts** | [**list[PartOrderRequestParts]**](PartOrderRequestParts.md) | Parts to be printed | 
**due_date** | **datetime** | Print due date, used to prioritize part orders for packing and printing | 
**flush** | **bool** | Push parts in a part order through the auto-packer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


