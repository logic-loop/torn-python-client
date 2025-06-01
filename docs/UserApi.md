# openapi_client.UserApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_attacks_get**](UserApi.md#user_attacks_get) | **GET** /user/attacks | Get your detailed attacks
[**user_attacksfull_get**](UserApi.md#user_attacksfull_get) | **GET** /user/attacksfull | Get your simplified attacks
[**user_bounties_get**](UserApi.md#user_bounties_get) | **GET** /user/bounties | Get bounties placed on you
[**user_calendar_get**](UserApi.md#user_calendar_get) | **GET** /user/calendar | Get your competition&#39;s event start time
[**user_crime_id_crimes_get**](UserApi.md#user_crime_id_crimes_get) | **GET** /user/{crimeId}/crimes | Get your crime statistics
[**user_education_get**](UserApi.md#user_education_get) | **GET** /user/education | Get your education information
[**user_enlistedcars_get**](UserApi.md#user_enlistedcars_get) | **GET** /user/enlistedcars | Get user enlisted cars
[**user_factionbalance_get**](UserApi.md#user_factionbalance_get) | **GET** /user/factionbalance | Get your current faction balance
[**user_forumfeed_get**](UserApi.md#user_forumfeed_get) | **GET** /user/forumfeed | Get updates on your threads and posts
[**user_forumfriends_get**](UserApi.md#user_forumfriends_get) | **GET** /user/forumfriends | Get updates on your friends&#39; activity
[**user_forumposts_get**](UserApi.md#user_forumposts_get) | **GET** /user/forumposts | Get your posts
[**user_forumsubscribedthreads_get**](UserApi.md#user_forumsubscribedthreads_get) | **GET** /user/forumsubscribedthreads | Get updates on threads you subscribed to
[**user_forumthreads_get**](UserApi.md#user_forumthreads_get) | **GET** /user/forumthreads | Get your threads
[**user_get**](UserApi.md#user_get) | **GET** /user | Get any User selection
[**user_hof_get**](UserApi.md#user_hof_get) | **GET** /user/hof | Get your hall of fame rankings
[**user_id_bounties_get**](UserApi.md#user_id_bounties_get) | **GET** /user/{id}/bounties | Get bounties placed on a specific user
[**user_id_forumposts_get**](UserApi.md#user_id_forumposts_get) | **GET** /user/{id}/forumposts | Get posts for a specific player
[**user_id_forumthreads_get**](UserApi.md#user_id_forumthreads_get) | **GET** /user/{id}/forumthreads | Get threads for a specific player
[**user_id_hof_get**](UserApi.md#user_id_hof_get) | **GET** /user/{id}/hof | Get hall of fame rankings for a specific player
[**user_id_personalstats_get**](UserApi.md#user_id_personalstats_get) | **GET** /user/{id}/personalstats | Get a player&#39;s personal stats
[**user_itemmarket_get**](UserApi.md#user_itemmarket_get) | **GET** /user/itemmarket | Get your item market listings for a specific item
[**user_jobranks_get**](UserApi.md#user_jobranks_get) | **GET** /user/jobranks | Get your starter job positions
[**user_list_get**](UserApi.md#user_list_get) | **GET** /user/list | Get your friends, enemies or targets list
[**user_lookup_get**](UserApi.md#user_lookup_get) | **GET** /user/lookup | Get all available user selections
[**user_organizedcrime_get**](UserApi.md#user_organizedcrime_get) | **GET** /user/organizedcrime | Get your current ongoing organized crime
[**user_personalstats_get**](UserApi.md#user_personalstats_get) | **GET** /user/personalstats | Get your personal stats
[**user_races_get**](UserApi.md#user_races_get) | **GET** /user/races | Get user races
[**user_revives_full_get**](UserApi.md#user_revives_full_get) | **GET** /user/revivesFull | Get your simplified revives
[**user_revives_get**](UserApi.md#user_revives_get) | **GET** /user/revives | Get your detailed revives
[**user_timestamp_get**](UserApi.md#user_timestamp_get) | **GET** /user/timestamp | Get current server time


# **user_attacks_get**
> FactionAttacksResponse user_attacks_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)

Get your detailed attacks

Requires limited access key. <br>

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
    api_instance = openapi_client.UserApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your detailed attacks
        api_response = api_instance.user_attacks_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_attacks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_attacks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
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

# **user_attacksfull_get**
> FactionAttacksFullResponse user_attacksfull_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)

Get your simplified attacks

Requires limited access key. <br>Returns up to 1,000 rows. <br>

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
    api_instance = openapi_client.UserApi(api_client)
    limit = 1000 # int |  (optional) (default to 1000)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your simplified attacks
        api_response = api_instance.user_attacksfull_get(limit=limit, sort=sort, to=to, var_from=var_from, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_attacksfull_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_attacksfull_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 1000]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
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

# **user_bounties_get**
> UserBountiesResponse user_bounties_get(timestamp=timestamp, comment=comment, key=key)

Get bounties placed on you

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_bounties_response import UserBountiesResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get bounties placed on you
        api_response = api_instance.user_bounties_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_bounties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_bounties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserBountiesResponse**](UserBountiesResponse.md)

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

# **user_calendar_get**
> UserCalendarResponse user_calendar_get(timestamp=timestamp, comment=comment, key=key)

Get your competition's event start time

Requires minimal access key. <br>Only available to yourself.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_calendar_response import UserCalendarResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your competition's event start time
        api_response = api_instance.user_calendar_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_calendar_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_calendar_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserCalendarResponse**](UserCalendarResponse.md)

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

# **user_crime_id_crimes_get**
> UserCrimesResponse user_crime_id_crimes_get(crime_id, timestamp=timestamp, comment=comment, key=key)

Get your crime statistics

Requires minimal access key. <br>Return the details and statistics about for a specific crime.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_crimes_response import UserCrimesResponse
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
    api_instance = openapi_client.UserApi(api_client)
    crime_id = 56 # int | Crime id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your crime statistics
        api_response = api_instance.user_crime_id_crimes_get(crime_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_crime_id_crimes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_crime_id_crimes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crime_id** | **int**| Crime id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserCrimesResponse**](UserCrimesResponse.md)

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

# **user_education_get**
> UserEducationResponse user_education_get(timestamp=timestamp, comment=comment, key=key)

Get your education information

The response contains a list of complete eduactions and of a current education (if any).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_education_response import UserEducationResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your education information
        api_response = api_instance.user_education_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_education_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_education_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserEducationResponse**](UserEducationResponse.md)

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

# **user_enlistedcars_get**
> UserEnlistedCarsResponse user_enlistedcars_get(timestamp=timestamp, comment=comment, key=key)

Get user enlisted cars

Requires minimal access key. <br>Returns a list of all user enlisted cars.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_enlisted_cars_response import UserEnlistedCarsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get user enlisted cars
        api_response = api_instance.user_enlistedcars_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_enlistedcars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_enlistedcars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserEnlistedCarsResponse**](UserEnlistedCarsResponse.md)

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

# **user_factionbalance_get**
> UserFactionBalanceResponse user_factionbalance_get(timestamp=timestamp, comment=comment, key=key)

Get your current faction balance

Requires limited access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_faction_balance_response import UserFactionBalanceResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your current faction balance
        api_response = api_instance.user_factionbalance_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_factionbalance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_factionbalance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Limited).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserFactionBalanceResponse**](UserFactionBalanceResponse.md)

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

# **user_forumfeed_get**
> UserForumFeedResponse user_forumfeed_get(timestamp=timestamp, comment=comment, key=key)

Get updates on your threads and posts

Requires minimal access key. <br>This selection returns data visible in 'Feed' section on forum page. Feed is sorted by timestamp descending. Only a maximum of 100 rows are returned.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_forum_feed_response import UserForumFeedResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get updates on your threads and posts
        api_response = api_instance.user_forumfeed_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_forumfeed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_forumfeed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserForumFeedResponse**](UserForumFeedResponse.md)

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

# **user_forumfriends_get**
> UserForumFriendsResponse user_forumfriends_get(timestamp=timestamp, comment=comment, key=key)

Get updates on your friends' activity

Requires minimal access key. <br>This selection returns data visible in 'Friends' section on forum page. Feed is sorted by timestamp descending. Only a maximum of 100 rows are returned.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_forum_friends_response import UserForumFriendsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get updates on your friends' activity
        api_response = api_instance.user_forumfriends_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_forumfriends_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_forumfriends_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserForumFriendsResponse**](UserForumFriendsResponse.md)

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

# **user_forumposts_get**
> UserForumPostsResponse user_forumposts_get(striptags=striptags, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)

Get your posts

Requires public access key. <br>Returns 20 posts per page.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_forum_posts_response import UserForumPostsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your posts
        api_response = api_instance.user_forumposts_get(striptags=striptags, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_forumposts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_forumposts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserForumPostsResponse**](UserForumPostsResponse.md)

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

# **user_forumsubscribedthreads_get**
> UserForumSubscribedThreadsResponse user_forumsubscribedthreads_get(timestamp=timestamp, comment=comment, key=key)

Get updates on threads you subscribed to

Requires minimal access key. <br>This selection returns data visible in 'Subscribed Threads' section on forum page. Threads are sorted in the same way as on site.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_forum_subscribed_threads_response import UserForumSubscribedThreadsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get updates on threads you subscribed to
        api_response = api_instance.user_forumsubscribedthreads_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_forumsubscribedthreads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_forumsubscribedthreads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserForumSubscribedThreadsResponse**](UserForumSubscribedThreadsResponse.md)

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

# **user_forumthreads_get**
> UserForumThreadsResponse user_forumthreads_get(limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)

Get your threads

Requires public access key. <br>Returns 100 threads per page. The field 'new_posts' is also available, indicating the amount of unread posts with a Minimum API key (or higher).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_forum_threads_response import UserForumThreadsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your threads
        api_response = api_instance.user_forumthreads_get(limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_forumthreads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_forumthreads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserForumThreadsResponse**](UserForumThreadsResponse.md)

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

# **user_get**
> UserGet200Response user_get(selections=selections, id=id, limit=limit, var_from=var_from, to=to, sort=sort, cat=cat, stat=stat, striptags=striptags, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any User selection

Key access level depends on the required selections. <br>Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_get200_response import UserGet200Response
from tornclient.models.user_selection_name import UserSelectionName
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
    api_instance = openapi_client.UserApi(api_client)
    selections = [openapi_client.UserSelectionName()] # List[UserSelectionName] | Selection names (optional)
    id = 'id_example' # str | selection id (optional)
    limit = 56 # int |  (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    cat = 'cat_example' # str | Selection category (optional)
    stat = 'stat_example' # str | Selection stat (optional)
    striptags = 'striptags_example' # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any User selection
        api_response = api_instance.user_get(selections=selections, id=id, limit=limit, var_from=var_from, to=to, sort=sort, cat=cat, stat=stat, striptags=striptags, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[UserSelectionName]**](UserSelectionName.md)| Selection names | [optional] 
 **id** | **str**| selection id | [optional] 
 **limit** | **int**|  | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **cat** | **str**| Selection category | [optional] 
 **stat** | **str**| Selection stat | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] 
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserGet200Response**](UserGet200Response.md)

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

# **user_hof_get**
> UserHofResponse user_hof_get(timestamp=timestamp, comment=comment, key=key)

Get your hall of fame rankings

Requires public access key. <br>When requesting selection with Limited, Full or Custom key, battle_stats selection will be populated.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_hof_response import UserHofResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your hall of fame rankings
        api_response = api_instance.user_hof_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_hof_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_hof_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserHofResponse**](UserHofResponse.md)

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

# **user_id_bounties_get**
> UserBountiesResponse user_id_bounties_get(id, timestamp=timestamp, comment=comment, key=key)

Get bounties placed on a specific user

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_bounties_response import UserBountiesResponse
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
    api_instance = openapi_client.UserApi(api_client)
    id = 56 # int | User id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get bounties placed on a specific user
        api_response = api_instance.user_id_bounties_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_id_bounties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_id_bounties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserBountiesResponse**](UserBountiesResponse.md)

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

# **user_id_forumposts_get**
> UserForumPostsResponse user_id_forumposts_get(id, striptags=striptags, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)

Get posts for a specific player

Requires public access key. <br>Returns 20 posts per page for a specific player.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_forum_posts_response import UserForumPostsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    id = 56 # int | User id
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get posts for a specific player
        api_response = api_instance.user_id_forumposts_get(id, striptags=striptags, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_id_forumposts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_id_forumposts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User id | 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserForumPostsResponse**](UserForumPostsResponse.md)

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

# **user_id_forumthreads_get**
> UserForumThreadsResponse user_id_forumthreads_get(id, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)

Get threads for a specific player

Requires public access key. <br>Returns 100 threads per page for a specific player. When requesting data for the key owner, a field 'new_posts' is also available, indicating the amount of unread posts. Minimum API key is required for that.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_forum_threads_response import UserForumThreadsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    id = 56 # int | User id
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get threads for a specific player
        api_response = api_instance.user_id_forumthreads_get(id, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_id_forumthreads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_id_forumthreads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User id | 
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserForumThreadsResponse**](UserForumThreadsResponse.md)

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

# **user_id_hof_get**
> UserHofResponse user_id_hof_get(id, timestamp=timestamp, comment=comment, key=key)

Get hall of fame rankings for a specific player

Requires public access key. <br>The battle_stats selection will be populated only when requesting selection with Limited, Full or Custom key and for yourself.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_hof_response import UserHofResponse
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
    api_instance = openapi_client.UserApi(api_client)
    id = 56 # int | User id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get hall of fame rankings for a specific player
        api_response = api_instance.user_id_hof_get(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_id_hof_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_id_hof_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserHofResponse**](UserHofResponse.md)

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

# **user_id_personalstats_get**
> UserPersonalStatsResponse user_id_personalstats_get(id, cat=cat, stat=stat, timestamp=timestamp, timestamp2=timestamp2, comment=comment, key=key)

Get a player's personal stats

Requires public access key. <br>
 *  UserPersonalStatsFull is returned only when this selection is requested for the key owner with Limited, Full or Custom key.
 *  UserPersonalStatsFullPublic is returned when the requested category is 'all'.
 *  UserPersonalStatsPopular is returned when the requested category is 'popular'. Please try to use UserPersonalStatsPopular over UserPersonalStatsFullPublic wherever possible in order to reduce the server load.
 *  Otherwise, UserPersonalStatsCategory is returned for the matched category.
 *  It's possible to request specific stats via 'stat' parameter. In this case the response will vary depending on the stats requested. Private stats are still available only to the key owner (with Limited or higher key).
 *  Additionally, historical stats can also be fetched via 'stat' query parameter, but 'timestamp' parameter must be provided as well. It's only possible to pass up to 10 historical stats at once (the rest is trimmed). When requesting historical stats the response will be of type UserPersonalStatsHistoric.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.personal_stats_category_enum import PersonalStatsCategoryEnum
from tornclient.models.personal_stats_stat_name import PersonalStatsStatName
from tornclient.models.user_personal_stats_response import UserPersonalStatsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    id = 56 # int | User id
    cat = openapi_client.PersonalStatsCategoryEnum() # PersonalStatsCategoryEnum |  (optional)
    stat = [openapi_client.PersonalStatsStatName()] # List[PersonalStatsStatName] | Stat names (10 maximum). Used to fetch historical stat values (optional)
    timestamp = 56 # int | Returns stats until this timestamp (converted to nearest date). (optional)
    timestamp2 = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a player's personal stats
        api_response = api_instance.user_id_personalstats_get(id, cat=cat, stat=stat, timestamp=timestamp, timestamp2=timestamp2, comment=comment, key=key)
        print("The response of UserApi->user_id_personalstats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_id_personalstats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User id | 
 **cat** | [**PersonalStatsCategoryEnum**](.md)|  | [optional] 
 **stat** | [**List[PersonalStatsStatName]**](PersonalStatsStatName.md)| Stat names (10 maximum). Used to fetch historical stat values | [optional] 
 **timestamp** | **int**| Returns stats until this timestamp (converted to nearest date). | [optional] 
 **timestamp2** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserPersonalStatsResponse**](UserPersonalStatsResponse.md)

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

# **user_itemmarket_get**
> UserItemMarketResponse user_itemmarket_get(offset=offset, timestamp=timestamp, comment=comment, key=key)

Get your item market listings for a specific item

Requires limited access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_item_market_response import UserItemMarketResponse
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
    api_instance = openapi_client.UserApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your item market listings for a specific item
        api_response = api_instance.user_itemmarket_get(offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_itemmarket_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_itemmarket_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Limited).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserItemMarketResponse**](UserItemMarketResponse.md)

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

# **user_jobranks_get**
> UserJobRanksResponse user_jobranks_get(timestamp=timestamp, comment=comment, key=key)

Get your starter job positions

Requires minimal access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_job_ranks_response import UserJobRanksResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your starter job positions
        api_response = api_instance.user_jobranks_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_jobranks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_jobranks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserJobRanksResponse**](UserJobRanksResponse.md)

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

# **user_list_get**
> UserListResponse user_list_get(cat, limit=limit, offset=offset, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get your friends, enemies or targets list

Requires limited access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_list_enum import UserListEnum
from tornclient.models.user_list_response import UserListResponse
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
    api_instance = openapi_client.UserApi(api_client)
    cat = openapi_client.UserListEnum() # UserListEnum | Select list type
    limit = 50 # int |  (optional) (default to 50)
    offset = 56 # int |  (optional)
    sort = ASC # str | Sort rows from newest to oldest<br>Default ordering is ascending (optional) (default to ASC)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your friends, enemies or targets list
        api_response = api_instance.user_list_get(cat, limit=limit, offset=offset, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**UserListEnum**](.md)| Select list type | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] 
 **sort** | **str**| Sort rows from newest to oldest&lt;br&gt;Default ordering is ascending | [optional] [default to ASC]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Limited).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserListResponse**](UserListResponse.md)

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

# **user_lookup_get**
> UserLookupResponse user_lookup_get(timestamp=timestamp, comment=comment, key=key)

Get all available user selections

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_lookup_response import UserLookupResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available user selections
        api_response = api_instance.user_lookup_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_lookup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_lookup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserLookupResponse**](UserLookupResponse.md)

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

# **user_organizedcrime_get**
> UserOrganizedCrimeResponse user_organizedcrime_get(timestamp=timestamp, comment=comment, key=key)

Get your current ongoing organized crime

Requires minimal access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_organized_crime_response import UserOrganizedCrimeResponse
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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your current ongoing organized crime
        api_response = api_instance.user_organizedcrime_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_organizedcrime_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_organizedcrime_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserOrganizedCrimeResponse**](UserOrganizedCrimeResponse.md)

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

# **user_personalstats_get**
> UserPersonalStatsResponse user_personalstats_get(cat=cat, stat=stat, timestamp=timestamp, timestamp2=timestamp2, comment=comment, key=key)

Get your personal stats

Requires public access key. <br>
 * UserPersonalStatsFull is returned only when this selection is requested with Limited, Full or Custom key access key.
 * UserPersonalStatsFullPublic is returned when the requested category is 'all'.
 * UserPersonalStatsPopular is returned when the requested category is 'popular'. Please try to use UserPersonalStatsPopular over UserPersonalStatsFullPublic wherever possible in order to reduce the server load.
 * Otherwise, UserPersonalStatsCategory is returned for the matched category.
 * It's possible to request specific stats via 'stat' parameter. In this case the response will vary depending on the stats requested. Private stats are still available only to the key owner (with Limited or higher key).
 * Additionally, historical stats can also be fetched via 'stat' query parameter, but 'timestamp' parameter must be provided as well. It's only possible to pass up to 10 historical stats at once (the rest is trimmed). When requesting historical stats the response will be of type UserPersonalStatsHistoric.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.personal_stats_category_enum import PersonalStatsCategoryEnum
from tornclient.models.personal_stats_stat_name import PersonalStatsStatName
from tornclient.models.user_personal_stats_response import UserPersonalStatsResponse
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
    api_instance = openapi_client.UserApi(api_client)
    cat = openapi_client.PersonalStatsCategoryEnum() # PersonalStatsCategoryEnum | Stats category. Required unless requesting specific stats via 'stat' query parameter (optional)
    stat = [openapi_client.PersonalStatsStatName()] # List[PersonalStatsStatName] | Stat names (10 maximum). Used to fetch historical stat values (optional)
    timestamp = 56 # int | Returns stats until this timestamp (converted to nearest date). (optional)
    timestamp2 = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your personal stats
        api_response = api_instance.user_personalstats_get(cat=cat, stat=stat, timestamp=timestamp, timestamp2=timestamp2, comment=comment, key=key)
        print("The response of UserApi->user_personalstats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_personalstats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**PersonalStatsCategoryEnum**](.md)| Stats category. Required unless requesting specific stats via &#39;stat&#39; query parameter | [optional] 
 **stat** | [**List[PersonalStatsStatName]**](PersonalStatsStatName.md)| Stat names (10 maximum). Used to fetch historical stat values | [optional] 
 **timestamp** | **int**| Returns stats until this timestamp (converted to nearest date). | [optional] 
 **timestamp2** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserPersonalStatsResponse**](UserPersonalStatsResponse.md)

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

# **user_races_get**
> UserRacesResponse user_races_get(limit=limit, sort=sort, var_from=var_from, to=to, cat=cat, timestamp=timestamp, comment=comment, key=key)

Get user races

Requires minimal access key. <br>Returns a list of user races, ordered by race start timestamp.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.user_races_response import UserRacesResponse
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
    api_instance = openapi_client.UserApi(api_client)
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    cat = custom # str | Category of races returned (optional) (default to custom)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Minimal).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get user races
        api_response = api_instance.user_races_get(limit=limit, sort=sort, var_from=var_from, to=to, cat=cat, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_races_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_races_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **cat** | **str**| Category of races returned | [optional] [default to custom]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Minimal).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserRacesResponse**](UserRacesResponse.md)

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

# **user_revives_full_get**
> RevivesFullResponse user_revives_full_get(limit=limit, sort=sort, to=to, var_from=var_from, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get your simplified revives

Requires limited access key. <br>

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
    api_instance = openapi_client.UserApi(api_client)
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your simplified revives
        api_response = api_instance.user_revives_full_get(limit=limit, sort=sort, to=to, var_from=var_from, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_revives_full_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_revives_full_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
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

# **user_revives_get**
> RevivesResponse user_revives_get(limit=limit, sort=sort, to=to, var_from=var_from, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get your detailed revives

Requires limited access key. <br>

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
    api_instance = openapi_client.UserApi(api_client)
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Limited).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get your detailed revives
        api_response = api_instance.user_revives_get(limit=limit, sort=sort, to=to, var_from=var_from, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_revives_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_revives_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
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

# **user_timestamp_get**
> TimestampResponse user_timestamp_get(timestamp=timestamp, comment=comment, key=key)

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
    api_instance = openapi_client.UserApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.user_timestamp_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of UserApi->user_timestamp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_timestamp_get: %s\n" % e)
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

