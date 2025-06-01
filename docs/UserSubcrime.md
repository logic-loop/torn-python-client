# UserSubcrime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**total** | **int** |  | 
**success** | **int** |  | 
**fail** | **int** |  | 

## Example

```python
from tornclient.models.user_subcrime import UserSubcrime

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubcrime from a JSON string
user_subcrime_instance = UserSubcrime.from_json(json)
# print the JSON string representation of the object
print(UserSubcrime.to_json())

# convert the object into a dict
user_subcrime_dict = user_subcrime_instance.to_dict()
# create an instance of UserSubcrime from a dict
user_subcrime_from_dict = UserSubcrime.from_dict(user_subcrime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


