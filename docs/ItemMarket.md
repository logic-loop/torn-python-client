# ItemMarket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**ItemMarketItem**](ItemMarketItem.md) |  | 
**listings** | [**List[ItemMarketListingsInner]**](ItemMarketListingsInner.md) |  | 

## Example

```python
from tornclient.models.item_market import ItemMarket

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMarket from a JSON string
item_market_instance = ItemMarket.from_json(json)
# print the JSON string representation of the object
print(ItemMarket.to_json())

# convert the object into a dict
item_market_dict = item_market_instance.to_dict()
# create an instance of ItemMarket from a dict
item_market_from_dict = ItemMarket.from_dict(item_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


