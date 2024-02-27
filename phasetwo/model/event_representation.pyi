# coding: utf-8

"""
    Phase Two Admin REST API

    This is a REST API reference for the Phase Two Keycloak custom resources. These are extensions to the standard [Keycloak Admin REST API](https://www.keycloak.org/docs-api/23.0.6/rest-api/index.html).  ### Base URI format Paths specified in the documentation are relative to the the base URI. - Format: `https://<host>:<port>/auth/realms` - Example: `https://app.phasetwo.io/auth/realms`  ### Authentication Authentication is achieved by using the `Authentication: Bearer <token>` header in all requests. This is either the access token received from a normal authentication, or by a request directly to the OpenID Connect token endpoint.  It is recommended that you use a Keycloak Admin Client, such as [this one for Javascript](https://github.com/keycloak/keycloak-nodejs-admin-client), as they take care of authentication, getting an access token, and refreshing it when it expires.  #### Client credentials grant example ``` POST /auth/realms/test-realm/protocol/openid-connect/token Host: app.phasetwo.io Accept: application/json Content-type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=admin-cli&client_secret=fd649804-3a74-4d69-acaa-8f065c6b7da1 ```  #### Password grant example ``` POST /auth/realms/test-realm/protocol/openid-connect/token Host: app.phasetwo.io Accept: application/json Content-type: application/x-www-form-urlencoded  grant_type=password&username=uname@foo.com&password=pwd123AZY&client_id=admin-cli ```  ### SDKs Modern API libraries are available for several common languages. These are available as open source at the links below, or you can choose to generate your own using our [OpenAPI spec file](https://raw.githubusercontent.com/p2-inc/phasetwo-docs/main/openapi.yaml).  | Language | Library | | --- | --- | | Java (and other JVM langs) | https://github.com/p2-inc/phasetwo-java | | JavaScript/TypeScript | https://github.com/p2-inc/phasetwo-js | | Python | https://github.com/p2-inc/phasetwo-python |   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from phasetwo import schemas  # noqa: F401


class EventRepresentation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            uid = schemas.StrSchema
            time = schemas.IntSchema
            realmId = schemas.StrSchema
            organizationId = schemas.StrSchema
            type = schemas.StrSchema
            representation = schemas.StrSchema
            operationType = schemas.StrSchema
            resourcePath = schemas.StrSchema
            resourceType = schemas.StrSchema
            error = schemas.StrSchema
        
            @staticmethod
            def authDetails() -> typing.Type['AuthDetailsRepresentation']:
                return AuthDetailsRepresentation
            
            
            class details(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                ) -> 'details':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "uid": uid,
                "time": time,
                "realmId": realmId,
                "organizationId": organizationId,
                "type": type,
                "representation": representation,
                "operationType": operationType,
                "resourcePath": resourcePath,
                "resourceType": resourceType,
                "error": error,
                "authDetails": authDetails,
                "details": details,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time"]) -> MetaOapg.properties.time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realmId"]) -> MetaOapg.properties.realmId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationId"]) -> MetaOapg.properties.organizationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["representation"]) -> MetaOapg.properties.representation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operationType"]) -> MetaOapg.properties.operationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourcePath"]) -> MetaOapg.properties.resourcePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceType"]) -> MetaOapg.properties.resourceType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authDetails"]) -> 'AuthDetailsRepresentation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uid", "time", "realmId", "organizationId", "type", "representation", "operationType", "resourcePath", "resourceType", "error", "authDetails", "details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> typing.Union[MetaOapg.properties.uid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time"]) -> typing.Union[MetaOapg.properties.time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realmId"]) -> typing.Union[MetaOapg.properties.realmId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationId"]) -> typing.Union[MetaOapg.properties.organizationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["representation"]) -> typing.Union[MetaOapg.properties.representation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operationType"]) -> typing.Union[MetaOapg.properties.operationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourcePath"]) -> typing.Union[MetaOapg.properties.resourcePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceType"]) -> typing.Union[MetaOapg.properties.resourceType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authDetails"]) -> typing.Union['AuthDetailsRepresentation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uid", "time", "realmId", "organizationId", "type", "representation", "operationType", "resourcePath", "resourceType", "error", "authDetails", "details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        uid: typing.Union[MetaOapg.properties.uid, str, schemas.Unset] = schemas.unset,
        time: typing.Union[MetaOapg.properties.time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        realmId: typing.Union[MetaOapg.properties.realmId, str, schemas.Unset] = schemas.unset,
        organizationId: typing.Union[MetaOapg.properties.organizationId, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        representation: typing.Union[MetaOapg.properties.representation, str, schemas.Unset] = schemas.unset,
        operationType: typing.Union[MetaOapg.properties.operationType, str, schemas.Unset] = schemas.unset,
        resourcePath: typing.Union[MetaOapg.properties.resourcePath, str, schemas.Unset] = schemas.unset,
        resourceType: typing.Union[MetaOapg.properties.resourceType, str, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        authDetails: typing.Union['AuthDetailsRepresentation', schemas.Unset] = schemas.unset,
        details: typing.Union[MetaOapg.properties.details, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventRepresentation':
        return super().__new__(
            cls,
            *_args,
            uid=uid,
            time=time,
            realmId=realmId,
            organizationId=organizationId,
            type=type,
            representation=representation,
            operationType=operationType,
            resourcePath=resourcePath,
            resourceType=resourceType,
            error=error,
            authDetails=authDetails,
            details=details,
            _configuration=_configuration,
            **kwargs,
        )

from phasetwo.model.auth_details_representation import AuthDetailsRepresentation
