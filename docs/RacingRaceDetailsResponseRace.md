# RacingRaceDetailsResponseRace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**track_id** | **int** |  | 
**creator_id** | **int** |  | 
**status** | [**RaceStatusEnum**](RaceStatusEnum.md) |  | 
**laps** | **int** |  | 
**participants** | [**RaceParticipants**](RaceParticipants.md) |  | 
**schedule** | [**RaceSchedule**](RaceSchedule.md) |  | 
**requirements** | [**RaceRequirements**](RaceRequirements.md) |  | 
**results** | [**List[RacerDetails]**](RacerDetails.md) |  | 

## Example

```python
from tornclient.models.racing_race_details_response_race import RacingRaceDetailsResponseRace

# TODO update the JSON string below
json = "{}"
# create an instance of RacingRaceDetailsResponseRace from a JSON string
racing_race_details_response_race_instance = RacingRaceDetailsResponseRace.from_json(json)
# print the JSON string representation of the object
print(RacingRaceDetailsResponseRace.to_json())

# convert the object into a dict
racing_race_details_response_race_dict = racing_race_details_response_race_instance.to_dict()
# create an instance of RacingRaceDetailsResponseRace from a dict
racing_race_details_response_race_from_dict = RacingRaceDetailsResponseRace.from_dict(racing_race_details_response_race_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


