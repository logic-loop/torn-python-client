# FactionCrimeSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** |  | 
**item_requirement** | [**FactionCrimeSlotItemRequirement**](FactionCrimeSlotItemRequirement.md) |  | 
**user_id** | **int** |  | [optional] 
**user** | [**FactionCrimeUser**](FactionCrimeUser.md) |  | 
**success_chance** | **int** | This field is replaced with &#39;checkpoint_pass_rate&#39; field and will be removed on 1st of May 2025. | [optional] 
**crime_pass_rate** | **int** | This field is replaced with &#39;checkpoint_pass_rate&#39; field and will be removed on 1st of May 2025. | [optional] 
**checkpoint_pass_rate** | **int** | Returns CPR for the player who joined the slot. If the slot is empty (availalbe), it shows your CPR for that slot. This value is 0 for expired crimes. | 

## Example

```python
from tornclient.models.faction_crime_slot import FactionCrimeSlot

# TODO update the JSON string below
json = "{}"
# create an instance of FactionCrimeSlot from a JSON string
faction_crime_slot_instance = FactionCrimeSlot.from_json(json)
# print the JSON string representation of the object
print(FactionCrimeSlot.to_json())

# convert the object into a dict
faction_crime_slot_dict = faction_crime_slot_instance.to_dict()
# create an instance of FactionCrimeSlot from a dict
faction_crime_slot_from_dict = FactionCrimeSlot.from_dict(faction_crime_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


