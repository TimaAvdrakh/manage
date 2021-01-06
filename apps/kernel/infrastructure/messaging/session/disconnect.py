from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import asn1
from apps.kernel.infrastructure.messaging import (
    base,
    tools,
)


class DisconnectRequest(base.OutgoingMessage):

    def __init__(self):
        super().__init__(None, asn1.sorm_message_session)

    def encode_data(self):
        reqs = asn1.NRST_DisconnectRequest(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        return der_encode(reqs)


class DisconnectResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        return DisconnectResponse(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_value(raw_message_['operator-name']),
            raw_message_['id']
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
