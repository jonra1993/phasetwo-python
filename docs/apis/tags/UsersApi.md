<a name="__pageTop"></a>
# phasetwo.apis.tags.users_api.UsersApi

All URIs are relative to *https://app.phasetwo.io/realms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_magic_link**](#create_magic_link) | **post** /{realm}/magic-link | Create a magic link to log in a user
[**realm_users_user_id_orgs_get**](#realm_users_user_id_orgs_get) | **get** /{realm}/users/{userId}/orgs | List organizations for the given user
[**realm_users_user_id_orgs_org_id_roles_get**](#realm_users_user_id_orgs_org_id_roles_get) | **get** /{realm}/users/{userId}/orgs/{orgId}/roles | List organization roles for the given user and org
[**realm_users_user_id_orgs_org_id_roles_patch**](#realm_users_user_id_orgs_org_id_roles_patch) | **patch** /{realm}/users/{userId}/orgs/{orgId}/roles | Revoke organization roles from a user
[**realm_users_user_id_orgs_org_id_roles_put**](#realm_users_user_id_orgs_org_id_roles_put) | **put** /{realm}/users/{userId}/orgs/{orgId}/roles | Grant a user organization roles

# **create_magic_link**
<a name="create_magic_link"></a>
> create_magic_link(realmmagic_link_representation)

Create a magic link to log in a user

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import users_api
from phasetwo.model.magic_link_representation import MagicLinkRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
    }
    body = MagicLinkRepresentation(
        email="email_example",
        client_id="client_id_example",
        redirect_uri="redirect_uri_example",
        expiration_seconds=1,
        force_create=True,
        send_email=True,
    )
    try:
        # Create a magic link to log in a user
        api_response = api_instance.create_magic_link(
            path_params=path_params,
            body=body,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling UsersApi->create_magic_link: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MagicLinkRepresentation**](../../models/MagicLinkRepresentation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_magic_link.ApiResponseFor200) | Magic Link created
400 | [ApiResponseFor400](#create_magic_link.ApiResponseFor400) | Malformed request
404 | [ApiResponseFor404](#create_magic_link.ApiResponseFor404) | User or Client not found

#### create_magic_link.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_magic_link.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_magic_link.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **realm_users_user_id_orgs_get**
<a name="realm_users_user_id_orgs_get"></a>
> [OrganizationRepresentation] realm_users_user_id_orgs_get(realmuser_id)

List organizations for the given user

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import users_api
from phasetwo.model.organization_representation import OrganizationRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'userId': "userId_example",
    }
    try:
        # List organizations for the given user
        api_response = api_instance.realm_users_user_id_orgs_get(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling UsersApi->realm_users_user_id_orgs_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
userId | UserIdSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#realm_users_user_id_orgs_get.ApiResponseFor200) | success

#### realm_users_user_id_orgs_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrganizationRepresentation**]({{complexTypePrefix}}OrganizationRepresentation.md) | [**OrganizationRepresentation**]({{complexTypePrefix}}OrganizationRepresentation.md) | [**OrganizationRepresentation**]({{complexTypePrefix}}OrganizationRepresentation.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **realm_users_user_id_orgs_org_id_roles_get**
<a name="realm_users_user_id_orgs_org_id_roles_get"></a>
> [OrganizationRoleRepresentation] realm_users_user_id_orgs_org_id_roles_get(realmuser_idorg_id)

List organization roles for the given user and org

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import users_api
from phasetwo.model.organization_role_representation import OrganizationRoleRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'userId': "userId_example",
        'orgId': "orgId_example",
    }
    try:
        # List organization roles for the given user and org
        api_response = api_instance.realm_users_user_id_orgs_org_id_roles_get(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling UsersApi->realm_users_user_id_orgs_org_id_roles_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
userId | UserIdSchema | | 
orgId | OrgIdSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#realm_users_user_id_orgs_org_id_roles_get.ApiResponseFor200) | success

#### realm_users_user_id_orgs_org_id_roles_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) | [**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) | [**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **realm_users_user_id_orgs_org_id_roles_patch**
<a name="realm_users_user_id_orgs_org_id_roles_patch"></a>
> [BulkResponseItem] realm_users_user_id_orgs_org_id_roles_patch(realmuser_idorg_idorganization_role_representation)

Revoke organization roles from a user

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import users_api
from phasetwo.model.organization_role_representation import OrganizationRoleRepresentation
from phasetwo.model.bulk_response_item import BulkResponseItem
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'userId': "userId_example",
        'orgId': "orgId_example",
    }
    body = [
        OrganizationRoleRepresentation(
            id="id_example",
            name="name_example",
            description="description_example",
        )
    ]
    try:
        # Revoke organization roles from a user
        api_response = api_instance.realm_users_user_id_orgs_org_id_roles_patch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling UsersApi->realm_users_user_id_orgs_org_id_roles_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) | [**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) | [**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
userId | UserIdSchema | | 
orgId | OrgIdSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
207 | [ApiResponseFor207](#realm_users_user_id_orgs_org_id_roles_patch.ApiResponseFor207) | Multi Status

#### realm_users_user_id_orgs_org_id_roles_patch.ApiResponseFor207
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor207ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor207ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BulkResponseItem**]({{complexTypePrefix}}BulkResponseItem.md) | [**BulkResponseItem**]({{complexTypePrefix}}BulkResponseItem.md) | [**BulkResponseItem**]({{complexTypePrefix}}BulkResponseItem.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **realm_users_user_id_orgs_org_id_roles_put**
<a name="realm_users_user_id_orgs_org_id_roles_put"></a>
> [BulkResponseItem] realm_users_user_id_orgs_org_id_roles_put(realmuser_idorg_idorganization_role_representation)

Grant a user organization roles

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import users_api
from phasetwo.model.organization_role_representation import OrganizationRoleRepresentation
from phasetwo.model.bulk_response_item import BulkResponseItem
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'userId': "userId_example",
        'orgId': "orgId_example",
    }
    body = [
        OrganizationRoleRepresentation(
            id="id_example",
            name="name_example",
            description="description_example",
        )
    ]
    try:
        # Grant a user organization roles
        api_response = api_instance.realm_users_user_id_orgs_org_id_roles_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling UsersApi->realm_users_user_id_orgs_org_id_roles_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) | [**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) | [**OrganizationRoleRepresentation**]({{complexTypePrefix}}OrganizationRoleRepresentation.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
userId | UserIdSchema | | 
orgId | OrgIdSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
207 | [ApiResponseFor207](#realm_users_user_id_orgs_org_id_roles_put.ApiResponseFor207) | Multi Status

#### realm_users_user_id_orgs_org_id_roles_put.ApiResponseFor207
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor207ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor207ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BulkResponseItem**]({{complexTypePrefix}}BulkResponseItem.md) | [**BulkResponseItem**]({{complexTypePrefix}}BulkResponseItem.md) | [**BulkResponseItem**]({{complexTypePrefix}}BulkResponseItem.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

