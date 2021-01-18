from pyasn1.codec.ber.decoder import decode as ber_decode

from apps.kernel.infrastructure.messaging.report import report
from apps.kernel.infrastructure.messaging import (
    tools,
    locations,
)
from apps.kernel.infrastructure.messaging.report.payload.general import (
    identifiers,
    addresses,
)
from apps.system.lib import (
    exceptions,
    basic,
    asn1,
)


class SubscriberReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrReportAbonentData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, SubscriberReportRecord.create
        )
        return SubscriberReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_,
                 data_block_number_, records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class SubscriberReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrAbonentsRecord):
        return SubscriberReportRecord(
            int(payload_['telco-id']),
            identifiers.create(payload_['idents']),
            str(payload_['contract-date']),
            str(payload_['contract']),
            str(payload_['actual-from']),
            str(payload_['actual-to']),
            int(payload_['status']),
            create_subscriber_info(payload_['abonent']),
            tools.get_optional_str(payload_['attach']),
            tools.get_optional_str(payload_['detach']),
            tools.get_optional_value(
                payload_['last-location'], locations.Location.create
            ),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['services']), Service.create
            ),
            tools.get_optional_value(payload_['line-data'], LineData.create),
            tools.get_optional_int(payload_['standard']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['addresses']),
                addresses.ReportedAddress.create
            )
        )

    def __init__(self, telco_code_, identifier_, contract_date_, contract_,
                 actual_from_, actual_to_, status_, subs_info_, attach_,
                 detach_, last_location_, services_, line_data_, standard_,
                 addresses_):
        self.telco_code = telco_code_
        self.identifier = identifier_
        self.contract_date = contract_date_
        self.contract = contract_
        self.actual_from = actual_from_
        self.actual_to = actual_to_
        self.status = status_
        self.subs_info = subs_info_
        self.attach = attach_
        self.detach = detach_
        self.last_location = last_location_
        self.services = services_
        self.line_data = line_data_
        self.standard = standard_
        self.addresses = addresses_

    def __dir__(self):
        return [
            'telco_code', 'identifier', 'contract_date', 'contract',
            'actual_from', 'actual_to', 'status', 'subs_info', 'attach',
            'detach', 'last_location', 'services', 'line_data', 'standard',
            'addresses'
        ]


class ServiceReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrReportServiceData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, Service.create
        )
        return ServiceReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_,
                 data_block_number_, records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


def create_subscriber_info(payload_: asn1.SkrAbonentInfo):
    oid = payload_['id']
    if oid == asn1.sorm_report_abonent_person:
        item, rest = ber_decode(payload_['data'], asn1.SkrAbonentPerson())
        return PersonInfo.create(item)
    if oid == asn1.sorm_report_abonent_organization:
        item, rest = ber_decode(
            payload_['data'], asn1.SkrAbonentOrganization()
        )
        return OrganizationInfo.create(item)
    raise exceptions.GeneralFault(
        f'unable to create subscriber info by the "{str(oid)}" OID'
    )


class PersonInfo(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrAbonentPerson):
        name_item = payload_['name-info']

        if name_item.getName() == 'unstruct-name':
            component = str(name_item.getComponent())
        else:
            component = PersonStructuredName.create(name_item.getComponent())

        return PersonInfo(
            component,
            tools.get_optional_str(payload_['birth-date']),
            PersonDocumentInfo.create(payload_['passport-info']),
            tools.get_optional_str(payload_['bank']),
            tools.get_optional_str(payload_['bank-account'])
        )

    def __init__(self, name_info_, birth_date_, document_info_, bank_,
                 bank_account_):
        self.name_info = name_info_
        self.birth_date = birth_date_
        self.document_info = document_info_
        self.bank = bank_
        self.bank_account = bank_account_

    def __dir__(self):
        return [
            'name_info', 'birth_date', 'document_info', 'bank', 'bank_account'
        ]


class PersonStructuredName(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrPersonStructNameInfoReport):
        return PersonStructuredName(
            str(payload_['given-name']),
            str(payload_['initial']),
            str(payload_['family-name'])
        )

    def __init__(self, given_name_, patronymic_name_, surname_):
        self.given_name = given_name_
        self.patronymic_name = patronymic_name_
        self.surname = surname_

    def __dir__(self):
        return [
            'given_name', 'patronymic_name', 'surname'
        ]


class PersonDocumentInfo(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrPassportInfoReport):
        item = payload_['ident-card-info']

        if item.getName() == 'unstruct-info':
            component = str(item.getComponent())
        else:
            component = StructuredDocumentInfo.create(item.getComponent())

        return PersonDocumentInfo(
            int(payload_['doc-type-id']),
            component
        )

    def __init__(self, document_type_id_, info_):
        self.document_type_id = document_type_id_
        self.info = info_

    def __dir__(self):
        return [
            'document_type_id', 'info'
        ]


class StructuredDocumentInfo(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrIdentCardStructInfoReport):
        return StructuredDocumentInfo(
            str(payload_['ident-card-serial']),
            str(payload_['ident-card-number']),
            str(payload_['ident-card-description'])
        )

    def __init__(self, serial_, number_, description_):
        self.serial = serial_
        self.number = number_
        self.description = description_

    def __dir__(self):
        return [
            'serial', 'number', 'description'
        ]


class OrganizationInfo(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrAbonentOrganization):
        return OrganizationInfo(
            str(payload_['full-name']),
            str(payload_['inn']),
            tools.get_optional_str(payload_['contact']),
            tools.get_optional_str(payload_['phone-fax']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['internal-users']),
                InternalUser.create
            ),
            tools.get_optional_str(payload_['bank']),
            tools.get_optional_str(payload_['bank-account'])
        )

    def __init__(self, full_name_, tax_reference_number_, contract_,
                 phone_fax_, internal_users_, bank_, bank_account_):
        self.full_name = full_name_
        self.tax_reference_number = tax_reference_number_
        self.contract = contract_
        self.phone_fax = phone_fax_
        self.internal_users = internal_users_
        self.bank = bank_
        self.bank_account = bank_account_

    def __dir__(self):
        return [
            'full_name', 'tax_reference_number', 'contract', 'phone_fax',
            'internal_users', 'bank', 'bank_account'
        ]


class InternalUser(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrInternalUsersRecord):
        return InternalUser(
            str(payload_['user-name']),
            str(payload_['internal-number'])
        )

    def __init__(self, user_name_, internal_number_):
        self.user_name = user_name_
        self.internal_number = internal_number_

    def __dir__(self):
        return [
            'user_name', 'internal_number'
        ]


class Service(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrAbonentService):
        return Service(
            int(payload_['telco-id']),
            int(payload_['service-id']),
            tools.get_optional_value(payload_['idents'], identifiers.create),
            str(payload_['contract']),
            str(payload_['begin-time']),
            str(payload_['end-time']),
            tools.get_optional_str(payload_['parameter'])
        )

    def __init__(self, telco_code_, service_id_, identifier_, contract_,
                 begin_time_, end_time_, parameter_):
        self.telco_code = telco_code_
        self.service_id = service_id_
        self.identifier = identifier_
        self.contract = contract_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.parameter = parameter_

    def __dir__(self):
        return [
            'telco_code', 'service_id', 'identifier', 'contract',
            'begin_time', 'end_time', 'parameter'
        ]


class LineData(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrLineData):
        return LineData(
            tools.get_optional_str(payload_['object']),
            tools.get_optional_str(payload_['cross']),
            tools.get_optional_str(payload_['block']),
            tools.get_optional_str(payload_['pair']),
            tools.get_optional_str(payload_['reserved'])
        )

    def __init__(self, object_, cross_, block_, pair_, reserved_):
        self.object = object_
        self.cross = cross_
        self.block = block_
        self.pair = pair_
        self.reserved = reserved_

    def __dir__(self):
        return [
            'object', 'cross', 'block', 'pair', 'reserved'
        ]


def create(raw_message_, payload_):
    component = payload_['report-block']['abonents']
    oid = component['id']
    if oid == asn1.sorm_report_abonent_abonent:
        return SubscriberReport.create(
            raw_message_, payload_, component['data']
        )
    if oid == asn1.sorm_report_abonent_service:
        return ServiceReport.create(raw_message_, payload_, component['data'])
    raise exceptions.GeneralFault(
        f'unable to create subscriber report data block ' +
        f'by the "{str(oid)}" OID'
    )
