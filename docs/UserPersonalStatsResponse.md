# UserPersonalStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personalstats** | [**List[PersonalStatsHistoricStat]**](PersonalStatsHistoricStat.md) |  | 

## Example

```python
from tornclient.models.user_personal_stats_response import UserPersonalStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserPersonalStatsResponse from a JSON string
user_personal_stats_response_instance = UserPersonalStatsResponse.from_json(json)
# print the JSON string representation of the object
print(UserPersonalStatsResponse.to_json())

# convert the object into a dict
user_personal_stats_response_dict = user_personal_stats_response_instance.to_dict()
# create an instance of UserPersonalStatsResponse from a dict
user_personal_stats_response_from_dict = UserPersonalStatsResponse.from_dict(user_personal_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


