# ItemMarketListingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **int** |  | 
**amount** | **int** |  | 
**item_details** | [**ItemMarketListingItemDetails**](ItemMarketListingItemDetails.md) | This field used camelCase instead of snake_case by accident and is replaced with &#39;item_details&#39; field. This will be removed on 1st of May 2025. | [optional] 
**item_details** | [**ItemMarketListingItemDetails**](ItemMarketListingItemDetails.md) |  | 

## Example

```python
from tornclient.models.item_market_listings_inner import ItemMarketListingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMarketListingsInner from a JSON string
item_market_listings_inner_instance = ItemMarketListingsInner.from_json(json)
# print the JSON string representation of the object
print(ItemMarketListingsInner.to_json())

# convert the object into a dict
item_market_listings_inner_dict = item_market_listings_inner_instance.to_dict()
# create an instance of ItemMarketListingsInner from a dict
item_market_listings_inner_from_dict = ItemMarketListingsInner.from_dict(item_market_listings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


