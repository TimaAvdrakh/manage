from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from .. import base
from .. import tools
from apps.system.lib import (
    asn1,
    exceptions,
)


class RawRequest(base.OutgoingMessage):

    def __init__(self, telco_codes_, task_):
        super().__init__(None, asn1.sorm_message_unformatted)
        self.telco_codes = telco_codes_
        self.task = task_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['telco_codes', 'task'])
        return fields

    def encode_data(self):
        reqs = asn1.NRST_RawRequest(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
                )
            )
        )
        if self.telco_codes is not None:
            tools.copy_list_to_sequence_of(
                reqs.getComponentByName('telcos'), self.telco_codes
            )
        reqs.setComponentByName('raw-task', self.task.to_asn1())
        return der_encode(reqs)


class RawDataType(object):
    data_reports = 0
    raw_cdr = 1
    raw_ipdr = 2
    raw_location = 10
    raw_passive = 11


class DataTypesRequest(base.ASN1Constructable):

    def __init__(self, raw_data_type_):
        self.raw_data_type = raw_data_type_

    def __dir__(self):
        return ['raw_data_type']

    def to_asn1(self):
        task = asn1.NRST_RawRequestTask()
        task.setComponentByName('data-types-request', self.raw_data_type)
        return task


class DataTypesResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        return DataTypesResponse(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            payload_['successful'],
            payload_['selected-type'],
            payload_['time-from'],
            payload_['time-to']
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, successful_, selected_type_, time_from_, time_to_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
        self.successful = successful_
        self.selected_type = selected_type_
        self.time_from = time_from_
        self.time_to = time_to_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['successful', 'selected_type', 'time_from', 'time_to'])
        return fields


class DataStartRequest(base.ASN1Constructable):

    def __init__(self, time_from_, time_to_, raw_data_type_):
        self.time_from = tools.to_date_and_time(time_from_)
        self.time_to = tools.to_date_and_time(time_to_)
        self.raw_data_type = raw_data_type_

    def __dir__(self):
        return ['time_from', 'time_to', 'raw_data_type']

    def to_asn1(self):
        task = asn1.NRST_RawRequestTask()
        body = task.getComponentByName('data-start-request')
        body['time-from'] = self.time_from
        body['time-to'] = self.time_to
        body['raw-type'] = self.raw_data_type
        return task


class DataStartResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        return DataStartResponse(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            payload_
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, successful_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
        self.successful = successful_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['successful'])
        return fields


class DataStopRequest(base.ASN1Constructable):

    def __init__(self):
        pass

    def __dir__(self):
        return []

    def to_asn1(self):
        task = asn1.NRST_RawRequestTask()
        task.setComponentByName('data-stop-request')
        return task


class DataStopResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        return DataStopResponse(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            payload_
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, successful_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
        self.successful = successful_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['successful'])
        return fields


class RawReport(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_: asn1.NRST_RawReport):
        report_block = payload_['report-block']
        if report_block.getName() != 'raw-cdr':
            raise exceptions.GeneralFault(
                'non raw bytes report block is not supported'
            )
        records = tools.sequence_of_to_list(report_block['raw-cdr'], str)
        return RawReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(payload_['request-id']),
            str(payload_['stream-id']),
            int(payload_['total-blocks-number']),
            int(payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, stream_id_, total_blocks_, block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
        self.request_id = request_id_
        self.stream_id = stream_id_
        self.total_blocks = total_blocks_
        self.block_number = block_number_
        self.records = records_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend([
            'request_id', 'stream_id', 'total_blocks', 'block_number'
        ])
        return fields


class RawAcknowledgement(base.OutgoingMessage):

    def __init__(self, message_id_, successful_, broken_record_,
                 error_description_):
        super().__init__(message_id_, asn1.sorm_message_unformatted)
        self.successful = successful_
        self.broken_record = broken_record_
        self.error_description = error_description_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['successful', 'broken_record', 'error_description'])
        return fields

    def encode_data(self):
        ack = asn1.NRST_Acknowledgement(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
                )
            )
        )
        ack.setComponentByName('successful', self.successful)
        if self.broken_record is not None:
            ack.setComponentByName('broken-record', self.broken_record)
        if self.error_description is not None:
            ack.setComponentByName('error-description', self.error_description)
        return der_encode(ack)
