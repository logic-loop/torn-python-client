# FactionTerritoriesReponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**territory** | [**List[FactionTerritory]**](FactionTerritory.md) |  | 

## Example

```python
from tornclient.models.faction_territories_reponse import FactionTerritoriesReponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoriesReponse from a JSON string
faction_territories_reponse_instance = FactionTerritoriesReponse.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoriesReponse.to_json())

# convert the object into a dict
faction_territories_reponse_dict = faction_territories_reponse_instance.to_dict()
# create an instance of FactionTerritoriesReponse from a dict
faction_territories_reponse_from_dict = FactionTerritoriesReponse.from_dict(faction_territories_reponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


