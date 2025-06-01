# ForumGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[ForumCategoriesResponseCategoriesInner]**](ForumCategoriesResponseCategoriesInner.md) |  | 
**threads** | [**List[ForumThreadBase]**](ForumThreadBase.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 
**thread** | [**ForumThreadExtended**](ForumThreadExtended.md) |  | 
**posts** | [**List[ForumPost]**](ForumPost.md) |  | 
**selections** | [**List[ForumSelectionName]**](ForumSelectionName.md) |  | 
**timestamp** | **int** |  | 

## Example

```python
from tornclient.models.forum_get200_response import ForumGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ForumGet200Response from a JSON string
forum_get200_response_instance = ForumGet200Response.from_json(json)
# print the JSON string representation of the object
print(ForumGet200Response.to_json())

# convert the object into a dict
forum_get200_response_dict = forum_get200_response_instance.to_dict()
# create an instance of ForumGet200Response from a dict
forum_get200_response_from_dict = ForumGet200Response.from_dict(forum_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


