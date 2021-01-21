from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import (
    asn1,
    basic,
)
from apps.kernel.infrastructure.messaging import (
    base,
    tools,
)


class DataReadyRequest(base.OutgoingMessage):

    def __init__(self):
        super().__init__(None, asn1.sorm_message_task)

    def encode_data(self):
        reqs = asn1.SkrDataReadyRequest(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
                )
            )
        )
        return der_encode(reqs)


class TaskStatus(basic.PrintableObject):

    def __init__(self, task_id, status, report_records,
                 report_limit_exceeded, error_description):
        self.task_id = task_id
        self.status = status
        self.report_records = report_records
        self.report_limit_exceeded = report_limit_exceeded
        self.error_description = error_description

    def __dir__(self):
        return [
            'task_id', 'status', 'report_records', 'report_limit_exceeded',
            'error_description'
        ]


class DataReadyResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message, payload):
        return DataReadyResponse(
            raw_message['version'],
            raw_message['message-id'],
            raw_message['message-time'],
            tools.get_optional_value(raw_message['operator-name']),
            raw_message['id'],
            payload
        )

    def __init__(self, version, message_id, message_time, operator_name,
                 id_, task_statuses):
        super().__init__(
            version, message_id, message_time, operator_name, id_
        )

        def transform(asn1_item):
            task_id = int(asn1_item['task-id'])
            result = asn1_item['result']
            return TaskStatus(
                task_id,
                tools.get_optional_int(result['result']),
                tools.get_optional_int(result['report-records-number']),
                tools.get_optional_bool(result['report-limit-exeeded']),
                tools.get_optional_str(result['error-description'])
            )

        self.task_statuses = tools.sequence_of_to_list(
            task_statuses, transform
        )

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['task_statuses'])
        return fields
