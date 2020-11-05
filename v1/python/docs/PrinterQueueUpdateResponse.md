# PrinterQueueUpdateResponse

Represents state of the update performed on the target queue
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **list[str]** |  | [optional] 
**code** | **int** | 0 means success, 1 for partial success (e.g: 1 uuid deleted, 1 not found), 2 is for error state (the request did not proceed) | [optional] 
**message** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


