# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class Probe(SubResource):
    """
    Load balancer Probe

    :param str id: Resource Id
    :param str name: Gets name of the resource that is unique within a
     resource group. This name can be used to access the resource
    :param str etag: A unique read-only string that changes whenever the
     resource is updated
    :param list load_balancing_rules: Gets Load balancer rules that use this
     probe
    :param str protocol: Gets or sets the protocol of the end point. Possible
     values are http pr Tcp. If Tcp is specified, a received ACK is required
     for the probe to be successful. If http is specified,a 200 OK response
     from the specifies URI is required for the probe to be successful.
     Possible values include: 'Http', 'Tcp'
    :param int port: Gets or sets Port for communicating the probe. Possible
     values range from 1 to 65535, inclusive.
    :param int interval_in_seconds: Gets or sets the interval, in seconds,
     for how frequently to probe the endpoint for health status. Typically,
     the interval is slightly less than half the allocated timeout period (in
     seconds) which allows two full probes before taking the instance out of
     rotation. The default value is 15, the minimum value is 5
    :param int number_of_probes: Gets or sets the number of probes where if
     no response, will result in stopping further traffic from being
     delivered to the endpoint. This values allows endponints to be taken out
     of rotation faster or slower than the typical times used in Azure.
    :param str request_path: Gets or sets the URI used for requesting health
     status from the VM. Path is required if a protocol is set to http.
     Otherwise, it is not allowed. There is no default value
    :param str provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    """

    _required = ['protocol', 'port']

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'load_balancing_rules': {'key': 'properties.loadBalancingRules', 'type': '[SubResource]', 'flatten': True},
        'protocol': {'key': 'properties.protocol', 'type': 'ProbeProtocol', 'flatten': True},
        'port': {'key': 'properties.port', 'type': 'int', 'flatten': True},
        'interval_in_seconds': {'key': 'properties.intervalInSeconds', 'type': 'int', 'flatten': True},
        'number_of_probes': {'key': 'properties.numberOfProbes', 'type': 'int', 'flatten': True},
        'request_path': {'key': 'properties.requestPath', 'type': 'str', 'flatten': True},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str', 'flatten': True},
    }

    def __init__(self, protocol, port, id=None, name=None, etag=None, load_balancing_rules=None, interval_in_seconds=None, number_of_probes=None, request_path=None, provisioning_state=None):
        super(Probe, self).__init__(id=id)
        self.name = name
        self.etag = etag
        self.load_balancing_rules = load_balancing_rules
        self.protocol = protocol
        self.port = port
        self.interval_in_seconds = interval_in_seconds
        self.number_of_probes = number_of_probes
        self.request_path = request_path
        self.provisioning_state = provisioning_state