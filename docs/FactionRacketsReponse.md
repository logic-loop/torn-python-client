# FactionRacketsReponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rackets** | [**List[TornRacket]**](TornRacket.md) |  | 

## Example

```python
from tornclient.models.faction_rackets_reponse import FactionRacketsReponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionRacketsReponse from a JSON string
faction_rackets_reponse_instance = FactionRacketsReponse.from_json(json)
# print the JSON string representation of the object
print(FactionRacketsReponse.to_json())

# convert the object into a dict
faction_rackets_reponse_dict = faction_rackets_reponse_instance.to_dict()
# create an instance of FactionRacketsReponse from a dict
faction_rackets_reponse_from_dict = FactionRacketsReponse.from_dict(faction_rackets_reponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


