# KeyGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**KeyInfoResponseInfo**](KeyInfoResponseInfo.md) |  | 
**log** | [**List[KeyLogResponseLogInner]**](KeyLogResponseLogInner.md) |  | 

## Example

```python
from tornclient.models.key_get200_response import KeyGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of KeyGet200Response from a JSON string
key_get200_response_instance = KeyGet200Response.from_json(json)
# print the JSON string representation of the object
print(KeyGet200Response.to_json())

# convert the object into a dict
key_get200_response_dict = key_get200_response_instance.to_dict()
# create an instance of KeyGet200Response from a dict
key_get200_response_from_dict = KeyGet200Response.from_dict(key_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


