# openapi_client.TornApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**torn_attacklog_get**](TornApi.md#torn_attacklog_get) | **GET** /torn/attacklog | Get attack log details
[**torn_bounties_get**](TornApi.md#torn_bounties_get) | **GET** /torn/bounties | Get bounties
[**torn_calendar_get**](TornApi.md#torn_calendar_get) | **GET** /torn/calendar | Get calendar information
[**torn_crime_id_subcrimes_get**](TornApi.md#torn_crime_id_subcrimes_get) | **GET** /torn/{crimeId}/subcrimes | Get Subcrimes information
[**torn_crimes_get**](TornApi.md#torn_crimes_get) | **GET** /torn/crimes | Get crimes information
[**torn_education_get**](TornApi.md#torn_education_get) | **GET** /torn/education | Get education information
[**torn_factionhof_get**](TornApi.md#torn_factionhof_get) | **GET** /torn/factionhof | Get faction hall of fame positions for a specific category
[**torn_factiontree_get**](TornApi.md#torn_factiontree_get) | **GET** /torn/factiontree | Get full faction tree
[**torn_get**](TornApi.md#torn_get) | **GET** /torn | Get any Torn selection
[**torn_hof_get**](TornApi.md#torn_hof_get) | **GET** /torn/hof | Get player hall of fame positions for a specific category
[**torn_ids_items_get**](TornApi.md#torn_ids_items_get) | **GET** /torn/{ids}/items | Get information about items
[**torn_itemammo_get**](TornApi.md#torn_itemammo_get) | **GET** /torn/itemammo | Get information about ammo
[**torn_itemmods_get**](TornApi.md#torn_itemmods_get) | **GET** /torn/itemmods | Get information about weapon upgrades
[**torn_items_get**](TornApi.md#torn_items_get) | **GET** /torn/items | Get information about items
[**torn_log_category_id_logtypes_get**](TornApi.md#torn_log_category_id_logtypes_get) | **GET** /torn/{logCategoryId}/logtypes | Get available log ids for a specific log category
[**torn_logcategories_get**](TornApi.md#torn_logcategories_get) | **GET** /torn/logcategories | Get available log categories
[**torn_logtypes_get**](TornApi.md#torn_logtypes_get) | **GET** /torn/logtypes | Get all available log ids
[**torn_lookup_get**](TornApi.md#torn_lookup_get) | **GET** /torn/lookup | Get all available torn selections
[**torn_territory_get**](TornApi.md#torn_territory_get) | **GET** /torn/territory | Get territory details
[**torn_territory_ids_territory_get**](TornApi.md#torn_territory_ids_territory_get) | **GET** /torn/{territoryIds}/territory | Get territory details
[**torn_timestamp_get**](TornApi.md#torn_timestamp_get) | **GET** /torn/timestamp | Get current server time


# **torn_attacklog_get**
> AttackLogResponse torn_attacklog_get(log, offset=offset, sort=sort, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get attack log details

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.attack_log_response import AttackLogResponse
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
    api_instance = openapi_client.TornApi(api_client)
    log = 'log_example' # str | Code of the attack log. E.g. d51ad4fe6be884b309b142e2d1d4f807
    offset = 0 # int |  (optional) (default to 0)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get attack log details
        api_response = api_instance.torn_attacklog_get(log, offset=offset, sort=sort, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_attacklog_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_attacklog_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log** | **str**| Code of the attack log. E.g. d51ad4fe6be884b309b142e2d1d4f807 | 
 **offset** | **int**|  | [optional] [default to 0]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**AttackLogResponse**](AttackLogResponse.md)

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

# **torn_bounties_get**
> TornBountiesResponse torn_bounties_get(limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get bounties

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_bounties_response import TornBountiesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get bounties
        api_response = api_instance.torn_bounties_get(limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_bounties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_bounties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornBountiesResponse**](TornBountiesResponse.md)

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

# **torn_calendar_get**
> TornCalendarResponse torn_calendar_get(timestamp=timestamp, comment=comment, key=key)

Get calendar information

Requires public access key. <br> Get the details about competitions & events in the running year.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_calendar_response import TornCalendarResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get calendar information
        api_response = api_instance.torn_calendar_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_calendar_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_calendar_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornCalendarResponse**](TornCalendarResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **torn_crime_id_subcrimes_get**
> TornSubcrimesResponse torn_crime_id_subcrimes_get(crime_id, timestamp=timestamp, comment=comment, key=key)

Get Subcrimes information

Requires public access key. <br> Return the details about possible actions for a specific crime.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_subcrimes_response import TornSubcrimesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    crime_id = 56 # int | Crime id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get Subcrimes information
        api_response = api_instance.torn_crime_id_subcrimes_get(crime_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_crime_id_subcrimes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_crime_id_subcrimes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crime_id** | **int**| Crime id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornSubcrimesResponse**](TornSubcrimesResponse.md)

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

# **torn_crimes_get**
> TornCrimesResponse torn_crimes_get(timestamp=timestamp, comment=comment, key=key)

Get crimes information

Requires public access key. <br> Return the details about released crimes.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_crimes_response import TornCrimesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get crimes information
        api_response = api_instance.torn_crimes_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_crimes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_crimes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornCrimesResponse**](TornCrimesResponse.md)

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

# **torn_education_get**
> TornEducationResponse torn_education_get(timestamp=timestamp, comment=comment, key=key)

Get education information

Requires public access key.<br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_education_response import TornEducationResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get education information
        api_response = api_instance.torn_education_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_education_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_education_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornEducationResponse**](TornEducationResponse.md)

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

# **torn_factionhof_get**
> TornFactionHofResponse torn_factionhof_get(cat, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get faction hall of fame positions for a specific category

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_faction_hof_category import TornFactionHofCategory
from tornclient.models.torn_faction_hof_response import TornFactionHofResponse
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
    api_instance = openapi_client.TornApi(api_client)
    cat = openapi_client.TornFactionHofCategory() # TornFactionHofCategory | Leaderboards category
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get faction hall of fame positions for a specific category
        api_response = api_instance.torn_factionhof_get(cat, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_factionhof_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_factionhof_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**TornFactionHofCategory**](.md)| Leaderboards category | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornFactionHofResponse**](TornFactionHofResponse.md)

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

# **torn_factiontree_get**
> TornFactionTreeResponse torn_factiontree_get(timestamp=timestamp, comment=comment, key=key)

Get full faction tree

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_faction_tree_response import TornFactionTreeResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get full faction tree
        api_response = api_instance.torn_factiontree_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_factiontree_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_factiontree_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornFactionTreeResponse**](TornFactionTreeResponse.md)

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

# **torn_get**
> TornGet200Response torn_get(selections=selections, id=id, striptags=striptags, limit=limit, to=to, var_from=var_from, sort=sort, cat=cat, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Torn selection

Requires public access key. <br> Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_get200_response import TornGet200Response
from tornclient.models.torn_selection_name import TornSelectionName
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
    api_instance = openapi_client.TornApi(api_client)
    selections = [openapi_client.TornSelectionName()] # List[TornSelectionName] | Selection names (optional)
    id = 'id_example' # str | selection id (optional)
    striptags = 'striptags_example' # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional)
    limit = 56 # int |  (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    cat = 'cat_example' # str | Selection category (optional)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Torn selection
        api_response = api_instance.torn_get(selections=selections, id=id, striptags=striptags, limit=limit, to=to, var_from=var_from, sort=sort, cat=cat, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[TornSelectionName]**](TornSelectionName.md)| Selection names | [optional] 
 **id** | **str**| selection id | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] 
 **limit** | **int**|  | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **cat** | **str**| Selection category | [optional] 
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornGet200Response**](TornGet200Response.md)

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

# **torn_hof_get**
> TornHofResponse torn_hof_get(cat, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get player hall of fame positions for a specific category

Requires public key.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_hof_category import TornHofCategory
from tornclient.models.torn_hof_response import TornHofResponse
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
    api_instance = openapi_client.TornApi(api_client)
    cat = openapi_client.TornHofCategory() # TornHofCategory | Leaderboards category
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get player hall of fame positions for a specific category
        api_response = api_instance.torn_hof_get(cat, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_hof_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_hof_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**TornHofCategory**](.md)| Leaderboards category | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornHofResponse**](TornHofResponse.md)

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

# **torn_ids_items_get**
> TornItemsResponse torn_ids_items_get(ids, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get information about items

Requires public key.<br>Details are always populated when available.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_items_response import TornItemsResponse
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
    api_instance = openapi_client.TornApi(api_client)
    ids = 'ids_example' # str | Item id or a list of item ids (comma separated)
    sort = ASC # str | Sort rows from newest to oldest<br>Default ordering is ascending (optional) (default to ASC)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get information about items
        api_response = api_instance.torn_ids_items_get(ids, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_ids_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_ids_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Item id or a list of item ids (comma separated) | 
 **sort** | **str**| Sort rows from newest to oldest&lt;br&gt;Default ordering is ascending | [optional] [default to ASC]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornItemsResponse**](TornItemsResponse.md)

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

# **torn_itemammo_get**
> TornItemAmmoResponse torn_itemammo_get(timestamp=timestamp, comment=comment, key=key)

Get information about ammo

Requires public key.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_item_ammo_response import TornItemAmmoResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get information about ammo
        api_response = api_instance.torn_itemammo_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_itemammo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_itemammo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornItemAmmoResponse**](TornItemAmmoResponse.md)

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

# **torn_itemmods_get**
> TornItemModsResponse torn_itemmods_get(timestamp=timestamp, comment=comment, key=key)

Get information about weapon upgrades

Requires public key.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_item_mods_response import TornItemModsResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get information about weapon upgrades
        api_response = api_instance.torn_itemmods_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_itemmods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_itemmods_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornItemModsResponse**](TornItemModsResponse.md)

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

# **torn_items_get**
> TornItemsResponse torn_items_get(cat=cat, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get information about items

Requires public key.<br>Default category is 'All'.<br>Details are not populated when requesting the category 'All'.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_item_category import TornItemCategory
from tornclient.models.torn_items_response import TornItemsResponse
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
    api_instance = openapi_client.TornApi(api_client)
    cat = openapi_client.TornItemCategory() # TornItemCategory | Item category type (optional)
    sort = ASC # str | Sort rows from newest to oldest<br>Default ordering is ascending (optional) (default to ASC)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get information about items
        api_response = api_instance.torn_items_get(cat=cat, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**TornItemCategory**](.md)| Item category type | [optional] 
 **sort** | **str**| Sort rows from newest to oldest&lt;br&gt;Default ordering is ascending | [optional] [default to ASC]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornItemsResponse**](TornItemsResponse.md)

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

# **torn_log_category_id_logtypes_get**
> TornLogTypesResponse torn_log_category_id_logtypes_get(log_category_id, timestamp=timestamp, comment=comment, key=key)

Get available log ids for a specific log category

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_log_types_response import TornLogTypesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    log_category_id = 56 # int | Log category id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get available log ids for a specific log category
        api_response = api_instance.torn_log_category_id_logtypes_get(log_category_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_log_category_id_logtypes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_log_category_id_logtypes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_category_id** | **int**| Log category id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornLogTypesResponse**](TornLogTypesResponse.md)

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

# **torn_logcategories_get**
> TornLogCategoriesResponse torn_logcategories_get(timestamp=timestamp, comment=comment, key=key)

Get available log categories

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_log_categories_response import TornLogCategoriesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get available log categories
        api_response = api_instance.torn_logcategories_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_logcategories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_logcategories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornLogCategoriesResponse**](TornLogCategoriesResponse.md)

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

# **torn_logtypes_get**
> TornLogTypesResponse torn_logtypes_get(timestamp=timestamp, comment=comment, key=key)

Get all available log ids

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_log_types_response import TornLogTypesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available log ids
        api_response = api_instance.torn_logtypes_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_logtypes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_logtypes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornLogTypesResponse**](TornLogTypesResponse.md)

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

# **torn_lookup_get**
> TornLookupResponse torn_lookup_get(timestamp=timestamp, comment=comment, key=key)

Get all available torn selections

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_lookup_response import TornLookupResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available torn selections
        api_response = api_instance.torn_lookup_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_lookup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_lookup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornLookupResponse**](TornLookupResponse.md)

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

# **torn_territory_get**
> TornTerritoriesResponse torn_territory_get(offset=offset, limit=limit, timestamp=timestamp, comment=comment, key=key)

Get territory details

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.torn_territories_response import TornTerritoriesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 20 # int |  (optional) (default to 20)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get territory details
        api_response = api_instance.torn_territory_get(offset=offset, limit=limit, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_territory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_territory_get: %s\n" % e)
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

[**TornTerritoriesResponse**](TornTerritoriesResponse.md)

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

# **torn_territory_ids_territory_get**
> TornTerritoriesResponse torn_territory_ids_territory_get(territory_ids, timestamp=timestamp, comment=comment, key=key)

Get territory details

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.faction_territory_enum import FactionTerritoryEnum
from tornclient.models.torn_territories_response import TornTerritoriesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    territory_ids = openapi_client.FactionTerritoryEnum() # FactionTerritoryEnum | Territory id or a list of territory ids (comma separated)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get territory details
        api_response = api_instance.torn_territory_ids_territory_get(territory_ids, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_territory_ids_territory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_territory_ids_territory_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **territory_ids** | [**FactionTerritoryEnum**](.md)| Territory id or a list of territory ids (comma separated) | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornTerritoriesResponse**](TornTerritoriesResponse.md)

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

# **torn_timestamp_get**
> TimestampResponse torn_timestamp_get(timestamp=timestamp, comment=comment, key=key)

Get current server time

Requires public key. <br>

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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.torn_timestamp_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->torn_timestamp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->torn_timestamp_get: %s\n" % e)
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

