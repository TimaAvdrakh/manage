from pyasn1.type import univ
from pyasn1.codec.der.encoder import encode as der_encode

from apps.kernel.infrastructure.messaging import base
from apps.system.lib import asn1


class RequestedPagerIdentifier(base.ASN1Copyable):
    pass


class RequestedPstnIdentifier(base.ASN1Copyable):

    def __init__(self, directory_number_, internal_number_=None):
        self.directory_number = directory_number_
        self.internal_number = internal_number_

    def __dir__(self):
        return [
            'directory_number', 'internal_number'
        ]

    def copy_to(self, target_):
        identifier = asn1.NRST_RequestedPstnIdentifier()
        self.set_component(
            identifier, 'directory-number', self.directory_number
        )
        self.set_component(
            identifier, 'internal-number', self.internal_number
        )
        target_.setComponentByName(
            'id', str(asn1.sorm_request_identifier_pstn)
        )
        target_.setComponentByName('data', univ.Any(der_encode(identifier)))


class RequestedGsmIdentifier(base.ASN1ChoiceBase):
    directory_number = 'directory-number'
    imsi = 'imsi'
    imei = 'imei'

    def __init__(self, name_, value_):
        super().__init__(asn1.NRST_RequestedGsmIdentifier(), name_, value_)

    def copy_to(self, target_):
        self.set_component(
            self.asn1_choice, self.component_name, self.component_value
        )
        target_.setComponentByName(
            'id', str(asn1.sorm_request_identifier_gsm)
        )
        target_.setComponentByName(
            'data', univ.Any(der_encode(self.asn1_choice))
        )


class RequestedCdmaIdentifier(base.ASN1ChoiceBase):
    directory_number = 'directory-number'
    imsi = 'imsi'
    esn = 'esn'
    min = 'min'

    def __init__(self, name_, value_):
        super(RequestedCdmaIdentifier, self).__init__(
            asn1.NRST_RequestedCdmaIdentifier(), name_, value_
        )

    def copy_to(self, target_):
        self.set_component(
            self.asn1_choice, self.component_name, self.component_value
        )
        target_.setComponentByName(
            'id', str(asn1.sorm_request_identifier_cdma)
        )
        target_.setComponentByName(
            'data', univ.Any(der_encode(self.asn1_choice))
        )


class RequestedDataNetworkIdentifier(base.ASN1ChoiceBase):

    def __init__(self, name_, value_):
        super(RequestedDataNetworkIdentifier, self).__init__(
            asn1.NRST_RequestedDataNetworkIdentifier(), name_, value_
        )

    def copy_to(self, target_):
        self.set_component(
            self.asn1_choice, self.component_name, self.component_value
        )
        target_.setComponentByName(
            'id', str(asn1.sorm_request_identifier_data_network)
        )
        target_.setComponentByName(
            'data', univ.Any(der_encode(self.asn1_choice))
        )


class RequestedVoipIdentifier(base.ASN1ChoiceBase):

    def __init__(self, name_, value_):
        super(RequestedVoipIdentifier, self).__init__(
            asn1.NRST_RequestedVoipIdentifier(), name_, value_
        )

    def copy_to(self, target_):
        self.set_component(
            self.asn1_choice, self.component_name, self.component_value
        )
        target_.setComponentByName(
            'id', str(asn1.sorm_request_identifier_voip)
        )
        target_.setComponentByName(
            'data', univ.Any(der_encode(self.asn1_choice))
        )


class RequestedIdentifier(base.ASN1Copyable):

    def __init__(self, identifier_):
        self.identifier = identifier_

    def copy_to(self, target_):
        self.identifier.copy_to(target_)

    def __repr__(self):
        return self.identifier.__repr__()
