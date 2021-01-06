from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import asn1
from .. import base
from .. import tools


class Trap(base.OutgoingMessage):

    def __init__(self, type_, trap_message_, reference_message_):
        super().__init__(None, asn1.sorm_message_trap)
        self.type = type_
        self.trap_message = trap_message_
        self.reference_message = reference_message_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['type', 'trap_message', 'reference_message'])
        return fields

    def encode_data(self):
        reqs = asn1.NRST_Trap(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
                )
            )
        )
        reqs['trap-type'] = self.type
        if self.trap_message is not None:
            reqs['trap-message'] = self.trap_message
        if self.reference_message is not None:
            reqs['reference-message'] = self.reference_message
        return der_encode(reqs)


class TrapAck(base.OutgoingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        message = TrapAck(raw_message_['message-id'])
        message.version = raw_message_['version']
        message.message_time = raw_message_['message-time']
        message.operator_name = tools.get_optional_value(
            raw_message_['operator-name']
        )
        return message

    def __init__(self, message_id_):
        super().__init__(message_id_, asn1.sorm_message_trap)

    def encode_data(self):
        return '\x81\x00'


class HeartbeatTrap(Trap):

    def __init__(self, trap_message, reference_message):
        super().__init__(
            asn1.NRST_TrapType('heartbeat'),
            trap_message,
            reference_message
        )


class RestartSoftwareTrap(Trap):

    def __init__(self, trap_message, reference_message):
        super().__init__(
            asn1.NRST_TrapType('restart-software'),
            trap_message,
            reference_message
        )


class UnauthorizedAccessTrap(Trap):

    def __init__(self, trap_message, reference_message):
        super().__init__(
            asn1.NRST_TrapType('unauthorized-access'),
            trap_message,
            reference_message
        )


class CriticalErrorTrap(Trap):

    def __init__(self, trap_message, reference_message):
        super().__init__(
            asn1.NRST_TrapType('critical-error'),
            trap_message,
            reference_message
        )


class MajorErrorTrap(Trap):

    def __init__(self, trap_message, reference_message):
        super().__init__(
            asn1.NRST_TrapType('major-error'), trap_message, reference_message
        )


class MinorErrorTrap(Trap):

    def __init__(self, trap_message, reference_message):
        super().__init__(
            asn1.NRST_TrapType('minor-error'), trap_message, reference_message
        )


def create_trap(raw_message_, payload_):
    trap_type = str(payload_['trap-type'])
    trap_message = tools.get_optional_value(payload_['trap-message'])
    reference_message = tools.get_optional_value(payload_['reference-message'])
    if trap_type == 'heartbeat':
        message = HeartbeatTrap(trap_message, reference_message)
    else:
        if trap_type == 'restart-software':
            message = RestartSoftwareTrap(
                trap_message, reference_message
            )
        else:
            if trap_type == 'unauthorized-access':
                message = UnauthorizedAccessTrap(
                    trap_message, reference_message
                )
            else:
                if trap_type == 'critical-error':
                    message = CriticalErrorTrap(
                        trap_message,
                        reference_message)
                else:
                    if trap_type == 'major-error':
                        message = MajorErrorTrap(
                            trap_message,
                            reference_message)
                    else:
                        if trap_type == 'minor-error':
                            message = MinorErrorTrap(
                                trap_message, reference_message
                            )
                        else:
                            message = Trap(
                                payload_['trap-type'],
                                trap_message,
                                reference_message
                            )
    message.message_id = raw_message_['message-id']
    message.version = raw_message_['version']
    message.message_time = raw_message_['message-time']
    message.operator_name = tools.get_optional_value(
        raw_message_['operator-name']
    )
    return message
