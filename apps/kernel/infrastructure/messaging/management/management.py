from apps.system.lib import asn1
from apps.kernel.infrastructure.messaging import base


class GetStructureRequest(base.OutgoingMessage):

    def __init__(self):
        super().__init__(None, asn1.sorm_message_management)

    def encode_data(self):
        return '\xa0\x02\x80\x00'
