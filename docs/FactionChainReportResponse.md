# FactionChainReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chainreport** | [**FactionChainReport**](FactionChainReport.md) |  | 

## Example

```python
from tornclient.models.faction_chain_report_response import FactionChainReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactionChainReportResponse from a JSON string
faction_chain_report_response_instance = FactionChainReportResponse.from_json(json)
# print the JSON string representation of the object
print(FactionChainReportResponse.to_json())

# convert the object into a dict
faction_chain_report_response_dict = faction_chain_report_response_instance.to_dict()
# create an instance of FactionChainReportResponse from a dict
faction_chain_report_response_from_dict = FactionChainReportResponse.from_dict(faction_chain_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


