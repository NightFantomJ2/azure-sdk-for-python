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


class DscNodeConfigurationCreateOrUpdateParametersProperties(Model):
    """The parameters supplied to the create or update node configuration
    operation.

    :param source: Gets or sets the source.
    :type source: ~azure.mgmt.automation.models.ContentSource
    :param name: Gets or sets the type of the parameter.
    :type name: str
    :param configuration: Gets or sets the configuration of the node.
    :type configuration:
     ~azure.mgmt.automation.models.DscConfigurationAssociationProperty
    :param new_node_configuration_build_version_required: If a new build
     version of NodeConfiguration is required.
    :type new_node_configuration_build_version_required: bool
    """

    _validation = {
        'source': {'required': True},
        'name': {'required': True},
        'configuration': {'required': True},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'ContentSource'},
        'name': {'key': 'name', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'DscConfigurationAssociationProperty'},
        'new_node_configuration_build_version_required': {'key': 'newNodeConfigurationBuildVersionRequired', 'type': 'bool'},
    }

    def __init__(self, source, name, configuration, new_node_configuration_build_version_required=None):
        super(DscNodeConfigurationCreateOrUpdateParametersProperties, self).__init__()
        self.source = source
        self.name = name
        self.configuration = configuration
        self.new_node_configuration_build_version_required = new_node_configuration_build_version_required