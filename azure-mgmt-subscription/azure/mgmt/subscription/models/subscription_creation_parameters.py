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


class SubscriptionCreationParameters(Model):
    """Subscription Creation Parameters required to create a new Azure
    subscription.

    :param display_name: The display name of the subscription.
    :type display_name: str
    :param owners: The list of principals that should be granted Owner access
     on the subscription. Principals should be of type User, Service Principal
     or Security Group.
    :type owners: list[~azure.mgmt.subscription.models.AdPrincipal]
    :param offer_type: The offer type of the subscription. For example,
     MS-AZR-0017P (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement
     devTest) are available. Only valid when creating a subscription in a
     enrollment account scope. Possible values include: 'MS-AZR-0017P',
     'MS-AZR-0148P'
    :type offer_type: str or ~azure.mgmt.subscription.models.OfferType
    :param additional_parameters:
    :type additional_parameters: dict[str, object]
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'owners': {'key': 'owners', 'type': '[AdPrincipal]'},
        'offer_type': {'key': 'offerType', 'type': 'str'},
        'additional_parameters': {'key': 'additionalParameters', 'type': '{object}'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionCreationParameters, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.owners = kwargs.get('owners', None)
        self.offer_type = kwargs.get('offer_type', None)
        self.additional_parameters = kwargs.get('additional_parameters', None)