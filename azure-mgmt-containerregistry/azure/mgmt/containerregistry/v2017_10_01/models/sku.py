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


class Sku(Model):
    """The SKU of a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The SKU name of the container registry. Required for registry
     creation. Possible values include: 'Classic', 'Basic', 'Standard',
     'Premium'
    :type name: str or
     ~azure.mgmt.containerregistry.v2017_10_01.models.SkuName
    :ivar tier: The SKU tier based on the SKU name. Possible values include:
     'Classic', 'Basic', 'Standard', 'Premium'
    :vartype tier: str or
     ~azure.mgmt.containerregistry.v2017_10_01.models.SkuTier
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, name):
        super(Sku, self).__init__()
        self.name = name
        self.tier = None
