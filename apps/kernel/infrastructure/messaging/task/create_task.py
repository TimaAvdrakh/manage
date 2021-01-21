from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import asn1
from apps.kernel.infrastructure.messaging import (
    base,
    tools,
)


class CreateTaskRequest(base.OutgoingMessage):

    def __init__(self, telco_codes, range_, report_limit, task):
        super().__init__(None, asn1.sorm_message_task)
        self.telco_codes = telco_codes
        self.range = range_
        self.report_limit = report_limit
        self.task = task

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['telco_codes', 'range', 'report_limit', 'task'])
        return fields

    def encode_data(self):
        reqs = asn1.SkrCreateTaskRequest(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(
                        tag.tagClassContext,
                        tag.tagFormatConstructed, 8
                    )
                )
            )
        )
        if self.telco_codes is not None:
            tools.copy_list_to_sequence_of(
                reqs.getComponentByName('telcos'), self.telco_codes
            )
        if self.range is not None:
            self.range.copy_to(reqs.getComponentByName('range'))
        if self.report_limit is not None:
            reqs.setComponentByName('report-limit', self.report_limit)
        task_body = self.task.to_asn1()
        reqs.getComponentByName(
            'task'
        ).setComponentByType(task_body.getTagSet(), task_body)
        return der_encode(reqs)


class CreateTaskResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message, payload):
        return CreateTaskResponse(
            raw_message['version'],
            raw_message['message-id'],
            raw_message['message-time'],
            tools.get_optional_str(raw_message['operator-name']),
            raw_message['id'],
            tools.get_optional_int(payload['task-id']),
            payload['successful'],
            tools.get_optional_str(payload['error-description'])
        )

    def __init__(self, version_, message_id, message_time, operator_name,
                 id_, task_id, successful, error_description):
        super().__init__(
            version_, message_id, message_time, operator_name, id_
        )
        self.task_id = task_id
        self.successful = successful
        self.error_description = error_description

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['task_id', 'successful', 'error_description'])
        return fields

