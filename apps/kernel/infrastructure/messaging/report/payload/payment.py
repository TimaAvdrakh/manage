from pyasn1.codec.ber.decoder import decode as ber_decode

from apps.kernel.infrastructure.messaging.report import report
from apps.kernel.infrastructure.messaging.report.payload.general import (
    addresses,
    identifiers,
)
from apps.kernel.infrastructure.messaging import (
    tools,
    locations,
)

from apps.system.lib import (
    exceptions,
    basic,
    asn1,
)


class BankTransactionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrBankTransactionReportData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, BankTransactionReportRecord.create
        )
        return BalanceFillUpReport(
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


class BankTransactionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrBankTransactionRecord):
        return BankTransactionReportRecord(
            int(payload_['telco-id']),
            identifiers.create(payload_['device-id']),
            str(payload_['date-time-fillup']),
            str(payload_['bank-account']),
            str(payload_['bank-name']),
            addresses.ReportedAddress.create(payload_['bank-address']),
            float(payload_['amount'])
        )

    def __init__(self, telco_code_, identifier_, date_fill_up_,
                 bank_account_, bank_name_, bank_address_, amount_):
        self.telco_code = telco_code_
        self.identifier = identifier_
        self.date_fill_up = date_fill_up_
        self.bank_account = bank_account_
        self.bank_name = bank_name_
        self.bank_address = bank_address_
        self.amount = amount_

    def __dir__(self):
        return [
            'telco_code', 'identifier', 'date_fill_up', 'bank_account',
            'bank_name', 'bank_address', 'amount'
        ]


class ExpressCardReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrExpressCardReportData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, ExpressCardReportRecord.create
        )
        return ExpressCardReport(
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


class ExpressCardReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrExpressPaysRecord):
        return ExpressCardReportRecord(
            int(payload_['telco-id']),
            identifiers.create(payload_['device-id']),
            str(payload_['date-time-fillup']),
            str(payload_['card-number']),
            float(payload_['amount'])
        )

    def __init__(self, telco_code_, identifier_, date_fill_up_,
                 card_number_, amount_):
        self.telco_code = telco_code_
        self.identifier = identifier_
        self.date_fill_up = date_fill_up_
        self.card_number = card_number_
        self.amount = amount_

    def __dir__(self):
        return [
            'telco_code', 'identifier', 'date_fill_up', 'card_number', 'amount'
        ]


class PublicTerminalReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrPublicTerminalReportData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, PublicTerminalReportRecord.create
        )
        return ExpressCardReport(
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


class PublicTerminalReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrPublicTerminalRecord):
        return PublicTerminalReportRecord(
            int(payload_['telco-id']),
            identifiers.create(payload_['device-id']),
            str(payload_['date-time-fillup']),
            str(payload_['terminal-id']),
            str(payload_['terminal-number']),
            addresses.ReportedAddress.create(payload_['terminal-address']),
            float(payload_['amount']),
            tools.get_optional_value(
                payload_['location'], locations.Location.create
            )
        )

    def __init__(self, telco_code_, identifier_, date_fill_up_, terminal_id_,
                 terminal_number_, terminal_address_, amount_, location_):
        self.telco_code = telco_code_
        self.identifier = identifier_
        self.date_fill_up = date_fill_up_
        self.terminal_id = terminal_id_
        self.terminal_number = terminal_number_
        self.terminal_address = terminal_address_
        self.amount = amount_
        self.location = location_

    def __dir__(self):
        return [
            'telco_code', 'identifier', 'date_fill_up', 'terminal_id',
            'terminal_number', 'terminal_address', 'amount', 'location'
        ]


class ServiceCenterReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrServiceCenterReport()
        )
        records = tools.sequence_of_to_list(
            sequence_of, ServiceCenterReportRecord.create
        )
        return ExpressCardReport(
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


class ServiceCenterReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrServiceCenterRecord):
        return ServiceCenterReportRecord(
            int(payload_['telco-id']),
            identifiers.create(payload_['device-id']),
            str(payload_['date-time-fillup']),
            str(payload_['center-id']),
            addresses.ReportedAddress.create(payload_['center-address']),
            float(payload_['amount'])
        )

    def __init__(self, telco_code_, identifier_, date_fill_up_, center_id_,
                 center_address_, amount_):
        self.telco_code = telco_code_
        self.identifier = identifier_
        self.date_fill_up = date_fill_up_
        self.center_id = center_id_
        self.center_address = center_address_
        self.amount = amount_

    def __dir__(self):
        return [
            'telco_code', 'identifier', 'date_fill_up', 'center_id',
            'center_address', 'amount'
        ]


class CrossAccountReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrCrossAccountReportData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, CrossAccountReportRecord.create
        )
        return ExpressCardReport(
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


class CrossAccountReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrCrossAccountRecord):
        return CrossAccountReportRecord(
            int(payload_['telco-id']),
            identifiers.create(payload_['device-id']),
            str(payload_['date-time-fillup']),
            identifiers.create(payload_['donanted-id']),
            float(payload_['amount'])
        )

    def __init__(self, telco_code_, receiver_, date_fill_up_, sender_,
                 amount_):
        self.telco_code = telco_code_
        self.receiver = receiver_
        self.date_fill_up = date_fill_up_
        self.sender = sender_
        self.amount = amount_

    def __dir__(self):
        return [
            'telco_code', 'receiver', 'date_fill_up', 'sender', 'amount'
        ]


class TelephoneCardReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrTelephoneCardReportData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, TelephoneCardReportRecord.create
        )
        return ExpressCardReport(
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


class TelephoneCardReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrValidateTelephoneCardRecord):
        return TelephoneCardReportRecord(
            int(payload_['telco-id']),
            identifiers.create(payload_['activator-device-id']),
            str(payload_['date-time-fillup']),
            str(payload_['card-number']),
            float(payload_['amount'])
        )

    def __init__(self, telco_code_, identifier_, date_fill_up_, card_number_,
                 amount_):
        self.telco_code = telco_code_
        self.identifier = identifier_
        self.date_fill_up = date_fill_up_
        self.card_number = card_number_
        self.amount = amount_

    def __dir__(self):
        return [
            'telco_code', 'identifier', 'date_fill_up', 'card_number', 'amount'
        ]


class BalanceFillUpReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.SkrBalanceFillupReportData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, BalanceFillUpReportRecord.create
        )
        return BalanceFillUpReport(
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


class BalanceFillUpReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.SkrValidateBalanceFillupRecord):
        return BalanceFillUpReportRecord(
            int(payload_['telco-id']),
            int(payload_['pay-type-id']),
            identifiers.create(payload_['device-id']),
            str(payload_['date-time-fillup']),
            float(payload_['amount']),
            tools.get_optional_str(payload_['pay-parameters'])
        )

    def __init__(self, telco_code_, pay_type_id_, identifier_,
                 date_fill_up_, amount_, parameters_):
        self.telco_code = telco_code_
        self.pay_type_id = pay_type_id_
        self.identifier = identifier_
        self.date_fill_up = date_fill_up_
        self.amount = amount_
        self.parameters = parameters_

    def __dir__(self):
        return [
            'telco_code', 'pay_type_id', 'identifier', 'date_fill_up',
            'amount', 'parameters'
        ]


def create(raw_message_, payload_):
    component = payload_['report-block']['payments']
    oid = component['id']
    creator = report_creators.get(oid, None)
    if creator is None or not callable(creator):
        raise exceptions.GeneralFault(
            f'unable to create payment report data block by' +
            f' the "{str(oid)}" OID'
        )
    return creator(raw_message_, payload_, component['data'])


report_creators = {
    asn1.sorm_report_payment_bank_transaction: BankTransactionReport.create,
    asn1.sorm_report_payment_express_pays: ExpressCardReport.create,
    asn1.sorm_report_payment_terminal_pays: PublicTerminalReport.create,
    asn1.sorm_report_payment_service_center: ServiceCenterReport.create,
    asn1.sorm_report_payment_cross_account: CrossAccountReport.create,
    asn1.sorm_report_payment_telephone_card: TelephoneCardReport.create,
    asn1.sorm_report_payment_balance_fillups: BalanceFillUpReport.create
}
