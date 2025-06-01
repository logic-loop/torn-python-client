# openapi_client.KeyApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**key_get**](KeyApi.md#key_get) | **GET** /key | Get any Key selection
[**key_info_get**](KeyApi.md#key_info_get) | **GET** /key/info | Get current key info
[**key_log_get**](KeyApi.md#key_log_get) | **GET** /key/log | Get current key log history


# **key_get**
> KeyGet200Response key_get(selections=selections, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Key selection

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.key_get200_response import KeyGet200Response
from tornclient.models.key_selection_name import KeySelectionName
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
    api_instance = openapi_client.KeyApi(api_client)
    selections = [openapi_client.KeySelectionName()] # List[KeySelectionName] | Selection names (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Key selection
        api_response = api_instance.key_get(selections=selections, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of KeyApi->key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[KeySelectionName]**](KeySelectionName.md)| Selection names | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**KeyGet200Response**](KeyGet200Response.md)

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

# **key_info_get**
> KeyInfoResponse key_info_get(timestamp=timestamp, comment=comment, key=key)

Get current key info

Available for any key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.key_info_response import KeyInfoResponse
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
    api_instance = openapi_client.KeyApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current key info
        api_response = api_instance.key_info_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of KeyApi->key_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->key_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**KeyInfoResponse**](KeyInfoResponse.md)

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

# **key_log_get**
> KeyLogResponse key_log_get(limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get current key log history

Available for any key. <br>
 * This selection contains up to last 250 request logs.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.key_log_response import KeyLogResponse
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
    api_instance = openapi_client.KeyApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current key log history
        api_response = api_instance.key_log_get(limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of KeyApi->key_log_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->key_log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**KeyLogResponse**](KeyLogResponse.md)

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

