from pyasn1.codec.ber.decoder import decode as ber_decode

from apps.kernel.infrastructure.messaging.report import report
from apps.kernel.infrastructure.messaging.report.payload.general import addresses
from apps.kernel.infrastructure.messaging import (
    tools,
    network,
)
from apps.system.lib import (
    exceptions,
    basic,
    asn1,
)


class BunchesReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrBunchesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, BunchesReportRecord.create
        )
        return BunchesReport(
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
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class BunchesReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrBunchRecord):
        return BunchesReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['bunch-type']),
            str(payload_['bunch-id']),
            str(payload_['switch-id']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, bunch_type_,
                 bunch_id_, switch_id_, description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.bunch_type = bunch_type_
        self.bunch_id = bunch_id_
        self.switch_id = switch_id_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'bunch_type', 'bunch_id',
            'switch_id', 'description'
        ]


class SwitchesReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrSwitchesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, SwitchesReportRecord.create
        )
        return SwitchesReport(
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
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class SwitchesReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrSwitchesRecord):
        return SwitchesReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['network-type']),
            int(payload_['switch-type']),
            str(payload_['switch-id']),
            tools.get_optional_str(payload_['switch-sign']),
            addresses.ReportedAddress.create(payload_['address']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, network_type_,
                 switch_type_, switch_id_, switch_sign_, address_,
                 description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.network_type = network_type_
        self.switch_type = switch_type_
        self.switch_id = switch_id_
        self.switch_sign = switch_sign_
        self.address = address_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'network_type',
            'switch_type', 'switch_id', 'switch_sign', 'address', 'description'
        ]


class GatesReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrGatesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, GatesReportRecord.create
        )
        return GatesReport(
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
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class GatesReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrGatesRecord):
        return GatesReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['gate-type']),
            int(payload_['gate-id']),
            tools.sequence_of_to_list(
                payload_['ip-list'], network.NetworkPeerInfo.create
            ),
            addresses.ReportedAddress.create(payload_['address']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, gate_type_,
                 gate_id_, ip_list_, address_, description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.gate_type = gate_type_
        self.gate_id = gate_id_
        self.ip_list = ip_list_
        self.address = address_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'gate_type', 'gate_id',
            'ip_list', 'address', 'description'
        ]


class CallTypesReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrCallTypesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, CallTypesReportRecord.create
        )
        return CallTypesReport(
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


class CallTypesReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrCallsTypesRecord):
        return CallTypesReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['call-type-id']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, call_type_id_,
                 description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.call_type_id = call_type_id_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'call_type_id',
            'description'
        ]


class SupplementServicesReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrSupplementServicesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, SupplementServicesReportRecord.create
        )
        return SupplementServicesReport(
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


class SupplementServicesReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrSupplementServicesRecord):
        return SupplementServicesReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['service-id']),
            str(payload_['mnemonic']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, service_id_,
                 mnemonic_, description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.service_id = service_id_
        self.mnemonic = mnemonic_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'service_id',
            'mnemonic', 'description'
        ]


class PayTypesReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrPayTypesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, PayTypesReportRecord.create
        )
        return PayTypesReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'], int(message_payload_['request-id']),
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


class PayTypesReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrPayTypesRecord):
        return PayTypesReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['pay-type-id']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_,
                 pay_type_id_, description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.pay_type_id = pay_type_id_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'pay_type_id',
            'description'
        ]


class TerminationCausesReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrTerminationCausesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, TerminationCausesReportRecord.create
        )
        return TerminationCausesReport(
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


class TerminationCausesReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrTerminationCausesRecord):
        return TerminationCausesReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['network-type']),
            int(payload_['termination-cause-id']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, network_type_,
                 termination_cause_id_, description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.network_type = network_type_
        self.termination_cause_id = termination_cause_id_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'network_type',
            'termination_cause_id', 'description'
        ]


class IPNumberingPlansReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrIpNumberingPlanRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, IPNumberingPlansReportRecord.create
        )
        return IPNumberingPlansReport(
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


class IPNumberingPlansReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrIpNumberingPlanRecord):
        return IPNumberingPlansReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            network.IPAddress.create(payload_['network-address']),
            network.IPMask.create(payload_['network-mask']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, network_address_,
                 network_mask_, description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.network_address = network_address_
        self.network_mask = network_mask_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'network_address',
            'network_mask', 'description'
        ]


class TelephoneNumberingPlansReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_),
            asn1.SkrTelephoneNumberingPlanRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, TelephoneNumberingPlansReportRecord.create
        )
        return TelephoneNumberingPlansReport(
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

    def __init__(self, version_, message_id_, message_time_,
                 operator_name_, id_, request_id_, task_id_, total_blocks_,
                 data_block_number_, records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class TelephoneNumberingPlansReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrTelephoneNumberingPlanRecord):
        return TelephoneNumberingPlansReportRecord(
            int(payload_['telco-id']),
            str(payload_['iso-3166-alpha-2']),
            str(payload_['iso-3166-alpha-3']),
            str(payload_['country-code']),
            str(payload_['national-significant-number']),
            int(payload_['area-code-length']),
            int(payload_['min-subscr-nr-length']),
            int(payload_['max-subscr-nr-length']),
            int(payload_['utc-min']),
            int(payload_['utc-max']),
            str(payload_['destination']),
            int(payload_['operator-type-id']),
            str(payload_['capacity-from']),
            str(payload_['capacity-to']),
            int(payload_['capacity-size']),
            str(payload_['location']),
            str(payload_['registrar']),
            str(payload_['range-activation']),
            str(payload_['mobile-country-code']),
            str(payload_['mobile-network-code']),
            tools.get_optional_str(payload_['range-deactivation']),
            tools.get_optional_str(payload_['range-status']),
            tools.get_optional_str(payload_['description']),
            tools.get_optional_str(payload_['operating-company-number'])
        )

    def __init__(self, telco_code_, iso_3166_alpha_2_, iso_3166_alpha_3_,
                 country_code_, national_significant_number_,
                 area_code_length_, min_subscr_nr_length_,
                 max_subscr_nr_length_, utc_min_, utc_max_, destination_,
                 operator_type_id_, capacity_from_, capacity_to_,
                 capacity_size_, location_, registrar_, range_activation_,
                 mobile_country_code_, mobile_network_code_,
                 range_deactivation_, range_status_, description_,
                 operating_company_number_):
        self.telco_code = telco_code_
        self.iso_3166_alpha_2 = iso_3166_alpha_2_
        self.iso_3166_alpha_3 = iso_3166_alpha_3_
        self.country_code = country_code_
        self.national_significant_number = national_significant_number_
        self.area_code_length = area_code_length_
        self.min_subscr_nr_length = min_subscr_nr_length_
        self.max_subscr_nr_length = max_subscr_nr_length_
        self.utc_min = utc_min_
        self.utc_max = utc_max_
        self.destination = destination_
        self.operator_type_id = operator_type_id_
        self.capacity_from = capacity_from_
        self.capacity_to = capacity_to_
        self.capacity_size = capacity_size_
        self.location = location_
        self.registrar = registrar_
        self.range_activation = range_activation_
        self.mobile_country_code = mobile_country_code_
        self.mobile_network_code = mobile_network_code_
        self.range_deactivation = range_deactivation_
        self.range_status = range_status_
        self.description = description_
        self.operating_company_number = operating_company_number_

    def __dir__(self):
        return [
            'telco_code', 'iso_3166_alpha_2', 'iso_3166_alpha_3',
            'country_code', 'national_significant_number', 'area_code_length',
            'min_subscr_nr_length', 'max_subscr_nr_length', 'utc_min',
            'utc_max', 'destination', 'operator_type_id', 'capacity_from',
            'capacity_to', 'capacity_size', 'location', 'registrar',
            'range_activation', 'mobile_country_code', 'mobile_network_code',
            'range_deactivation', 'range_status', 'description',
            'operating_company_number'
        ]


class DocumentTypesReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrDocTypesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, DocumentTypesReportRecord.create
        )
        return DocumentTypesReport(
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
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class DocumentTypesReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrDocTypesRecord):
        return DocumentTypesReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['doc-type-id']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, doc_type_id_,
                 description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.doc_type_id = doc_type_id_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'doc_type_id', 'description'
        ]


class TelcosReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrTelcosRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, TelcosReportRecord.create
        )
        return TelcosReport(
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


class TelcosReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrTelcosRecord):
        return TelcosReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            str(payload_['description']),
            tools.get_optional_str(payload_['mcc']),
            tools.get_optional_str(payload_['mnc'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, description_,
                 mcc_, mnc_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.description = description_
        self.mcc = mcc_
        self.mnc = mnc_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'description', 'mcc',
            'mnc'
        ]


class IPDataPointsReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrIpDataPointsRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, IPDataPointsReportRecord.create
        )
        return IPDataPointsReport(
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


class IPDataPointsReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrIpDataPointRecord):
        return IPDataPointsReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            int(payload_['point-id']),
            str(payload_['description'])
        )

    def __init__(self, telco_code_, begin_time_, end_time_, point_id_,
                 description_):
        self.telco_code = telco_code_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.point_id = point_id_
        self.description = description_

    def __dir__(self):
        return [
            'telco_code', 'begin_time', 'end_time', 'point_id', 'description'
        ]


class BunchesMapReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrBunchesMapRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, BunchesMapReportRecord.create
        )
        return BunchesMapReport(
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


class BunchesMapReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrBunchesMapRecord):
        return BunchesMapReportRecord(
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            BunchMapPoint.create(payload_['a-bunch']),
            BunchMapPoint.create(payload_['b-bunch'])
        )

    def __init__(self, begin_time_, end_time_, a_bunch_, b_bunch_):
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.a_bunch = a_bunch_
        self.b_bunch = b_bunch_

    def __dir__(self):
        return [
            'begin_time', 'end_time', 'a_bunch', 'b_bunch'
        ]


class BunchMapPoint(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrBunchMapPoint):
        return BunchMapPoint(
            int(payload_['telco-id']),
            str(payload_['switch-id']),
            network.Bunch.create(payload_['bunch-id'])
        )

    def __init__(self, telco_code_, switch_id_, bunch_id_):
        self.telco_code = telco_code_
        self.switch_id = switch_id_
        self.bunch_id = bunch_id_

    def __dir__(self):
        return [
            'telco_code', 'switch_id_', 'bunch_id'
        ]


class SpecialNumbersReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrSpecialNumbersRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, SpecialNumbersReportRecord.create
        )
        return SpecialNumbersReport(
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


class SpecialNumbersReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrSpecialNumberRecord):
        return SpecialNumbersReportRecord(
            int(payload_['telco-id']),
            str(payload_['directory-number']),
            str(payload_['description']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time']),
            tools.get_optional_ip_address(payload_['network-address'])
        )

    def __init__(self, telco_code_, directory_number_, description_,
                 begin_time_, end_time_, network_address_):
        self.telco_code = telco_code_
        self.directory_number = directory_number_
        self.description = description_
        self.begin_time = begin_time_
        self.end_time = end_time_
        self.network_address = network_address_

    def __dir__(self):
        return [
            'telco_code', 'directory_number', 'description', 'begin_time',
            'end_time', 'network-address'
        ]


class SS7SignalPointCodeReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrSignalPointCodesRecordsData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, SS7SignalPointCodeReportRecord.create
        )
        return SS7SignalPointCodeReport(
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


class SS7SignalPointCodeReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrSignalPointCodesRecord):
        return SS7SignalPointCodeReportRecord(
            int(payload_['ss7-point-code']),
            str(payload_['switch-id']),
            str(payload_['description']),
            str(payload_['begin-time']),
            tools.get_optional_str(payload_['end-time'])
        )

    def __init__(self, code_, switch_id_, description_, begin_time_,
                 end_time_):
        self.code = code_
        self.switch_id = switch_id_
        self.description = description_
        self.begin_time = begin_time_
        self.end_time = end_time_

    def __dir__(self):
        return [
            'code', 'switch_id', 'description', 'begin_time', 'end_time'
        ]


def create(raw_message_, payload_):
    component = payload_['report-block']['dictionary']
    oid = component['id']
    creator = report_creators.get(oid, None)
    if creator is None or not callable(creator):
        raise exceptions.GeneralFault(
            f'unable to create dictionary report data ' +
            f'block by the "{str(oid)}" OID'
        )
    return creator(raw_message_, payload_, component['data'])


report_creators = {
    asn1.sorm_report_dictionary_bunches: BunchesReport.create,
    asn1.sorm_report_dictionary_switches: SwitchesReport.create,
    asn1.sorm_report_dictionary_gates: GatesReport.create,
    asn1.sorm_report_dictionary_call_types: CallTypesReport.create,
    asn1.sorm_report_dictionary_supplement_services: SupplementServicesReport.create,
    asn1.sorm_report_dictionary_pay_types: PayTypesReport.create,
    asn1.sorm_report_dictionary_termination_causes: TerminationCausesReport.create,
    asn1.sorm_report_dictionary_ip_numbering_plan: IPNumberingPlansReport.create,
    asn1.sorm_report_dictionary_phone_numbering_plan: TelephoneNumberingPlansReport.create,
    asn1.sorm_report_dictionary_doc_types: DocumentTypesReport.create,
    asn1.sorm_report_dictionary_telcos: TelcosReport.create,
    asn1.sorm_report_dictionary_ip_data_points: IPDataPointsReport.create,
    asn1.sorm_report_dictionary_bunches_map: BunchesMapReport.create,
    asn1.sorm_report_dictionary_special_numbers: SpecialNumbersReport.create,
    asn1.sorm_report_dictionary_signal_point_codes: SS7SignalPointCodeReport.create
}
