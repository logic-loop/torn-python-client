# openapi_client.ForumApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forum_categories_get**](ForumApi.md#forum_categories_get) | **GET** /forum/categories | Get publicly available forum categories
[**forum_category_ids_threads_get**](ForumApi.md#forum_category_ids_threads_get) | **GET** /forum/{categoryIds}/threads | Get threads for specific public forum category or categories
[**forum_get**](ForumApi.md#forum_get) | **GET** /forum | Get any Forum selection
[**forum_lookup_get**](ForumApi.md#forum_lookup_get) | **GET** /forum/lookup | Get all available forum selections
[**forum_thread_id_posts_get**](ForumApi.md#forum_thread_id_posts_get) | **GET** /forum/{threadId}/posts | Get specific forum thread posts
[**forum_thread_id_thread_get**](ForumApi.md#forum_thread_id_thread_get) | **GET** /forum/{threadId}/thread | Get specific thread details
[**forum_threads_get**](ForumApi.md#forum_threads_get) | **GET** /forum/threads | Get threads across all forum categories
[**forum_timestamp_get**](ForumApi.md#forum_timestamp_get) | **GET** /forum/timestamp | Get current server time


# **forum_categories_get**
> ForumCategoriesResponse forum_categories_get(timestamp=timestamp, comment=comment, key=key)

Get publicly available forum categories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.forum_categories_response import ForumCategoriesResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get publicly available forum categories
        api_response = api_instance.forum_categories_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->forum_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->forum_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumCategoriesResponse**](ForumCategoriesResponse.md)

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

# **forum_category_ids_threads_get**
> ForumThreadsResponse forum_category_ids_threads_get(category_ids, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)

Get threads for specific public forum category or categories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.forum_threads_response import ForumThreadsResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    category_ids = 'category_ids_example' # str | Category id or a list of category ids (comma separated)
    limit = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get threads for specific public forum category or categories
        api_response = api_instance.forum_category_ids_threads_get(category_ids, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->forum_category_ids_threads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->forum_category_ids_threads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_ids** | **str**| Category id or a list of category ids (comma separated) | 
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumThreadsResponse**](ForumThreadsResponse.md)

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

# **forum_get**
> ForumGet200Response forum_get(selections=selections, id=id, striptags=striptags, limit=limit, sort=sort, var_from=var_from, to=to, offset=offset, cat=cat, timestamp=timestamp, comment=comment, key=key)

Get any Forum selection

Requires public access key. <br>Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.forum_get200_response import ForumGet200Response
from tornclient.models.forum_selection_name import ForumSelectionName
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
    api_instance = openapi_client.ForumApi(api_client)
    selections = [openapi_client.ForumSelectionName()] # List[ForumSelectionName] | Selection names (optional)
    id = 'id_example' # str | selection id (optional)
    striptags = 'striptags_example' # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional)
    limit = 56 # int |  (optional)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    offset = 56 # int |  (optional)
    cat = 'cat_example' # str | Selection category (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Forum selection
        api_response = api_instance.forum_get(selections=selections, id=id, striptags=striptags, limit=limit, sort=sort, var_from=var_from, to=to, offset=offset, cat=cat, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->forum_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->forum_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[ForumSelectionName]**](ForumSelectionName.md)| Selection names | [optional] 
 **id** | **str**| selection id | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] 
 **limit** | **int**|  | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **offset** | **int**|  | [optional] 
 **cat** | **str**| Selection category | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumGet200Response**](ForumGet200Response.md)

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

# **forum_lookup_get**
> ForumLookupResponse forum_lookup_get(timestamp=timestamp, comment=comment, key=key)

Get all available forum selections

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.forum_lookup_response import ForumLookupResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available forum selections
        api_response = api_instance.forum_lookup_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->forum_lookup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->forum_lookup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumLookupResponse**](ForumLookupResponse.md)

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

# **forum_thread_id_posts_get**
> ForumPostsResponse forum_thread_id_posts_get(thread_id, offset=offset, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get specific forum thread posts

Requires public access key. <br>Returns 20 posts per page for a specific thread.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.forum_posts_response import ForumPostsResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    thread_id = 56 # int | Thread id
    offset = 56 # int |  (optional)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get specific forum thread posts
        api_response = api_instance.forum_thread_id_posts_get(thread_id, offset=offset, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->forum_thread_id_posts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->forum_thread_id_posts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| Thread id | 
 **offset** | **int**|  | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumPostsResponse**](ForumPostsResponse.md)

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

# **forum_thread_id_thread_get**
> ForumThreadResponse forum_thread_id_thread_get(thread_id, timestamp=timestamp, comment=comment, key=key)

Get specific thread details

Requires public access key. <br>Contains details of a thread including topic content and poll (if any).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.forum_thread_response import ForumThreadResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    thread_id = 56 # int | Thread id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get specific thread details
        api_response = api_instance.forum_thread_id_thread_get(thread_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->forum_thread_id_thread_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->forum_thread_id_thread_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| Thread id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumThreadResponse**](ForumThreadResponse.md)

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

# **forum_threads_get**
> ForumThreadsResponse forum_threads_get(limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)

Get threads across all forum categories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from tornclient.models.forum_threads_response import ForumThreadsResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get threads across all forum categories
        api_response = api_instance.forum_threads_get(limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->forum_threads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->forum_threads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumThreadsResponse**](ForumThreadsResponse.md)

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

# **forum_timestamp_get**
> TimestampResponse forum_timestamp_get(timestamp=timestamp, comment=comment, key=key)

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
    api_instance = openapi_client.ForumApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.forum_timestamp_get(timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->forum_timestamp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->forum_timestamp_get: %s\n" % e)
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

