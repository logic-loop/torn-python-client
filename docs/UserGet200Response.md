# UserGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crimes** | [**UserCrime**](UserCrime.md) |  | 
**races** | [**List[RacingRaceDetailsResponse]**](RacingRaceDetailsResponse.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 
**enlistedcars** | [**List[UserRaceCarDetails]**](UserRaceCarDetails.md) |  | 
**forum_posts** | [**List[ForumPost]**](ForumPost.md) |  | 
**forum_threads** | [**List[ForumThreadUserExtended]**](ForumThreadUserExtended.md) |  | 
**forum_subscribed_threads** | [**List[ForumSubscribedThread]**](ForumSubscribedThread.md) |  | [optional] 
**forum_feed** | [**List[ForumFeed]**](ForumFeed.md) |  | 
**forum_friends** | [**List[ForumFeed]**](ForumFeed.md) |  | 
**hof** | [**UserHofStats**](UserHofStats.md) |  | 
**calendar** | [**UserCalendar**](UserCalendar.md) |  | 
**education** | [**UserEducation**](UserEducation.md) |  | 
**bounties** | [**List[Bounty]**](Bounty.md) |  | 
**jobranks** | [**UserJobRanks**](UserJobRanks.md) |  | 
**faction_balance** | [**UserFactionBalance**](UserFactionBalance.md) |  | 
**revives** | [**List[ReviveSimplified]**](ReviveSimplified.md) |  | 
**itemmarket** | [**List[UserItemMarketListing]**](UserItemMarketListing.md) |  | 
**list** | [**List[UserList]**](UserList.md) |  | 
**personalstats** | [**List[PersonalStatsHistoricStat]**](PersonalStatsHistoricStat.md) |  | 
**organized_crime** | [**FactionCrime**](FactionCrime.md) |  | 
**attacks** | [**List[AttackSimplified]**](AttackSimplified.md) |  | 
**selections** | [**List[UserSelectionName]**](UserSelectionName.md) |  | 
**timestamp** | **int** |  | 

## Example

```python
from tornclient.models.user_get200_response import UserGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGet200Response from a JSON string
user_get200_response_instance = UserGet200Response.from_json(json)
# print the JSON string representation of the object
print(UserGet200Response.to_json())

# convert the object into a dict
user_get200_response_dict = user_get200_response_instance.to_dict()
# create an instance of UserGet200Response from a dict
user_get200_response_from_dict = UserGet200Response.from_dict(user_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


