# MarketGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itemmarket** | [**ItemMarket**](ItemMarket.md) |  | 
**metadata** | [**RequestMetadataWithLinks**](RequestMetadataWithLinks.md) |  | 
**selections** | [**List[MarketSelectionName]**](MarketSelectionName.md) |  | 
**timestamp** | **int** |  | 

## Example

```python
from tornclient.models.market_get200_response import MarketGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MarketGet200Response from a JSON string
market_get200_response_instance = MarketGet200Response.from_json(json)
# print the JSON string representation of the object
print(MarketGet200Response.to_json())

# convert the object into a dict
market_get200_response_dict = market_get200_response_instance.to_dict()
# create an instance of MarketGet200Response from a dict
market_get200_response_from_dict = MarketGet200Response.from_dict(market_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


