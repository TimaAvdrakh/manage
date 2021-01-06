from apps.system.lib import exceptions


def create_typed_message(raw_message_, payload_):
    name = payload_.getName()
    creator = message_creators.get(name, None)
    if creator is None or not callable(creator):
        raise exceptions.GeneralFault(
            f'unable to chose trap message by "{name}" name'
        )
    return creator(raw_message_, payload_.getComponent())


from . import trap

message_creators = {
    'trap': trap.create_trap,
    'trap-ack': trap.TrapAck.create
}
