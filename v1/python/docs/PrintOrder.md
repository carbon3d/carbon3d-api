# PrintOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The uuid of the print order | [optional] 
**build_uuid** | **str** | The uuid of the build to be queued | [optional] 
**total_copies** | **int** | The total number of copies to be printed | [optional] [default to 1]
**route_to** | **list[str]** | Serial number of printers to be printed on | [optional] 
**created_at** | **datetime** | Time when print order was created | [optional] 
**print_order_number** | **str** | Customer-provided print order number | [optional] 
**print_order_tags** | **dict(str, str)** | Key value pairs to be associated with print order | [optional] 
**notes** | **str** | Notes associated with | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


