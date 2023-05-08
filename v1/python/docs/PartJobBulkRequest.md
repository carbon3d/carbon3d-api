# PartJobBulkRequest

Request to submit new Part Jobs
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts** | [**list[JobPart]**](JobPart.md) |  | 
**build_sop_uuid** | **str** |  | 
**print_sop_uuid** | **str** |  | 
**group_name** | **str** | Group identifier | 
**due_date** | **datetime** | Print due date, used to prioritize Part Jobs | 
**split_group** | **bool** | Allows a part_group to be split across multiple builds. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


