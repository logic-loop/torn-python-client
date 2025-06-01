# FactionTerritoryWarsHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**territorywars** | [**List[FactionTerritoryWarFinished]**](FactionTerritoryWarFinished.md) |  | 

## Example

```python
from tornclient.models.faction_territory_wars_history_response import FactionTerritoryWarsHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionTerritoryWarsHistoryResponse from a JSON string
faction_territory_wars_history_response_instance = FactionTerritoryWarsHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(FactionTerritoryWarsHistoryResponse.to_json())

# convert the object into a dict
faction_territory_wars_history_response_dict = faction_territory_wars_history_response_instance.to_dict()
# create an instance of FactionTerritoryWarsHistoryResponse from a dict
faction_territory_wars_history_response_from_dict = FactionTerritoryWarsHistoryResponse.from_dict(faction_territory_wars_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


