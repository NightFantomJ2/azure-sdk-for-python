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

from msrest.serialization import Model


class RegenerateAccessKeyParameters(Model):
    """Parameters supplied to the Regenerate Authorization Rule operation,
    specifies which key neeeds to be reset.

    :param key_type: The access key to regenerate. Possible values include:
     'PrimaryKey', 'SecondaryKey'
    :type key_type: str or :class:`KeyType
     <azure.mgmt.eventhub.models.KeyType>`
    :param key: Optional, if the key value provided, is set for KeyType or
     autogenerated Key value set for keyType
    :type key: str
    """

    _validation = {
        'key_type': {'required': True},
    }

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'KeyType'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, key_type, key=None):
        self.key_type = key_type
        self.key = key