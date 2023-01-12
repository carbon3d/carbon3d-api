# AutomationRun

Automation Run object with its params and state
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | uuid for the automation run itself | 
**customer_id** | **str** | customer id | [optional] 
**created_at** | **str** | Create time | [optional] 
**updated_at** | **str** | Update time | [optional] 
**part_uuids** | **list[str]** | uuids of created parts. | [optional] 
**part_order_uuid** | **str** | Part order uuid. | [optional] 
**model_uuids** | **list[str]** | uuids of models submitted for automation | 
**model_sop_uuid** | **str** | uuid for a model_sop to be applied to the submitted model | [optional] 
**part_sop_uuid** | **str** | uuid for a part_sop to be applied to the submitted model | [optional] 
**build_sop_uuid** | **str** | uuid for a build_sop to be applied to the submitted model | [optional] 
**printer_queue_sop_uuid** | **str** | uuid for a printer_queue_sop to be applied to the submitted model | [optional] 
**status** | **str** | Automation run status: --&gt; submitted --&gt; processing --&gt; succeeded --&gt; failed --&gt; canceled  | [optional] 
**steps** | [**list[AutomationRunSteps]**](AutomationRunSteps.md) | List of steps taken during this automation run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


