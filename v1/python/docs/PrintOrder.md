# PrintOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The uuid of the print order | [optional] 
**build_uuid** | **str** | The uuid of the build to be queued | [optional] 
**total_copies** | **int** | The total number of copies to be printed | [optional] [default to 1]
**created_at** | **datetime** | Time when print order was created | [optional] 
**print_order_number** | **str** | Customer-provided print order number | [optional] 
**print_order_tags** | **dict(str, str)** | Key value pairs to be associated with print order | [optional] 
**notes** | **str** | Notes associated with | [optional] 
**routed_to** | [**dict(str, PrintOrderRoutedTo)**](PrintOrderRoutedTo.md) | Printers that this print order was routed to, keyed off printer serial number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


