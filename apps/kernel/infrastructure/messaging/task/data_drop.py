from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import asn1
from apps.kernel.infrastructure.messaging import (
    base,
    tools,
)


class DataDropRequest(base.OutgoingMessage):

    def __init__(self, task_id_):
        super().__init__(None, asn1.sorm_message_task)
        self.task_id = task_id_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['task_id'])
        return fields

    def encode_data(self):
        reqs = asn1.SkrDataDropRequest(
            value=(self.task_id),
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)
                )
            )
        )
        return der_encode(reqs)


class DataDropResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        return DataDropResponse(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_value(raw_message_['operator-name']),
            raw_message_['id'],
            int(payload_['task-id']),
            bool(payload_['successful']),
            tools.get_optional_str(payload_['error-description'])
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, task_id_, successful_, error_description_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
        self.task_id = task_id_
        self.successful = successful_
        self.error_description = error_description_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['task_id', 'successful', 'error_description'])
        return fields
