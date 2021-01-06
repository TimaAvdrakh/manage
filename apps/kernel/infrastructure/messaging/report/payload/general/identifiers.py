from pyasn1.codec.ber.decoder import decode as ber_decode

from apps.system.lib import (
    basic,
    exceptions,
    asn1,
)
from apps.kernel.infrastructure.messaging import (
    tools,
    network,
)


class ReportedPagerIdentifier(basic.PrintableObject):
    pass


class ReportedPstnIdentifier(basic.PrintableObject):

    @staticmethod
    def create(payload_):
        item, rest = ber_decode(payload_, asn1.NRST_ReportedPstnIdentifier())
        return ReportedPstnIdentifier(
            str(item['directory-number']),
            tools.get_optional_str(item['internal-number'])
        )

    def __init__(self, directory_number_, internal_number_):
        self.directory_number = directory_number_
        self.internal_number = internal_number_

    def __dir__(self):
        return [
            'directory_number', 'internal_number'
        ]


class ReportedGsmIdentifier(basic.PrintableObject):

    @staticmethod
    def create(payload_):
        item, rest = ber_decode(payload_, asn1.NRST_ReportedGsmIdentifier())
        return ReportedGsmIdentifier(
            str(item['directory-number']),
            str(item['imsi']),
            tools.get_optional_str(item['imei']),
            tools.get_optional_str(item['icc'])
        )

    def __init__(self, directory_number_, imsi_, imei_, icc_):
        self.directory_number = directory_number_
        self.imsi = imsi_
        self.imei = imei_
        self.icc = icc_

    def __dir__(self):
        return [
            'directory_number', 'imsi', 'imei', 'icc'
        ]


class ReportedCdmaIdentifier(basic.PrintableObject):

    @staticmethod
    def create(payload_):
        item, rest = ber_decode(payload_, asn1.NRST_ReportedCdmaIdentifier())
        return ReportedCdmaIdentifier(
            str(item['directory-number']),
            str(item['imsi']),
            tools.get_optional_str(item['esn']),
            tools.get_optional_str(item['min']),
            tools.get_optional_str(item['icc'])
        )

    def __init__(self, directory_number_, imsi_, esn_, min_, icc_):
        self.directory_number = directory_number_
        self.imsi = imsi_
        self.esn = esn_
        self.min = min_
        self.icc = icc_

    def __dir__(self):
        return [
            'directory_number', 'imsi', 'esn', 'min', 'icc'
        ]


class ReportedDataNetworkIdentifier(basic.PrintableObject):

    @staticmethod
    def create(payload_):
        item, rest = ber_decode(payload_, asn1.NRST_ReportedDataNetworkIdentifier())
        return ReportedDataNetworkIdentifier(
            tools.get_optional_value(
                item['user-equipment'], network.DataNetworkEquipment.create
            ),
            tools.get_optional_str(item['login']),
            tools.get_optional_ip_address(item['ip-address']),
            tools.get_optional_str(item['e-mail']),
            tools.get_optional_str(item['pin']),
            tools.get_optional_str(item['phone-number']),
            tools.get_optional_str(item['user-domain']),
            tools.get_optional_str(item['reserved']),
            tools.get_optional_value(item['ip-mask'], network.IPMask.create)
        )

    def __init__(self, user_equipment_, login_, ip_address_, e_mail_, pin_,
                 phone_number_, user_domain_, reserved_, ip_mask_):
        self.user_equipment = user_equipment_
        self.login = login_
        self.ip_address = ip_address_
        self.e_mail = e_mail_
        self.pin = pin_
        self.phone_number = phone_number_
        self.user_domain = user_domain_
        self.reserved = reserved_
        self.ip_mask = ip_mask_

    def __dir__(self):
        return [
            'user_equipment', 'login', 'ip_address', 'e_mail', 'pin',
            'phone_number', 'user_domain', 'reserved', 'ip_mask'
        ]


class ReportedVoipIdentifier(basic.PrintableObject):

    @staticmethod
    def create(payload_):
        item, rest = ber_decode(payload_, asn1.NRST_ReportedVoipIdentifier())
        ip_bytes = tools.get_optional_bytes(item['ip-address'])
        return ReportedVoipIdentifier(
            network.IPAddress(ip_bytes) if ip_bytes is not None else None, tools.get_optional_str(
                item['originator-name']
            ),
            tools.get_optional_str(item['calling-number'])
        )

    def __init__(self, ip_address_, originator_name_, calling_number_):
        self.ip_address = ip_address_
        self.originator_name = originator_name_
        self.calling_number = calling_number_

    def __dir__(self):
        return [
            'ip_address', 'originator_name', 'calling_number'
        ]


def create(raw_identifier_: asn1.NRST_ReportedIdentifier):
    raw_id = raw_identifier_['id']
    creator = identifier_creators.get(raw_id, None)
    if creator is None or not callable(creator):
        raise exceptions.GeneralFault(
            'unable to create reported identifier by "{0}" id'.format(id)
        )
    return creator(raw_identifier_['data'])


identifier_creators = {
    asn1.sorm_report_identifier_pager: None,
    asn1.sorm_report_identifier_pstn: ReportedPstnIdentifier.create,
    asn1.sorm_report_identifier_gsm: ReportedGsmIdentifier.create,
    asn1.sorm_report_identifier_cdma: ReportedCdmaIdentifier.create,
    asn1.sorm_report_identifier_data_network: ReportedDataNetworkIdentifier.create,
    asn1.sorm_report_identifier_voip: ReportedVoipIdentifier.create
}
