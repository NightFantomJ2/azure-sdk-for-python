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

from .resource import Resource


class VirtualMachineScaleSetVM(Resource):
    """Describes a virtual machine scale set virtual machine.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar instance_id: The virtual machine instance ID.
    :vartype instance_id: str
    :ivar sku: The virtual machine SKU.
    :vartype sku: ~azure.mgmt.compute.v2015_06_15.models.Sku
    :ivar latest_model_applied: Specifies whether the latest model has been
     applied to the virtual machine.
    :vartype latest_model_applied: bool
    :ivar instance_view: The virtual machine instance view.
    :vartype instance_view:
     ~azure.mgmt.compute.v2015_06_15.models.VirtualMachineInstanceView
    :param hardware_profile: Specifies the hardware settings for the virtual
     machine.
    :type hardware_profile:
     ~azure.mgmt.compute.v2015_06_15.models.HardwareProfile
    :param storage_profile: Specifies the storage settings for the virtual
     machine disks.
    :type storage_profile:
     ~azure.mgmt.compute.v2015_06_15.models.StorageProfile
    :param os_profile: Specifies the operating system settings for the virtual
     machine.
    :type os_profile: ~azure.mgmt.compute.v2015_06_15.models.OSProfile
    :param network_profile: Specifies the network interfaces of the virtual
     machine.
    :type network_profile:
     ~azure.mgmt.compute.v2015_06_15.models.NetworkProfile
    :param diagnostics_profile: Specifies the boot diagnostic settings state.
     <br><br>Minimum api-version: 2015-06-15.
    :type diagnostics_profile:
     ~azure.mgmt.compute.v2015_06_15.models.DiagnosticsProfile
    :param availability_set: Specifies information about the availability set
     that the virtual machine should be assigned to. Virtual machines specified
     in the same availability set are allocated to different nodes to maximize
     availability. For more information about availability sets, see [Manage
     the availability of virtual
     machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json).
     <br><br> For more information on Azure planned maintainance, see [Planned
     maintenance for virtual machines in
     Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
     <br><br> Currently, a VM can only be added to availability set at creation
     time. An existing VM cannot be added to an availability set.
    :type availability_set: ~azure.mgmt.compute.v2015_06_15.models.SubResource
    :param provisioning_state: The provisioning state, which only appears in
     the response.
    :type provisioning_state: str
    :param license_type: Specifies that the image or disk that is being used
     was licensed on-premises. This element is only used for images that
     contain the Windows Server operating system. <br><br> Possible values are:
     <br><br> Windows_Client <br><br> Windows_Server <br><br> If this element
     is included in a request for an update, the value must match the initial
     value. This value cannot be updated. <br><br> For more information, see
     [Azure Hybrid Use Benefit for Windows
     Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
     <br><br> Minimum api-version: 2015-06-15
    :type license_type: str
    :param plan: Specifies information about the marketplace image used to
     create the virtual machine. This element is only used for marketplace
     images. Before you can use a marketplace image from an API, you must
     enable the image for programmatic use.  In the Azure portal, find the
     marketplace image that you want to use and then click **Want to deploy
     programmatically, Get Started ->**. Enter any required information and
     then click **Save**.
    :type plan: ~azure.mgmt.compute.v2015_06_15.models.Plan
    :ivar resources: The virtual machine child extension resources.
    :vartype resources:
     list[~azure.mgmt.compute.v2015_06_15.models.VirtualMachineExtension]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'instance_id': {'readonly': True},
        'sku': {'readonly': True},
        'latest_model_applied': {'readonly': True},
        'instance_view': {'readonly': True},
        'resources': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'instance_id': {'key': 'instanceId', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'latest_model_applied': {'key': 'properties.latestModelApplied', 'type': 'bool'},
        'instance_view': {'key': 'properties.instanceView', 'type': 'VirtualMachineInstanceView'},
        'hardware_profile': {'key': 'properties.hardwareProfile', 'type': 'HardwareProfile'},
        'storage_profile': {'key': 'properties.storageProfile', 'type': 'StorageProfile'},
        'os_profile': {'key': 'properties.osProfile', 'type': 'OSProfile'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'diagnostics_profile': {'key': 'properties.diagnosticsProfile', 'type': 'DiagnosticsProfile'},
        'availability_set': {'key': 'properties.availabilitySet', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'license_type': {'key': 'properties.licenseType', 'type': 'str'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'resources': {'key': 'resources', 'type': '[VirtualMachineExtension]'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineScaleSetVM, self).__init__(**kwargs)
        self.instance_id = None
        self.sku = None
        self.latest_model_applied = None
        self.instance_view = None
        self.hardware_profile = kwargs.get('hardware_profile', None)
        self.storage_profile = kwargs.get('storage_profile', None)
        self.os_profile = kwargs.get('os_profile', None)
        self.network_profile = kwargs.get('network_profile', None)
        self.diagnostics_profile = kwargs.get('diagnostics_profile', None)
        self.availability_set = kwargs.get('availability_set', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.license_type = kwargs.get('license_type', None)
        self.plan = kwargs.get('plan', None)
        self.resources = None
