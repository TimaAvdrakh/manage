from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import asn1
from apps.kernel.infrastructure.messaging import (
    base,
    tools,
)


class DataLoadRequest(base.OutgoingMessage):

    def __init__(self, task_id_):
        super().__init__(None, asn1.sorm_message_task)
        self.task_id = task_id_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['task_id'])
        return fields

    def encode_data(self):
        reqs = asn1.NRST_DataLoadRequest(
            value=(self.task_id),
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
                )
            )
        )
        return der_encode(reqs)


class DataLoadResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        return DataLoadResponse(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_value(raw_message_['operator-name']),
            raw_message_['id'],
            int(payload_['task-id']),
            bool(payload_['data-exists']),
            tools.get_optional_int(payload_['data-blocks-number']),
            tools.get_optional_str(payload_['error-description'])
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, task_id_, data_exists_, data_blocks_number_,
                 error_description_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
        self.task_id = task_id_
        self.data_exists = data_exists_
        self.data_blocks_number = data_blocks_number_
        self.error_description = error_description_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend([
            'task_id',
            'data_exists',
            'data_blocks_number',
            'error_description'
        ])
        return fields
