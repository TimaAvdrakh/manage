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

    def __init__(self, task_id_, status_, report_records_,
                 report_limit_exceeded_, error_description_):
        self.task_id = task_id_
        self.status = status_
        self.report_records = report_records_
        self.report_limit_exceeded = report_limit_exceeded_
        self.error_description = error_description_

    def __dir__(self):
        return [
            'task_id', 'status', 'report_records', 'report_limit_exceeded',
            'error_description'
        ]


class DataReadyResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        return DataReadyResponse(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_value(raw_message_['operator-name']),
            raw_message_['id'],
            payload_
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, task_statuses_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )

        def transform(asn1_item_):
            task_id = int(asn1_item_['task-id'])
            result = asn1_item_['result']
            return TaskStatus(
                task_id,
                tools.get_optional_int(result['result']),
                tools.get_optional_int(result['report-records-number']),
                tools.get_optional_bool(result['report-limit-exeeded']),
                tools.get_optional_str(result['error-description'])
            )

        self.task_statuses = tools.sequence_of_to_list(
            task_statuses_, transform
        )

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['task_statuses'])
        return fields
