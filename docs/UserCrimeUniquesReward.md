# UserCrimeUniquesReward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserCrimeRewardItem]**](UserCrimeRewardItem.md) |  | 
**money** | [**UserCrimeUniquesRewardMoney**](UserCrimeUniquesRewardMoney.md) |  | 
**ammo** | [**UserCrimeUniquesRewardAmmo**](UserCrimeUniquesRewardAmmo.md) |  | 

## Example

```python
from tornclient.models.user_crime_uniques_reward import UserCrimeUniquesReward

# TODO update the JSON string below
json = "{}"
# create an instance of UserCrimeUniquesReward from a JSON string
user_crime_uniques_reward_instance = UserCrimeUniquesReward.from_json(json)
# print the JSON string representation of the object
print(UserCrimeUniquesReward.to_json())

# convert the object into a dict
user_crime_uniques_reward_dict = user_crime_uniques_reward_instance.to_dict()
# create an instance of UserCrimeUniquesReward from a dict
user_crime_uniques_reward_from_dict = UserCrimeUniquesReward.from_dict(user_crime_uniques_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


