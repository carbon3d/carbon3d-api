# PartJob

Job object with its params and state
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] [readonly] 
**part_uuid** | **str** |  | [optional] 
**status** | **str** | PartJob status:   * &#x60;waiting&#x60; - PartJob is waiting to run.   * &#x60;model_program_running&#x60; - PartJob is running provided model program.   * &#x60;build_prep_waiting&#x60; - PartJob is waiting for build preparation step.   * &#x60;failed&#x60; - PartJob failed.  | [optional] [readonly] 
**failure_reason** | **str** | PartJob failure reason (only present when status &#x3D;&#x3D; &#x60;failed&#x60;):   * &#x60;unauthorized&#x60; - The request was unauthorized.   * &#x60;model_program_run&#x60; - The request failed while running a model program.   * &#x60;bad_request&#x60; - The request was malformed.   * &#x60;other&#x60; - PartJob has failed for any other reason.  | [optional] [readonly] 
**model_uuid** | **str** |  | 
**model_program_uuid** | **str** |  | 
**model_program_parameters** | **dict(str, str)** | parameters for the model program | 
**build_sop_uuid** | **str** |  | 
**print_sop_uuid** | **str** |  | 
**group_name** | **str** | Group identifier | 
**due_date** | **datetime** | Print due date, used to prioritize Part Jobs | 
**split_group** | **bool** | Allows a part_group to be split across multiple builds. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


