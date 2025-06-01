# UserForumThreadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum_threads** | [**List[ForumThreadUserExtended]**](ForumThreadUserExtended.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 

## Example

```python
from tornclient.models.user_forum_threads_response import UserForumThreadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserForumThreadsResponse from a JSON string
user_forum_threads_response_instance = UserForumThreadsResponse.from_json(json)
# print the JSON string representation of the object
print(UserForumThreadsResponse.to_json())

# convert the object into a dict
user_forum_threads_response_dict = user_forum_threads_response_instance.to_dict()
# create an instance of UserForumThreadsResponse from a dict
user_forum_threads_response_from_dict = UserForumThreadsResponse.from_dict(user_forum_threads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


