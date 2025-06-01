# FactionGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hof** | [**FactionHofStats**](FactionHofStats.md) |  | 
**members** | [**List[FactionMember]**](FactionMember.md) |  | 
**basic** | [**FactionBasic**](FactionBasic.md) |  | 
**pacts** | [**List[FactionPact]**](FactionPact.md) |  | 
**wars** | [**FactionWars**](FactionWars.md) |  | 
**news** | [**List[FactionNews]**](FactionNews.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 
**revives** | [**List[ReviveSimplified]**](ReviveSimplified.md) |  | 
**territorywars** | [**FactionTerritoryWarsResponseTerritorywars**](FactionTerritoryWarsResponseTerritorywars.md) |  | 
**attacks** | [**List[AttackSimplified]**](AttackSimplified.md) |  | 
**balance** | [**FactionBalance**](FactionBalance.md) |  | 
**territoryownership** | [**List[FactionTerritoryOwnership]**](FactionTerritoryOwnership.md) |  | 
**positions** | [**List[FactionPosition]**](FactionPosition.md) |  | 
**applications** | [**List[FactionApplication]**](FactionApplication.md) |  | 
**chain** | [**FactionOngoingChain**](FactionOngoingChain.md) |  | 
**chains** | [**List[FactionChain]**](FactionChain.md) |  | 
**chainreport** | [**FactionChainReport**](FactionChainReport.md) |  | 
**crimes** | [**List[FactionCrime]**](FactionCrime.md) |  | 
**crime** | [**FactionCrime**](FactionCrime.md) |  | 
**rankedwarreport** | [**FactionRankedWarReportResponseRankedwarreport**](FactionRankedWarReportResponseRankedwarreport.md) |  | 
**territorywarreport** | [**List[FactionTerritoryWarReport]**](FactionTerritoryWarReport.md) |  | 
**territory** | [**List[FactionTerritory]**](FactionTerritory.md) |  | 
**upgrades** | [**FactionUpgrades**](FactionUpgrades.md) |  | 
**state** | [**FactionBranchStateEnum**](FactionBranchStateEnum.md) |  | 
**stats** | [**List[FactionStat]**](FactionStat.md) |  | 
**contributors** | [**List[FactionContributor]**](FactionContributor.md) |  | 
**rackets** | [**List[TornRacket]**](TornRacket.md) |  | 
**rankedwars** | [**List[FactionRankedWarDetails]**](FactionRankedWarDetails.md) |  | 
**selections** | [**List[FactionSelectionName]**](FactionSelectionName.md) |  | 
**timestamp** | **int** |  | 

## Example

```python
from tornclient.models.faction_get200_response import FactionGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FactionGet200Response from a JSON string
faction_get200_response_instance = FactionGet200Response.from_json(json)
# print the JSON string representation of the object
print(FactionGet200Response.to_json())

# convert the object into a dict
faction_get200_response_dict = faction_get200_response_instance.to_dict()
# create an instance of FactionGet200Response from a dict
faction_get200_response_from_dict = FactionGet200Response.from_dict(faction_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


