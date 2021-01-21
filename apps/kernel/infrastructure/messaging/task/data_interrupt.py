from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import asn1
from apps.kernel.infrastructure.messaging import (
    base,
    tools,
)


class DataInterruptRequest(base.OutgoingMessage):

    def __init__(self, task_id):
        super().__init__(None, asn1.sorm_message_task)
        self.task_id = task_id

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['task_id'])
        return fields

    def encode_data(self):
        reqs = asn1.SkrDataInterruptRequest(
            value=(self.task_id),
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)
                )
            )
        )
        return der_encode(reqs)


class DataInterruptResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message, payload):
        return DataInterruptResponse(
            raw_message['version'],
            raw_message['message-id'],
            raw_message['message-time'],
            tools.get_optional_value(raw_message['operator-name']),
            raw_message['id'],
            int(payload['request-id']),
            bool(payload['successful']),
            tools.get_optional_int(payload['data-blocks-available']),
            tools.get_optional_str(payload['error-description'])
        )

    def __init__(self, version, message_id, message_time, operator_name,
                 id_, request_id, successful, data_blocks_available,
                 error_description):
        super().__init__(
            version, message_id, message_time, operator_name, id_
        )
        self.request_id = request_id
        self.successful = successful
        self.data_blocks_available = data_blocks_available
        self.error_description = error_description

    def __dir__(self):
        fields = super().__dir__()
        fields.extend([
            'request_id', 'successful', 'data_blocks_available',
            'error_description'
        ])
        return fields
