from apps.system.lib import exceptions


def create_typed_message(raw_message, payload):
    name = payload.getName()
    creator = message_creators.get(name, None)
    if creator is None or not callable(creator):
        raise exceptions.GeneralFault(
            f'unable to chose task message by "{name}" name'
        )
    return creator(raw_message, payload.getComponent())


from .create_task import CreateTaskResponse
from .data_ready import DataReadyResponse
from .data_load import DataLoadResponse
from .data_interrupt import DataInterruptResponse
from .data_drop import DataDropResponse

message_creators = {
    'create-task-response': CreateTaskResponse.create,
    'data-ready-response': DataReadyResponse.create,
    'data-load-response': DataLoadResponse.create,
    'data-interrupt-response': DataInterruptResponse.create,
    'data-drop-response': DataDropResponse.create
}
