# RacingGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**races** | [**List[Race]**](Race.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 
**records** | [**List[RaceRecord]**](RaceRecord.md) |  | 
**race** | [**RacingRaceDetailsResponseRace**](RacingRaceDetailsResponseRace.md) |  | [optional] 
**cars** | [**List[RaceCar]**](RaceCar.md) |  | 
**tracks** | [**List[RaceTrack]**](RaceTrack.md) |  | 
**carupgrades** | [**List[RaceCarUpgrade]**](RaceCarUpgrade.md) |  | 
**selections** | [**List[RacingSelectionName]**](RacingSelectionName.md) |  | 
**timestamp** | **int** |  | 

## Example

```python
from tornclient.models.racing_get200_response import RacingGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RacingGet200Response from a JSON string
racing_get200_response_instance = RacingGet200Response.from_json(json)
# print the JSON string representation of the object
print(RacingGet200Response.to_json())

# convert the object into a dict
racing_get200_response_dict = racing_get200_response_instance.to_dict()
# create an instance of RacingGet200Response from a dict
racing_get200_response_from_dict = RacingGet200Response.from_dict(racing_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


