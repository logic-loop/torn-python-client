# openapi_client.RacingApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**racing_cars_get**](RacingApi.md#racing_cars_get) | **GET** /racing/cars | Get cars and their racing stats
[**racing_carupgrades_get**](RacingApi.md#racing_carupgrades_get) | **GET** /racing/carupgrades | Get all possible car upgrades
[**racing_get**](RacingApi.md#racing_get) | **GET** /racing | Get any Racing selection
[**racing_lookup_get**](RacingApi.md#racing_lookup_get) | **GET** /racing/lookup | Get all available racing selections
[**racing_race_id_race_get**](RacingApi.md#racing_race_id_race_get) | **GET** /racing/{raceId}/race | Get specific race details
[**racing_races_get**](RacingApi.md#racing_races_get) | **GET** /racing/races | Get races
[**racing_timestamp_get**](RacingApi.md#racing_timestamp_get) | **GET** /racing/timestamp | Get current server time
[**racing_track_id_records_get**](RacingApi.md#racing_track_id_records_get) | **GET** /racing/{trackId}/records | Get track records
[**racing_tracks_get**](RacingApi.md#racing_tracks_get) | **GET** /racing/tracks | Get race tracks and descriptions


# **racing_cars_get**
> RacingCarsResponse racing_cars_get(timestamp=timestamp, comment=comment, key=key)

Get cars and their racing stats

Requires public access key. <br>Returns the stat details about racing cars.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.racing_cars_response import RacingCarsResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get cars and their racing stats
        api_response = api_instance.racing_cars_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_cars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_cars_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingCarsResponse**](RacingCarsResponse.md)

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

# **racing_carupgrades_get**
> RacingCarUpgradesResponse racing_carupgrades_get(timestamp=timestamp, comment=comment, key=key)

Get all possible car upgrades

Requires public access key. <br>Returns the details about all possible car upgrades.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.racing_car_upgrades_response import RacingCarUpgradesResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all possible car upgrades
        api_response = api_instance.racing_carupgrades_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_carupgrades_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_carupgrades_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingCarUpgradesResponse**](RacingCarUpgradesResponse.md)

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

# **racing_get**
> RacingGet200Response racing_get(selections=selections, id=id, limit=limit, sort=sort, to=to, var_from=var_from, cat=cat, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Racing selection

Requires public access key. <br>Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.racing_get200_response import RacingGet200Response
from tornclient.models.racing_selection_name import RacingSelectionName
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
    api_instance = openapi_client.RacingApi(api_client)
    selections = [openapi_client.RacingSelectionName()] # List[RacingSelectionName] | Selection names (optional)
    id = 'id_example' # str | selection id (optional)
    limit = 56 # int |  (optional)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    cat = 'cat_example' # str | Selection category (optional)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Racing selection
        api_response = api_instance.racing_get(selections=selections, id=id, limit=limit, sort=sort, to=to, var_from=var_from, cat=cat, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[RacingSelectionName]**](RacingSelectionName.md)| Selection names | [optional] 
 **id** | **str**| selection id | [optional] 
 **limit** | **int**|  | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **cat** | **str**| Selection category | [optional] 
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingGet200Response**](RacingGet200Response.md)

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

# **racing_lookup_get**
> RacingLookupResponse racing_lookup_get(timestamp=timestamp, comment=comment, key=key)

Get all available racing selections

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.racing_lookup_response import RacingLookupResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available racing selections
        api_response = api_instance.racing_lookup_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_lookup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_lookup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingLookupResponse**](RacingLookupResponse.md)

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

# **racing_race_id_race_get**
> RacingRaceDetailsResponse racing_race_id_race_get(race_id, timestamp=timestamp, comment=comment, key=key)

Get specific race details

Requires public access key. <br>Returns the details of a race.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.racing_race_details_response import RacingRaceDetailsResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    race_id = 56 # int | Race id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get specific race details
        api_response = api_instance.racing_race_id_race_get(race_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_race_id_race_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_race_id_race_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| Race id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingRaceDetailsResponse**](RacingRaceDetailsResponse.md)

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

# **racing_races_get**
> RacingRacesResponse racing_races_get(limit=limit, sort=sort, to=to, var_from=var_from, cat=cat, timestamp=timestamp, comment=comment, key=key)

Get races

Requires public access key. <br>Returns a list of races, ordered by race start timestamp.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.racing_races_response import RacingRacesResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    cat = custom # str | Category of races returned (optional) (default to custom)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get races
        api_response = api_instance.racing_races_get(limit=limit, sort=sort, to=to, var_from=var_from, cat=cat, timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_races_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_races_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **cat** | **str**| Category of races returned | [optional] [default to custom]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingRacesResponse**](RacingRacesResponse.md)

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

# **racing_timestamp_get**
> TimestampResponse racing_timestamp_get(timestamp=timestamp, comment=comment, key=key)

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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.racing_timestamp_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_timestamp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_timestamp_get: %s\n" % e)
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

# **racing_track_id_records_get**
> RacingTrackRecordsResponse racing_track_id_records_get(track_id, cat, timestamp=timestamp, comment=comment, key=key)

Get track records

Requires public access key. <br>Returns a list of 10 best lap records for the chosen track and car class. Results are cached globally 1 hour.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.race_class_enum import RaceClassEnum
from tornclient.models.racing_track_records_response import RacingTrackRecordsResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    track_id = 56 # int | Track id
    cat = openapi_client.RaceClassEnum() # RaceClassEnum | Car class
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get track records
        api_response = api_instance.racing_track_id_records_get(track_id, cat, timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_track_id_records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_track_id_records_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_id** | **int**| Track id | 
 **cat** | [**RaceClassEnum**](.md)| Car class | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingTrackRecordsResponse**](RacingTrackRecordsResponse.md)

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

# **racing_tracks_get**
> RacingTracksResponse racing_tracks_get(timestamp=timestamp, comment=comment, key=key)

Get race tracks and descriptions

Requires public access key. <br>Returns the details about racing tracks.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.racing_tracks_response import RacingTracksResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get race tracks and descriptions
        api_response = api_instance.racing_tracks_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->racing_tracks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->racing_tracks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingTracksResponse**](RacingTracksResponse.md)

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

