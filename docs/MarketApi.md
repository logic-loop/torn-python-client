# openapi_client.MarketApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_get**](MarketApi.md#market_get) | **GET** /market | Get any Market selection
[**market_id_itemmarket_get**](MarketApi.md#market_id_itemmarket_get) | **GET** /market/{id}/itemmarket | Get item market listings
[**market_lookup_get**](MarketApi.md#market_lookup_get) | **GET** /market/lookup | Get all available market selections
[**market_timestamp_get**](MarketApi.md#market_timestamp_get) | **GET** /market/timestamp | Get current server time


# **market_get**
> MarketGet200Response market_get(selections=selections, id=id, bonus=bonus, cat=cat, sort=sort, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Market selection

Requires public access key. <br>Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.market_get200_response import MarketGet200Response
from tornclient.models.market_selection_name import MarketSelectionName
from tornclient.models.weapon_bonus_enum import WeaponBonusEnum
from tornclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torn.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.torn.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketApi(api_client)
    selections = [openapi_client.MarketSelectionName()] # List[MarketSelectionName] | Selection names (optional)
    id = 'id_example' # str | selection id (optional)
    bonus = openapi_client.WeaponBonusEnum() # WeaponBonusEnum | Used to filter weapons with a specific bonus (optional)
    cat = 'cat_example' # str | Selection category (optional)
    sort = 'sort_example' # str | Direction to sort rows in (optional)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Market selection
        api_response = api_instance.market_get(selections=selections, id=id, bonus=bonus, cat=cat, sort=sort, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->market_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[MarketSelectionName]**](MarketSelectionName.md)| Selection names | [optional] 
 **id** | **str**| selection id | [optional] 
 **bonus** | [**WeaponBonusEnum**](.md)| Used to filter weapons with a specific bonus | [optional] 
 **cat** | **str**| Selection category | [optional] 
 **sort** | **str**| Direction to sort rows in | [optional] 
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**MarketGet200Response**](MarketGet200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_id_itemmarket_get**
> MarketItemMarketResponse market_id_itemmarket_get(id, bonus=bonus, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get item market listings

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.market_item_market_response import MarketItemMarketResponse
from tornclient.models.weapon_bonus_enum import WeaponBonusEnum
from tornclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torn.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.torn.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketApi(api_client)
    id = 56 # int | Item id
    bonus = openapi_client.WeaponBonusEnum() # WeaponBonusEnum | Used to filter weapons with a specific bonus. (optional)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get item market listings
        api_response = api_instance.market_id_itemmarket_get(id, bonus=bonus, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->market_id_itemmarket_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_id_itemmarket_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 
 **bonus** | [**WeaponBonusEnum**](.md)| Used to filter weapons with a specific bonus. | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**MarketItemMarketResponse**](MarketItemMarketResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_lookup_get**
> MarketLookupResponse market_lookup_get(timestamp=timestamp, comment=comment, key=key)

Get all available market selections

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.market_lookup_response import MarketLookupResponse
from tornclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torn.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.torn.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available market selections
        api_response = api_instance.market_lookup_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->market_lookup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_lookup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**MarketLookupResponse**](MarketLookupResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_timestamp_get**
> TimestampResponse market_timestamp_get(timestamp=timestamp, comment=comment, key=key)

Get current server time

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.timestamp_response import TimestampResponse
from tornclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torn.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.torn.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.market_timestamp_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->market_timestamp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_timestamp_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TimestampResponse**](TimestampResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

