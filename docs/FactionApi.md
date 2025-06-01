# openapi_client.FactionApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**faction_applications_get**](FactionApi.md#faction_applications_get) | **GET** /faction/applications | Get your faction&#39;s applications
[**faction_attacks_get**](FactionApi.md#faction_attacks_get) | **GET** /faction/attacks | Get your faction&#39;s detailed attacks
[**faction_attacksfull_get**](FactionApi.md#faction_attacksfull_get) | **GET** /faction/attacksfull | Get your faction&#39;s simplified attacks
[**faction_balance_get**](FactionApi.md#faction_balance_get) | **GET** /faction/balance | Get your faction&#39;s &amp; member&#39;s balance details
[**faction_basic_get**](FactionApi.md#faction_basic_get) | **GET** /faction/basic | Get your faction&#39;s basic details
[**faction_chain_get**](FactionApi.md#faction_chain_get) | **GET** /faction/chain | Get your faction&#39;s current chain
[**faction_chain_id_chainreport_get**](FactionApi.md#faction_chain_id_chainreport_get) | **GET** /faction/{chainId}/chainreport | Get a chain report
[**faction_chainreport_get**](FactionApi.md#faction_chainreport_get) | **GET** /faction/chainreport | Get your faction&#39;s latest chain report
[**faction_chains_get**](FactionApi.md#faction_chains_get) | **GET** /faction/chains | Get a list of your faction&#39;s completed chains
[**faction_contributors_get**](FactionApi.md#faction_contributors_get) | **GET** /faction/contributors | Get your faction&#39;s challenge contributors
[**faction_crime_id_crime_get**](FactionApi.md#faction_crime_id_crime_get) | **GET** /faction/{crimeId}/crime | Get a specific organized crime
[**faction_crimes_get**](FactionApi.md#faction_crimes_get) | **GET** /faction/crimes | Get your faction&#39;s organized crimes
[**faction_get**](FactionApi.md#faction_get) | **GET** /faction | Get any Faction selection
[**faction_hof_get**](FactionApi.md#faction_hof_get) | **GET** /faction/hof | Get your faction&#39;s hall of fame rankings.
[**faction_id_basic_get**](FactionApi.md#faction_id_basic_get) | **GET** /faction/{id}/basic | Get a faction&#39;s basic details
[**faction_id_chain_get**](FactionApi.md#faction_id_chain_get) | **GET** /faction/{id}/chain | Get a faction&#39;s current chain
[**faction_id_chains_get**](FactionApi.md#faction_id_chains_get) | **GET** /faction/{id}/chains | Get a list of a faction&#39;s completed chains
[**faction_id_hof_get**](FactionApi.md#faction_id_hof_get) | **GET** /faction/{id}/hof | Get a faction&#39;s hall of fame rankings.
[**faction_id_members_get**](FactionApi.md#faction_id_members_get) | **GET** /faction/{id}/members | Get a list of a faction&#39;s members
[**faction_id_rankedwars_get**](FactionApi.md#faction_id_rankedwars_get) | **GET** /faction/{id}/rankedwars | Get a faction&#39;s ranked wars history
[**faction_id_territory_get**](FactionApi.md#faction_id_territory_get) | **GET** /faction/{id}/territory | Get a list of a faction&#39;s territories
[**faction_id_territorywars_get**](FactionApi.md#faction_id_territorywars_get) | **GET** /faction/{id}/territorywars | Get a faction&#39;s territory wars history
[**faction_id_wars_get**](FactionApi.md#faction_id_wars_get) | **GET** /faction/{id}/wars | Get a faction&#39;s wars &amp; pacts details
[**faction_lookup_get**](FactionApi.md#faction_lookup_get) | **GET** /faction/lookup | 
[**faction_members_get**](FactionApi.md#faction_members_get) | **GET** /faction/members | Get a list of your faction&#39;s members
[**faction_news_get**](FactionApi.md#faction_news_get) | **GET** /faction/news | Get your faction&#39;s news details
[**faction_positions_get**](FactionApi.md#faction_positions_get) | **GET** /faction/positions | Get your faction&#39;s positions details
[**faction_rackets_get**](FactionApi.md#faction_rackets_get) | **GET** /faction/rackets | Get a list of current rackets
[**faction_ranked_war_id_rankedwarreport_get**](FactionApi.md#faction_ranked_war_id_rankedwarreport_get) | **GET** /faction/{rankedWarId}/rankedwarreport | Get ranked war details
[**faction_rankedwars_get**](FactionApi.md#faction_rankedwars_get) | **GET** /faction/rankedwars | Get ranked wars list
[**faction_revives_full_get**](FactionApi.md#faction_revives_full_get) | **GET** /faction/revivesFull | Get your faction&#39;s simplified revives
[**faction_revives_get**](FactionApi.md#faction_revives_get) | **GET** /faction/revives | Get your faction&#39;s detailed revives
[**faction_stats_get**](FactionApi.md#faction_stats_get) | **GET** /faction/stats | Get your faction&#39;s challenges stats
[**faction_territory_get**](FactionApi.md#faction_territory_get) | **GET** /faction/territory | Get a list of your faction&#39;s territories
[**faction_territory_war_id_territorywarreport_get**](FactionApi.md#faction_territory_war_id_territorywarreport_get) | **GET** /faction/{territoryWarId}/territorywarreport | Get territory war details
[**faction_territoryownership_get**](FactionApi.md#faction_territoryownership_get) | **GET** /faction/territoryownership | Get a list of your faction&#39;s territories
[**faction_territorywars_get**](FactionApi.md#faction_territorywars_get) | **GET** /faction/territorywars | Get territory wars list
[**faction_timestamp_get**](FactionApi.md#faction_timestamp_get) | **GET** /faction/timestamp | Get current server time
[**faction_upgrades_get**](FactionApi.md#faction_upgrades_get) | **GET** /faction/upgrades | Get your faction&#39;s upgrades
[**faction_wars_get**](FactionApi.md#faction_wars_get) | **GET** /faction/wars | Get your faction&#39;s wars &amp; pacts details


# **faction_applications_get**
> FactionApplicationsResponse faction_applications_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's applications

Requires minimal access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_applications_response import FactionApplicationsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's applications
        api_response = api_instance.faction_applications_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_applications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_applications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionApplicationsResponse**](FactionApplicationsResponse.md)

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

# **faction_attacks_get**
> FactionAttacksResponse faction_attacks_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)

Get your faction's detailed attacks

Requires limited access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_attacks_response import FactionAttacksResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's detailed attacks
        api_response = api_instance.faction_attacks_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_attacks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_attacks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Limited).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionAttacksResponse**](FactionAttacksResponse.md)

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

# **faction_attacksfull_get**
> FactionAttacksFullResponse faction_attacksfull_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)

Get your faction's simplified attacks

Requires limited access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_attacks_full_response import FactionAttacksFullResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    limit = 1000 # int |  (optional) (default to 1000)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's simplified attacks
        api_response = api_instance.faction_attacksfull_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_attacksfull_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_attacksfull_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 1000]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Limited).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionAttacksFullResponse**](FactionAttacksFullResponse.md)

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

# **faction_balance_get**
> FactionBalanceResponse faction_balance_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's & member's balance details

Requires limited access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_balance_response import FactionBalanceResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's & member's balance details
        api_response = api_instance.faction_balance_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_balance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_balance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Limited).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionBalanceResponse**](FactionBalanceResponse.md)

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

# **faction_basic_get**
> FactionBasicResponse faction_basic_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's basic details

Requires public access key. <br> The 'is_enlisted' value will be populated if you have API faction permissions (with custom, limited or full access keys), otherwise it will be set as null.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_basic_response import FactionBasicResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's basic details
        api_response = api_instance.faction_basic_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_basic_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_basic_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionBasicResponse**](FactionBasicResponse.md)

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

# **faction_chain_get**
> FactionOngoingChainResponse faction_chain_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's current chain

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_ongoing_chain_response import FactionOngoingChainResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's current chain
        api_response = api_instance.faction_chain_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_chain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_chain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionOngoingChainResponse**](FactionOngoingChainResponse.md)

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

# **faction_chain_id_chainreport_get**
> FactionChainReportResponse faction_chain_id_chainreport_get(chain_id, timestamp=timestamp, comment=comment, key=key)

Get a chain report

Requires public access key. <br> Chain reports for ongoing chains are available only for your own faction.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_chain_report_response import FactionChainReportResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    chain_id = 56 # int | Chain id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a chain report
        api_response = api_instance.faction_chain_id_chainreport_get(chain_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_chain_id_chainreport_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_chain_id_chainreport_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **int**| Chain id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionChainReportResponse**](FactionChainReportResponse.md)

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

# **faction_chainreport_get**
> FactionChainReportResponse faction_chainreport_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's latest chain report

Requires public access key. <br> This includes currently ongoing chains.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_chain_report_response import FactionChainReportResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's latest chain report
        api_response = api_instance.faction_chainreport_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_chainreport_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_chainreport_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionChainReportResponse**](FactionChainReportResponse.md)

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

# **faction_chains_get**
> FactionChainsResponse faction_chains_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)

Get a list of your faction's completed chains

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_chains_response import FactionChainsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a list of your faction's completed chains
        api_response = api_instance.faction_chains_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_chains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_chains_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionChainsResponse**](FactionChainsResponse.md)

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

# **faction_contributors_get**
> FactionContributorsResponse faction_contributors_get(stat, cat=cat, timestamp=timestamp, comment=comment, key=key)

Get your faction's challenge contributors

Requires limiteed access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_contributors_response import FactionContributorsResponse
from tornclient.models.faction_stat_enum import FactionStatEnum
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
    api_instance = openapi_client.FactionApi(api_client)
    stat = openapi_client.FactionStatEnum() # FactionStatEnum | Get contributors for this field.
    cat = 'cat_example' # str | By default, this selection will return only current faction's member contributions, and the option 'all' will return all contributors. (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's challenge contributors
        api_response = api_instance.faction_contributors_get(stat, cat=cat, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_contributors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_contributors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat** | [**FactionStatEnum**](.md)| Get contributors for this field. | 
 **cat** | **str**| By default, this selection will return only current faction&#39;s member contributions, and the option &#39;all&#39; will return all contributors. | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionContributorsResponse**](FactionContributorsResponse.md)

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

# **faction_crime_id_crime_get**
> FactionCrimeResponse faction_crime_id_crime_get(crime_id, timestamp=timestamp, comment=comment, key=key)

Get a specific organized crime

Requires minimal access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_crime_response import FactionCrimeResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    crime_id = 56 # int | Crime id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a specific organized crime
        api_response = api_instance.faction_crime_id_crime_get(crime_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_crime_id_crime_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_crime_id_crime_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crime_id** | **int**| Crime id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionCrimeResponse**](FactionCrimeResponse.md)

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

# **faction_crimes_get**
> FactionCrimesResponse faction_crimes_get(cat=cat, offset=offset, var_from=var_from, to=to, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get your faction's organized crimes

Requires minimal access key with faction API access permissions. <br> It's possible to get older entries either by timestamp range (from, to) or with offset.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_crimes_response import FactionCrimesResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    cat = 'cat_example' # str | Category of organized crimes returned. Category 'available' includes both 'recruiting' & 'planning', and category 'completed' includes both 'successful' & 'failure'<br>Default category is 'all' (optional)
    offset = 0 # int |  (optional) (default to 0)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's organized crimes
        api_response = api_instance.faction_crimes_get(cat=cat, offset=offset, var_from=var_from, to=to, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_crimes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_crimes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | **str**| Category of organized crimes returned. Category &#39;available&#39; includes both &#39;recruiting&#39; &amp; &#39;planning&#39;, and category &#39;completed&#39; includes both &#39;successful&#39; &amp; &#39;failure&#39;&lt;br&gt;Default category is &#39;all&#39; | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionCrimesResponse**](FactionCrimesResponse.md)

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

# **faction_get**
> FactionGet200Response faction_get(selections=selections, id=id, limit=limit, var_from=var_from, to=to, cat=cat, stat=stat, striptags=striptags, sort=sort, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Faction selection

Key access level depends on the required selections. <br> Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_get200_response import FactionGet200Response
from tornclient.models.faction_selection_name import FactionSelectionName
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
    api_instance = openapi_client.FactionApi(api_client)
    selections = [openapi_client.FactionSelectionName()] # List[FactionSelectionName] | Selection names (optional)
    id = 'id_example' # str | selection id (optional)
    limit = 56 # int |  (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    cat = 'cat_example' # str | Selection category (optional)
    stat = 'stat_example' # str | Stat category (optional)
    striptags = 'striptags_example' # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Faction selection
        api_response = api_instance.faction_get(selections=selections, id=id, limit=limit, var_from=var_from, to=to, cat=cat, stat=stat, striptags=striptags, sort=sort, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[FactionSelectionName]**](FactionSelectionName.md)| Selection names | [optional] 
 **id** | **str**| selection id | [optional] 
 **limit** | **int**|  | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **cat** | **str**| Selection category | [optional] 
 **stat** | **str**| Stat category | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionGet200Response**](FactionGet200Response.md)

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

# **faction_hof_get**
> FactionHofResponse faction_hof_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's hall of fame rankings.

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_hof_response import FactionHofResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's hall of fame rankings.
        api_response = api_instance.faction_hof_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_hof_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_hof_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionHofResponse**](FactionHofResponse.md)

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

# **faction_id_basic_get**
> FactionBasicResponse faction_id_basic_get(id, timestamp=timestamp, comment=comment, key=key)

Get a faction's basic details

Requires public access key. <br> The 'is_enlisted' value will be populated if you're requesting data for your faction and have faction permissions (with custom, limited or full access keys), otherwise it will be set as null.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_basic_response import FactionBasicResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a faction's basic details
        api_response = api_instance.faction_id_basic_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_basic_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_basic_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionBasicResponse**](FactionBasicResponse.md)

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

# **faction_id_chain_get**
> FactionOngoingChainResponse faction_id_chain_get(id, timestamp=timestamp, comment=comment, key=key)

Get a faction's current chain

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_ongoing_chain_response import FactionOngoingChainResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a faction's current chain
        api_response = api_instance.faction_id_chain_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_chain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_chain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionOngoingChainResponse**](FactionOngoingChainResponse.md)

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

# **faction_id_chains_get**
> FactionChainsResponse faction_id_chains_get(id, limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)

Get a list of a faction's completed chains

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_chains_response import FactionChainsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    limit = 100 # int |  (optional) (default to 100)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a list of a faction's completed chains
        api_response = api_instance.faction_id_chains_get(id, limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_chains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_chains_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionChainsResponse**](FactionChainsResponse.md)

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

# **faction_id_hof_get**
> FactionHofResponse faction_id_hof_get(id, timestamp=timestamp, comment=comment, key=key)

Get a faction's hall of fame rankings.

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_hof_response import FactionHofResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a faction's hall of fame rankings.
        api_response = api_instance.faction_id_hof_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_hof_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_hof_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionHofResponse**](FactionHofResponse.md)

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

# **faction_id_members_get**
> FactionMembersResponse faction_id_members_get(id, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get a list of a faction's members

Requires public access key. <br> The 'revive_setting' value will be populated (not Unknown) if you're requesting data for your own faction and have faction permissions (with custom, limited or full access keys), otherwise it will be set as 'Unknown'.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_members_response import FactionMembersResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a list of a faction's members
        api_response = api_instance.faction_id_members_get(id, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionMembersResponse**](FactionMembersResponse.md)

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

# **faction_id_rankedwars_get**
> FactionRankedWarResponse faction_id_rankedwars_get(id, timestamp=timestamp, comment=comment, key=key)

Get a faction's ranked wars history

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_ranked_war_response import FactionRankedWarResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a faction's ranked wars history
        api_response = api_instance.faction_id_rankedwars_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_rankedwars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_rankedwars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionRankedWarResponse**](FactionRankedWarResponse.md)

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

# **faction_id_territory_get**
> FactionTerritoriesReponse faction_id_territory_get(id, timestamp=timestamp, comment=comment, key=key)

Get a list of a faction's territories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_territories_reponse import FactionTerritoriesReponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a list of a faction's territories
        api_response = api_instance.faction_id_territory_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_territory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_territory_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionTerritoriesReponse**](FactionTerritoriesReponse.md)

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

# **faction_id_territorywars_get**
> FactionTerritoryWarsHistoryResponse faction_id_territorywars_get(id, timestamp=timestamp, comment=comment, key=key)

Get a faction's territory wars history

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_territory_wars_history_response import FactionTerritoryWarsHistoryResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a faction's territory wars history
        api_response = api_instance.faction_id_territorywars_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_territorywars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_territorywars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionTerritoryWarsHistoryResponse**](FactionTerritoryWarsHistoryResponse.md)

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

# **faction_id_wars_get**
> FactionWarsResponse faction_id_wars_get(id, timestamp=timestamp, comment=comment, key=key)

Get a faction's wars & pacts details

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_wars_response import FactionWarsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    id = 56 # int | Faction id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a faction's wars & pacts details
        api_response = api_instance.faction_id_wars_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_id_wars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_id_wars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Faction id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionWarsResponse**](FactionWarsResponse.md)

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

# **faction_lookup_get**
> FactionLookupResponse faction_lookup_get(timestamp=timestamp, comment=comment, key=key)

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_lookup_response import FactionLookupResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        api_response = api_instance.faction_lookup_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_lookup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_lookup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionLookupResponse**](FactionLookupResponse.md)

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

# **faction_members_get**
> FactionMembersResponse faction_members_get(striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get a list of your faction's members

Requires public access key. <br> The 'revive_setting' value will be populated (not Unknown) if you have faction permissions (with custom, limited or full access keys), otherwise it will be set as 'Unknown'.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_members_response import FactionMembersResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a list of your faction's members
        api_response = api_instance.faction_members_get(striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionMembersResponse**](FactionMembersResponse.md)

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

# **faction_news_get**
> FactionNewsResponse faction_news_get(cat, striptags=striptags, limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)

Get your faction's news details

Requires minimal access key with faction API access permissions. <br> It is possible to pass up to 10 categories at the time (comma separated). Categories 'attack', 'depositFunds' and 'giveFunds' are only available with 'Custom', 'Limited' or 'Full' access keys.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_news_category import FactionNewsCategory
from tornclient.models.faction_news_response import FactionNewsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    cat = openapi_client.FactionNewsCategory() # FactionNewsCategory | News category type
    striptags = false # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to false)
    limit = 100 # int |  (optional) (default to 100)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's news details
        api_response = api_instance.faction_news_get(cat, striptags=striptags, limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_news_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_news_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**FactionNewsCategory**](.md)| News category type | 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to false]
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionNewsResponse**](FactionNewsResponse.md)

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

# **faction_positions_get**
> FactionPositionsResponse faction_positions_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's positions details

Requires minimal access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_positions_response import FactionPositionsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's positions details
        api_response = api_instance.faction_positions_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_positions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_positions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionPositionsResponse**](FactionPositionsResponse.md)

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

# **faction_rackets_get**
> FactionRacketsReponse faction_rackets_get(timestamp=timestamp, comment=comment, key=key)

Get a list of current rackets

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_rackets_reponse import FactionRacketsReponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a list of current rackets
        api_response = api_instance.faction_rackets_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_rackets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_rackets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionRacketsReponse**](FactionRacketsReponse.md)

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

# **faction_ranked_war_id_rankedwarreport_get**
> FactionRankedWarReportResponse faction_ranked_war_id_rankedwarreport_get(ranked_war_id, timestamp=timestamp, comment=comment, key=key)

Get ranked war details

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_ranked_war_report_response import FactionRankedWarReportResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    ranked_war_id = 56 # int | Ranked war id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get ranked war details
        api_response = api_instance.faction_ranked_war_id_rankedwarreport_get(ranked_war_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_ranked_war_id_rankedwarreport_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_ranked_war_id_rankedwarreport_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranked_war_id** | **int**| Ranked war id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionRankedWarReportResponse**](FactionRankedWarReportResponse.md)

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

# **faction_rankedwars_get**
> FactionRankedWarResponse faction_rankedwars_get(cat=cat, var_from=var_from, to=to, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get ranked wars list

Requires public access key. <br> When category 'all' is chosen, you can use 'from', 'to' & 'sort' query parameters.<br>When category 'ongoing' is chosen, all currently active ranked wars are returned.<br>When no category is chosen, this selection will return ranked war history of your own faction (if any).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_ranked_war_response import FactionRankedWarResponse
from tornclient.models.faction_ranked_wars_category_enum import FactionRankedWarsCategoryEnum
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
    api_instance = openapi_client.FactionApi(api_client)
    cat = openapi_client.FactionRankedWarsCategoryEnum() # FactionRankedWarsCategoryEnum |  (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get ranked wars list
        api_response = api_instance.faction_rankedwars_get(cat=cat, var_from=var_from, to=to, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_rankedwars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_rankedwars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**FactionRankedWarsCategoryEnum**](.md)|  | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionRankedWarResponse**](FactionRankedWarResponse.md)

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

# **faction_revives_full_get**
> RevivesFullResponse faction_revives_full_get(limit=limit, sort=sort, to=to, var_from=var_from, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get your faction's simplified revives

Requires limited access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.revives_full_response import RevivesFullResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    limit = 1000 # int |  (optional) (default to 1000)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's simplified revives
        api_response = api_instance.faction_revives_full_get(limit=limit, sort=sort, to=to, var_from=var_from, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_revives_full_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_revives_full_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 1000]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Limited).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RevivesFullResponse**](RevivesFullResponse.md)

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

# **faction_revives_get**
> RevivesResponse faction_revives_get(limit=limit, sort=sort, to=to, var_from=var_from, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get your faction's detailed revives

Requires limited access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.revives_response import RevivesResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's detailed revives
        api_response = api_instance.faction_revives_get(limit=limit, sort=sort, to=to, var_from=var_from, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_revives_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_revives_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Limited).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RevivesResponse**](RevivesResponse.md)

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

# **faction_stats_get**
> FactionStatsResponse faction_stats_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's challenges stats

Requires minimal access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_stats_response import FactionStatsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's challenges stats
        api_response = api_instance.faction_stats_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionStatsResponse**](FactionStatsResponse.md)

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

# **faction_territory_get**
> FactionTerritoriesReponse faction_territory_get(timestamp=timestamp, comment=comment, key=key)

Get a list of your faction's territories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_territories_reponse import FactionTerritoriesReponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a list of your faction's territories
        api_response = api_instance.faction_territory_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_territory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_territory_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionTerritoriesReponse**](FactionTerritoriesReponse.md)

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

# **faction_territory_war_id_territorywarreport_get**
> FactionTerritoryWarReportResponse faction_territory_war_id_territorywarreport_get(territory_war_id, timestamp=timestamp, comment=comment, key=key)

Get territory war details

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_territory_war_report_response import FactionTerritoryWarReportResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    territory_war_id = 56 # int | Territory war id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get territory war details
        api_response = api_instance.faction_territory_war_id_territorywarreport_get(territory_war_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_territory_war_id_territorywarreport_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_territory_war_id_territorywarreport_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **territory_war_id** | **int**| Territory war id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionTerritoryWarReportResponse**](FactionTerritoryWarReportResponse.md)

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

# **faction_territoryownership_get**
> FactionTerritoriesOwnershipResponse faction_territoryownership_get(offset=offset, limit=limit, timestamp=timestamp, comment=comment, key=key)

Get a list of your faction's territories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_territories_ownership_response import FactionTerritoriesOwnershipResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 20 # int |  (optional) (default to 20)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a list of your faction's territories
        api_response = api_instance.faction_territoryownership_get(offset=offset, limit=limit, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_territoryownership_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_territoryownership_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionTerritoriesOwnershipResponse**](FactionTerritoriesOwnershipResponse.md)

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

# **faction_territorywars_get**
> FactionTerritoryWarsResponse faction_territorywars_get(cat=cat, var_from=var_from, to=to, sort=sort, limit=limit, timestamp=timestamp, comment=comment, key=key)

Get territory wars list

Requires public access key. <br> When category 'finished' is chosen, you can use 'from', 'to' & 'sort' query parameters.<br>When category 'ongoing' is chosen, all currently active territory wars are returned.<br>When no category is chosen, this selection will return territory war history of your own faction (if any).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_territory_wars_category_enum import FactionTerritoryWarsCategoryEnum
from tornclient.models.faction_territory_wars_response import FactionTerritoryWarsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    cat = openapi_client.FactionTerritoryWarsCategoryEnum() # FactionTerritoryWarsCategoryEnum |  (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    limit = 100 # int |  (optional) (default to 100)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get territory wars list
        api_response = api_instance.faction_territorywars_get(cat=cat, var_from=var_from, to=to, sort=sort, limit=limit, timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_territorywars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_territorywars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**FactionTerritoryWarsCategoryEnum**](.md)|  | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **limit** | **int**|  | [optional] [default to 100]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionTerritoryWarsResponse**](FactionTerritoryWarsResponse.md)

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

# **faction_timestamp_get**
> TimestampResponse faction_timestamp_get(timestamp=timestamp, comment=comment, key=key)

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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.faction_timestamp_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_timestamp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_timestamp_get: %s\n" % e)
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

# **faction_upgrades_get**
> FactionUpgradesResponse faction_upgrades_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's upgrades

Requires minimal access key with faction API access permissions. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_upgrades_response import FactionUpgradesResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's upgrades
        api_response = api_instance.faction_upgrades_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_upgrades_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_upgrades_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionUpgradesResponse**](FactionUpgradesResponse.md)

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

# **faction_wars_get**
> FactionWarsResponse faction_wars_get(timestamp=timestamp, comment=comment, key=key)

Get your faction's wars & pacts details

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_wars_response import FactionWarsResponse
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
    api_instance = openapi_client.FactionApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your faction's wars & pacts details
        api_response = api_instance.faction_wars_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of FactionApi->faction_wars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionApi->faction_wars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**FactionWarsResponse**](FactionWarsResponse.md)

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

