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


class DiskInstanceView(Model):
    """The instance view of the disk.

    :param name: The disk name.
    :type name: str
    :param encryption_settings: Specifies the encryption settings for the OS
     Disk. <br><br> Minimum api-version: 2015-06-15
    :type encryption_settings:
     list[~azure.mgmt.compute.v2017_03_30.models.DiskEncryptionSettings]
    :param statuses: The resource status information.
    :type statuses:
     list[~azure.mgmt.compute.v2017_03_30.models.InstanceViewStatus]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'encryption_settings': {'key': 'encryptionSettings', 'type': '[DiskEncryptionSettings]'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, *, name: str=None, encryption_settings=None, statuses=None, **kwargs) -> None:
        super(DiskInstanceView, self).__init__(**kwargs)
        self.name = name
        self.encryption_settings = encryption_settings
        self.statuses = statuses
