# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource import ProxyResource


class DatabaseBlobAuditingPolicy(ProxyResource):
    """A database blob auditing policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar kind: Resource kind.
    :vartype kind: str
    :param state: Required. Specifies the state of the policy. If state is
     Enabled, storageEndpoint and storageAccountAccessKey are required.
     Possible values include: 'Enabled', 'Disabled'
    :type state: str or ~azure.mgmt.sql.models.BlobAuditingPolicyState
    :param storage_endpoint: Specifies the blob storage endpoint (e.g.
     https://MyAccount.blob.core.windows.net). If state is Enabled,
     storageEndpoint is required.
    :type storage_endpoint: str
    :param storage_account_access_key: Specifies the identifier key of the
     auditing storage account. If state is Enabled, storageAccountAccessKey is
     required.
    :type storage_account_access_key: str
    :param retention_days: Specifies the number of days to keep in the audit
     logs.
    :type retention_days: int
    :param audit_actions_and_groups: Specifies the Actions and Actions-Groups
     to audit.
    :type audit_actions_and_groups: list[str]
    :param storage_account_subscription_id: Specifies the blob storage
     subscription Id.
    :type storage_account_subscription_id: str
    :param is_storage_secondary_key_in_use: Specifies whether
     storageAccountAccessKey value is the storage’s secondary key.
    :type is_storage_secondary_key_in_use: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'readonly': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'BlobAuditingPolicyState'},
        'storage_endpoint': {'key': 'properties.storageEndpoint', 'type': 'str'},
        'storage_account_access_key': {'key': 'properties.storageAccountAccessKey', 'type': 'str'},
        'retention_days': {'key': 'properties.retentionDays', 'type': 'int'},
        'audit_actions_and_groups': {'key': 'properties.auditActionsAndGroups', 'type': '[str]'},
        'storage_account_subscription_id': {'key': 'properties.storageAccountSubscriptionId', 'type': 'str'},
        'is_storage_secondary_key_in_use': {'key': 'properties.isStorageSecondaryKeyInUse', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(DatabaseBlobAuditingPolicy, self).__init__(**kwargs)
        self.kind = None
        self.state = kwargs.get('state', None)
        self.storage_endpoint = kwargs.get('storage_endpoint', None)
        self.storage_account_access_key = kwargs.get('storage_account_access_key', None)
        self.retention_days = kwargs.get('retention_days', None)
        self.audit_actions_and_groups = kwargs.get('audit_actions_and_groups', None)
        self.storage_account_subscription_id = kwargs.get('storage_account_subscription_id', None)
        self.is_storage_secondary_key_in_use = kwargs.get('is_storage_secondary_key_in_use', None)
