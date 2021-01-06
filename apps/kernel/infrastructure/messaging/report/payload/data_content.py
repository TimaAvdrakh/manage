from pyasn1.codec.ber.decoder import decode as ber_decode

from apps.kernel.infrastructure.messaging import tools
from apps.kernel.infrastructure.messaging.report import report
from apps.system.lib import (
    exceptions,
    basic,
    asn1,
)


class RawRecordContentReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_),
            asn1.NRST_ReportDataContentRawData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, RawRecordContentRecord.create
        )
        return RawRecordContentReport(
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


class RawRecordContentRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_RawRecordContent):
        return RawRecordContentRecord(
            bool(payload_['successful']),
            tools.get_optional_bytes(payload_['data']),
            tools.get_optional_str(payload_['error']),
            tools.get_optional_str(payload_['codec-info']),
            tools.get_optional_int(payload_['direction'])
        )

    def __init__(self, successful_, data_, error_, codec_info_, direction_):
        self.successful = successful_
        self.data = data_
        self.error = error_
        self.codec_info = codec_info_
        self.direction = direction_
        self.data_info = None if self.data is None else f'{len(self.data)} bytes binary data'

    def __dir__(self):
        return [
         'successful', 'data_info', 'error', 'codec_info', 'direction'
        ]


def create(raw_message_, payload_):
    component = payload_['report-block']['data-content']
    oid = component['id']
    if oid == asn1.sorm_report_data_content_raw:
        return RawRecordContentReport.create(
            raw_message_, payload_, component['data']
        )
    raise exceptions.GeneralFault(
        f'unable to create data content report data block' +
        f' by the "{str(oid)}" OID'
    )
