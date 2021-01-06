from apps.system.lib import exceptions


def create_typed_message(raw_message_, payload_):
    name = payload_.getName()
    creator = message_creators.get(name, None)
    if creator is None or not callable(creator):
        raise exceptions.GeneralFault(
            f'unable to chose session message by "{name}" name'
        )
    return creator(raw_message_, payload_.getComponent())


from .connect import ConnectResponse
from .adjustment import AdjustmentResponse
from .disconnect import DisconnectResponse

message_creators = {
    'connect-response': ConnectResponse.create,
    'adjustment-response': AdjustmentResponse.create,
    'disconnect-response': DisconnectResponse.create
}
