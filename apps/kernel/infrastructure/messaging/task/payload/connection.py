from pyasn1.type import tag
from pyasn1.type import univ
from pyasn1.codec.der.encoder import encode as der_encode


from apps.kernel.infrastructure.messaging import base
from apps.system.lib import (
    asn1,
    exceptions,
)
from .general import operations
from .general import identifiers


class BaseValidateConnectionsTask(base.ASN1Constructable):

    def __init__(self, component_name_, items_):
        self.component_name = component_name_
        self.items = items_

    def __dir__(self):
        return ['items']

    def to_asn1(self):
        task = asn1.SkrConnectionsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
                )
            )
        )
        body = task.getComponentByName(self.component_name)
        for item in self.items:
            choice = asn1.SkrRequestedConnectionParameter()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                component = choice.getComponentByName('find-mask')
                descriptor = tagged_components.get(
                    item.__class__.__name__, None
                )
                if descriptor is None:
                    raise exceptions.GeneralFault(
                        f'unable to construct connection request ' +
                        f'item by the "{item.__class__.__name__}" class'
                    )
                component.setComponentByName('id', descriptor[0])
                if isinstance(item, base.ASN1Constructable):
                    component.setComponentByName(
                        'data', univ.Any(der_encode(item.to_asn1()))
                    )
                else:
                    if isinstance(item, base.ASN1Copyable):
                        predicate = descriptor[1]()
                        item.copy_to(predicate)
                        component.setComponentByName(
                            'data', univ.Any(der_encode(predicate))
                        )
                    else:
                        raise exceptions.GeneralFault(
                            f'unable to encode predicate item ' +
                            f'by the "{item.__class__.__name__}" class'
                        )
            body.append(choice)

        return task


class ValidateConnectionsTask(BaseValidateConnectionsTask):

    def __init__(self, items_):
        super().__init__('validate-connections', items_)


class ValidateDataTask(BaseValidateConnectionsTask):

    def __init__(self, items_):
        super().__init__('validate-data', items_)


class RequestedPagerIdentifier(base.ASN1Constructable):

    def __init__(self, value_):
        self.value = value_

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    def to_asn1(self):
        return asn1.SkrRequestedPagerIdentifier(self.value)


class RequestedPstnConnection(base.ASN1ChoiceBase):
    duration = 'duration'
    call_type_id = 'call-type-id'
    in_subscriber_type = 'in-abonent-type'
    out_subscriber_type = 'out-abonent-type'
    switch_id = 'switch-id'
    inbound_bunch = 'inbound-bunch'
    outbound_bunch = 'outbound-bunch'
    border_switch_id = 'border-switch-id'
    term_cause = 'term-cause'
    supplement_service_id = 'supplement-service-id'
    phone_card_number = 'phone-card-number'
    in_info = 'in-info'
    out_info = 'out-info'
    forwarding_identifier = 'forwarding-identifier'
    message = 'message'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedConnectionPstnData(),
            component_name_,
            component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedConnectionPstnData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedMobileConnection(base.ASN1ChoiceBase):
    duration = 'duration'
    call_type_id = 'call-type-id'
    supplement_service_id = 'supplement-service-id'
    in_subscriber_type = 'in-abonent-type'
    out_subscriber_type = 'out-abonent-type'
    switch_id = 'switch-id'
    inbound_bunch = 'inbound-bunch'
    outbound_bunch = 'outbound-bunch'
    border_switch_id = 'border-switch-id'
    roaming_partner_id = 'roaming-partner-id'
    term_cause = 'term-cause'
    in_info = 'in-info'
    in_end_location = 'in-end-location'
    in_begin_location = 'in-begin-location'
    dialed_digits = 'dialed-digits'
    out_info = 'out-info'
    out_begin_location = 'out-begin-location'
    out_end_location = 'out-end-location'
    forwarding_identifier = 'forwarding-identifier'
    message = 'message'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedConnectionMobileData(),
            component_name_,
            component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedConnectionMobileData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedAAA(base.ASN1ChoiceBase):
    point_id = 'point-id'
    login_type = 'login-type'
    user_equipment = 'user-equipment'
    allocated_ip = 'allocated-ip'
    user_name = 'user-name'
    user_password = 'user-password'
    connect_type = 'connect-type'
    calling_number = 'calling-number'
    called_number = 'called-number'
    nas = 'nas'
    apn = 'apn'
    sgsn_ip = 'sgsn-ip'
    ggsn_ip = 'ggsn-ip'
    service_area_code = 'service-area-code'
    location_start = 'location-start'
    location_end = 'location-end'
    phone_card_number = 'phone-card-number'
    imsi = 'imsi'
    imei = 'imei'
    esn = 'esn'
    pool_number = 'pool-number'
    mcc = 'mcc'
    mnc = 'mnc'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedAAALoginData(),
            component_name_,
            component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedAAALoginData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedResource(base.ASN1ChoiceBase):
    point_id = 'point-id'
    client_info = 'client-info'
    server_info = 'server-info'
    url = 'url'
    term_cause = 'term-cause'
    http_method = 'http-method'
    subscriber_id = 'abonent-id'
    nat_info = 'nat-info'
    location = 'location'

    def __init__(self, component_name, component_value):
        super().__init__(
            asn1.SkrRequestedResourceData(),
            component_name,
            component_value
        )

    def copy_to(self, target_: asn1.SkrRequestedResourceData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedEmail(base.ASN1ChoiceBase):
    point_id = 'point-id'
    client_info = 'client-info'
    server_info = 'server-info'
    sender = 'sender'
    receiver = 'receiver'
    cc = 'cc'
    subject = 'subject'
    attachments = 'attachements'
    mail_server = 'mail-server'
    term_cause = 'term-cause'
    subscriber_id = 'abonent-id'
    message = 'message'
    nat_info = 'nat-info'
    location = 'location'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedEmailData(),
            component_name_,
            component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedEmailData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedIm(base.ASN1ChoiceBase):
    point_id = 'point-id'
    client_info = 'client-info'
    server_info = 'server-info'
    user_login = 'user-login'
    user_password = 'user-password'
    sender_screen_name = 'sender-screen-name'
    sender_uin = 'sender-uin'
    receiver_screen_name = 'receiver-screen-name'
    receiver_uin = 'receiver-uin'
    protocol = 'protocol'
    term_cause = 'term-cause'
    subscriber_id = 'abonent-id'
    message = 'message'
    nat_info = 'nat-info'
    location = 'location'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedImData(),
            component_name_,
            component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedImData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedVoip(base.ASN1ChoiceBase):
    point_id = 'point-id'
    client_info = 'client-info'
    server_info = 'server-info'
    duration = 'duration'
    originator_name = 'originator-name'
    call_type_id = 'call-type-id'
    voip_calling_number = 'voip-calling-number'
    voip_called_number = 'voip-called-number'
    inbound_bunch = 'inbound-bunch'
    outbound_bunch = 'outbound-bunch'
    conference_id = 'conference-id'
    protocol = 'protocol'
    term_cause = 'term-cause'
    subscriber_id = 'abonent-id'
    nat_info = 'nat-info'
    location = 'location'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedVoipData(), component_name_, component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedVoipData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedFileTransfer(base.ASN1ChoiceBase):
    point_id = 'point-id'
    client_info = 'client-info'
    server_info = 'server-info'
    server_name = 'server-name'
    user_name = 'user-name'
    user_password = 'user-password'
    term_cause = 'term-cause'
    subscriber_id = 'abonent-id'
    nat_info = 'nat-info'
    location = 'location'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedFileTransferData(),
            component_name_,
            component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedFileTransferData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedTermAccess(base.ASN1ChoiceBase):
    point_id = 'point-id'
    client_info = 'client-info'
    server_info = 'server-info'
    subscriber_id = 'abonent-id'
    nat_info = 'nat-info'
    location = 'location'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedTermAccessData(),
            component_name_,
            component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedTermAccessData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedRawFlow(base.ASN1ChoiceBase):
    point_id = 'point-id'
    protocol_code = 'protocol-code'
    client_info = 'client-info'
    server_info = 'server-info'
    subscriber_id = 'abonent-id'
    nat_info = 'nat-info'
    location = 'location'

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.SkrRequestedRawFlowsData(),
            component_name_,
            component_value_
        )

    def copy_to(self, target_: asn1.SkrRequestedRawFlowsData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedAddressTranslation(base.ASN1ChoiceBase):
    point_id = 'point-id'
    record_type = 'record-type'
    private_ip = 'private-ip'
    public_ip = 'public-ip'
    destination_ip = 'destination-ip'
    translation_type = 'translation-type'

    def __init__(self, component_name, component_value):
        super().__init__(
            asn1.SkrRequestedAddressTranslationsData(),
            component_name,
            component_value
        )

    def copy_to(self, target_: asn1.SkrRequestedAddressTranslationsData):
        self.set_component(target_, self.component_name, self.component_value)


class RequestedPstnConnectionIdentifier(identifiers.RequestedPstnIdentifier):

    def __init__(self, directory_number_, internal_number_=None):
        super().__init__(
            directory_number_, internal_number_
        )

    def copy_to(self, target_):
        identifier = asn1.SkrRequestedPstnIdentifier()
        self.set_component(
            identifier, 'directory-number', self.directory_number
        )
        self.set_component(identifier, 'internal-number', self.internal_number)
        target_.setComponentByName(
            'id', str(asn1.sorm_request_identifier_pstn)
        )
        target_.setComponentByName('data', identifier)


RequestedCdmaConnectionIdentifier = identifiers.RequestedCdmaIdentifier
RequestedGsmConnectionIdentifier = identifiers.RequestedGsmIdentifier
tagged_components = {
    RequestedPagerIdentifier.__name__: (
        asn1.sorm_request_connection_pager, asn1.SkrRequestedPagerIdentifier
    ),
    RequestedPstnConnection.__name__: (
        asn1.sorm_request_connection_pstn,
        asn1.SkrRequestedConnectionPstnData
    ),
    RequestedMobileConnection.__name__: (
        asn1.sorm_request_connection_mobile,
        asn1.SkrRequestedConnectionMobileData
    ),
    RequestedAAA.__name__: (
        asn1.sorm_request_connection_aaa_login,
        asn1.SkrRequestedAAALoginData
    ),
    RequestedResource.__name__: (
        asn1.sorm_request_connection_resource,
        asn1.SkrRequestedResourceData
    ),
    RequestedEmail.__name__: (
        asn1.sorm_request_connection_email,
        asn1.SkrRequestedEmailData
    ),
    RequestedIm.__name__: (
        asn1.sorm_request_connection_im,
        asn1.SkrRequestedImData
    ),
    RequestedVoip.__name__: (
        asn1.sorm_request_connection_voip,
        asn1.SkrRequestedVoipData
    ),
    RequestedFileTransfer.__name__: (
        asn1.sorm_request_connection_file_transfer,
        asn1.SkrRequestedFileTransferData
    ),
    RequestedTermAccess.__name__: (
        asn1.sorm_request_connection_term_access,
        asn1.SkrRequestedTermAccessData
    ),
    RequestedRawFlow.__name__: (
        asn1.sorm_request_connection_raw_flows,
        asn1.SkrRequestedRawFlowsData
    ),
    RequestedAddressTranslation.__name__: (
        asn1.sorm_request_connection_address_translations,
        asn1.SkrRequestedAddressTranslationsData
    )
}
