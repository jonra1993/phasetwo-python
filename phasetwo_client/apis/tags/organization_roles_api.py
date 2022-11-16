# coding: utf-8

"""
    Phase Two Admin REST API

    This is a REST API reference for the Phase Two Keycloak custom resources. These are extensions to the standard [Keycloak Admin REST API](https://www.keycloak.org/docs-api/17.0/rest-api/index.html).  ### Base URI format Paths specified in the documentation are relative to the the base URI. - Format: `https://<host>:<port>/auth/realms` - Example: `https://app.phasetwo.io/auth/realms`  ### Authentication Authentication is achieved by using the `Authentication: Bearer <token>` header in all requests. This is either the access token received from a normal authentication, or by a request directly to the OpenID Connect token endpoint.  It is recommended that you use a Keycloak Admin Client, such as [this one for Javascript](https://github.com/keycloak/keycloak-nodejs-admin-client), as they take care of authetication, getting an access token, and refreshing it when it expires.  #### Client credentials grant example ``` POST /auth/realms/test-realm/protocol/openid-connect/token Host: app.phasetwo.io Accept: application/json Content-type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=admin-cli&client_secret=fd649804-3a74-4d69-acaa-8f065c6b7da1 ```  #### Password grant example ``` POST /auth/realms/test-realm/protocol/openid-connect/token Host: app.phasetwo.io Accept: application/json Content-type: application/x-www-form-urlencoded  grant_type=password&username=uname@foo.com&password=pwd123AZY&client_id=admin-cli ```   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

from phasetwo_client.paths.realm_orgs_org_id_roles_name_users_user_id.get import CheckUserOrganizationRole
from phasetwo_client.paths.realm_orgs_org_id_roles.post import CreateOrganizationRole
from phasetwo_client.paths.realm_orgs_org_id_roles_name.delete import DeleteOrganizationRole
from phasetwo_client.paths.realm_orgs_org_id_roles_name.get import GetOrganizationRole
from phasetwo_client.paths.realm_orgs_org_id_roles.get import GetOrganizationRoles
from phasetwo_client.paths.realm_orgs_org_id_roles_name_users.get import GetUserOrganizationRoles
from phasetwo_client.paths.realm_orgs_org_id_roles_name_users_user_id.put import GrantUserOrganizationRole
from phasetwo_client.paths.realm_orgs_org_id_roles_name_users_user_id.delete import RevokeUserOrganizationRole
from phasetwo_client.paths.realm_orgs_org_id_roles_name.put import UpdateOrganizationRole


class OrganizationRolesApi(
    CheckUserOrganizationRole,
    CreateOrganizationRole,
    DeleteOrganizationRole,
    GetOrganizationRole,
    GetOrganizationRoles,
    GetUserOrganizationRoles,
    GrantUserOrganizationRole,
    RevokeUserOrganizationRole,
    UpdateOrganizationRole,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
