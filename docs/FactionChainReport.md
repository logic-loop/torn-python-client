# FactionChainReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**faction_id** | **int** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**details** | [**FactionChainReportDetails**](FactionChainReportDetails.md) |  | 
**bonuses** | [**List[FactionChainReportBonus]**](FactionChainReportBonus.md) |  | 
**attackers** | [**List[FactionChainReportAttacker]**](FactionChainReportAttacker.md) |  | 
**non_attackers** | **List[int]** | This is replaced with &#39;sci_fi&#39; field and will be removed on 1st June 2025. | [optional] 
**non_attackers** | **List[int]** |  | 

## Example

```python
from tornclient.models.faction_chain_report import FactionChainReport

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChainReport from a JSON string
faction_chain_report_instance = FactionChainReport.from_json(json)
# print the JSON string representation of the object
print(FactionChainReport.to_json())

# convert the object into a dict
faction_chain_report_dict = faction_chain_report_instance.to_dict()
# create an instance of FactionChainReport from a dict
faction_chain_report_from_dict = FactionChainReport.from_dict(faction_chain_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


