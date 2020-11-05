# PrinterQueueMoveRequest

Represents the move request for prints on a given target printer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** |  | 
**printer_serial** | **str** | Target printer for the move operation | 
**index** | **int** | Target index for given uuids on target printer queue. If given 0, places the first uuid at the top of the queue, followed by other param uuids and the rest of the existing queue. If index provided is higher than the max index of the queue, add uuid(s) to the end. Use &#39;-1&#39; to express &#39;end of queue&#39;. | 
**print_uuids** | **list[str]** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


