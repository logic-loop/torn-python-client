# UserLife

Unfortunately, current life value is often shown incorrectly, and the calculation for each member is very resource heavy, so this field is deprecated and will be removed on 1st of May, 2025.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **int** |  | [optional] 
**maximum** | **int** |  | [optional] 

## Example

```python
from tornclient.models.user_life import UserLife

# TODO update the JSON string below
json = "{}"
# create an instance of UserLife from a JSON string
user_life_instance = UserLife.from_json(json)
# print the JSON string representation of the object
print(UserLife.to_json())

# convert the object into a dict
user_life_dict = user_life_instance.to_dict()
# create an instance of UserLife from a dict
user_life_from_dict = UserLife.from_dict(user_life_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


