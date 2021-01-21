from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import asn1
from apps.kernel.infrastructure.messaging import (
    base,
    tools,
)


class DataLoadRequest(base.OutgoingMessage):

    def __init__(self, task_id):
        super().__init__(None, asn1.sorm_message_task)
        self.task_id = task_id

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['task_id'])
        return fields

    def encode_data(self):
        reqs = asn1.SkrDataLoadRequest(
            value=self.task_id,
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
                )
            )
        )
        return der_encode(reqs)


class DataLoadResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message, payload):
        return DataLoadResponse(
            raw_message['version'],
            raw_message['message-id'],
            raw_message['message-time'],
            tools.get_optional_value(raw_message['operator-name']),
            raw_message['id'],
            int(payload['task-id']),
            bool(payload['data-exists']),
            tools.get_optional_int(payload['data-blocks-number']),
            tools.get_optional_str(payload['error-description'])
        )

    def __init__(self, version, message_id, message_time, operator_name,
                 id, task_id, data_exists, data_blocks_number,
                 error_description):
        super().__init__(
            version, message_id, message_time, operator_name, id
        )
        self.task_id = task_id
        self.data_exists = data_exists
        self.data_blocks_number = data_blocks_number
        self.error_description = error_description

    def __dir__(self):
        fields = super().__dir__()
        fields.extend([
            'task_id',
            'data_exists',
            'data_blocks_number',
            'error_description'
        ])
        return fields
