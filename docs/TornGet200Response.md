# TornGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subcrimes** | [**List[TornSubcrime]**](TornSubcrime.md) |  | 
**crimes** | [**List[TornCrime]**](TornCrime.md) |  | 
**calendar** | [**TornCalendarResponseCalendar**](TornCalendarResponseCalendar.md) |  | 
**hof** | [**List[TornHof]**](TornHof.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 
**factionhof** | [**List[TornFactionHof]**](TornFactionHof.md) |  | 
**logtypes** | [**List[TornLog]**](TornLog.md) |  | 
**items** | [**List[TornItem]**](TornItem.md) |  | 
**logcategories** | [**List[TornLogCategory]**](TornLogCategory.md) |  | 
**education** | [**List[TornEducation]**](TornEducation.md) |  | 
**bounties** | [**List[Bounty]**](Bounty.md) |  | 
**itemammo** | [**List[TornItemAmmo]**](TornItemAmmo.md) |  | 
**faction_tree** | [**List[TornFactionTree]**](TornFactionTree.md) |  | 
**attacklog** | [**AttackLogResponseAttacklog**](AttackLogResponseAttacklog.md) |  | 
**territory** | [**List[TornTerritory]**](TornTerritory.md) |  | 
**itemmods** | [**List[TornItemMods]**](TornItemMods.md) |  | 
**selections** | [**List[TornSelectionName]**](TornSelectionName.md) |  | 
**timestamp** | **int** |  | 

## Example

```python
from tornclient.models.torn_get200_response import TornGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TornGet200Response from a JSON string
torn_get200_response_instance = TornGet200Response.from_json(json)
# print the JSON string representation of the object
print(TornGet200Response.to_json())

# convert the object into a dict
torn_get200_response_dict = torn_get200_response_instance.to_dict()
# create an instance of TornGet200Response from a dict
torn_get200_response_from_dict = TornGet200Response.from_dict(torn_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


