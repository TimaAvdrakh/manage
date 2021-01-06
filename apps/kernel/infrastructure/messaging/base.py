import time
import threading

from pyasn1.type import univ
from pyasn1.codec.der.encoder import encode as der_encode
from pyasn1.codec.ber.decoder import decode as ber_decode

from apps.system.lib import (
    basic,
    exceptions,
    asn1,
)


class NamedString:

    def __init__(self, value_: str):
        self.value = value_

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.value}")'


class ASN1Constructable(basic.PrintableObject):

    def to_asn1(self):
        raise NotImplementedError('method is not implemented')


class ASN1Copyable(basic.PrintableObject):

    def copy_to(self, target_):
        raise NotImplementedError('method is not implemented')

    def set_component(self, target_, component_name_, value_):
        if value_ is not None:
            if isinstance(value_, ASN1Copyable):
                value_.copy_to(target_.getComponentByName(component_name_))
            else:
                target_.setComponentByName(component_name_, value_)


class ASN1ChoiceBase(ASN1Copyable):

    def __init__(self, asn1_choice_, component_name_, component_value_):
        if component_name_ not in asn1_choice_.componentType.keys():
            raise exceptions.GeneralFault(
                f'an invalid component name "{component_name_}" is ' +
                f'specified for the "{asn1_choice_.__class__.__name__}"' +
                f' ASN.1 CHOICE'
            )
        if component_value_ is None:
            raise exceptions.GeneralFault(
                f'a value for the "{component_name_}" component name of ' +
                f'the "{asn1_choice_.__class__.__name__}" ASN.1 CHOICE is ' +
                f'not specified'
            )
        self.asn1_choice = asn1_choice_
        self.component_name = component_name_
        self.component_value = component_value_

    def __repr__(self):
        return '{0}({1}: "{2}")'.format(
            self.__class__.__name__, self.component_name, self.component_value
        )


class BaseMessage(basic.PrintableObject):

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_):
        self.version = version_
        self.message_id = message_id_
        self.message_time = message_time_
        self.operator_name = operator_name_
        self.id = id_

    def __dir__(self):
        return [
            'version', 'message_id', 'message_time', 'operator_name', 'id'
        ]


class OutgoingMessage(BaseMessage):
    last_message_id = 0
    id_generation_lock = threading.Lock()

    @staticmethod
    def get_next_message_id():
        with OutgoingMessage.id_generation_lock:
            OutgoingMessage.last_message_id += 1
            return OutgoingMessage.last_message_id

    def __init__(self, message_id_, id_):
        super().__init__(
            asn1.vers,
            asn1.NRST_MessageID(
                message_id_ if message_id_ is not None else OutgoingMessage.get_next_message_id()
            ),
            asn1.NRST_DateAndTime(time.strftime('%y%m%d%H%M%SZ', time.localtime())),
            None,
            id_
        )

    def encode(self):
        message = asn1.NRST_Message()
        message['version'] = self.version
        message['message-id'] = self.message_id
        message['message-time'] = self.message_time
        message['id'] = self.id
        message['data'] = univ.Any(self.encode_data())
        return der_encode(message)

    def encode_data(self):
        raise NotImplementedError('method is not implemented')


IncomingMessage = BaseMessage


def create_typed_message(raw_message_):
    payload_id = str(raw_message_['id'])
    descriptor = message_descriptors.get(payload_id, None)
    if descriptor is None:
        raise exceptions.GeneralFault(
            'unable to recognize message with id: "{payload_id}"'
        )
    payload, rest = ber_decode(
        raw_message_['data'], descriptor.descriptor_reference()
    )
    return descriptor.creator(raw_message_, payload)


class PayloadDescriptor(object):

    def __init__(self, descriptor_reference_, creator_):
        self.descriptor_reference = descriptor_reference_
        self.creator = creator_


from .filter import factory as filter_factory
from .management import factory as management_factory
from .report import factory as report_factory
from .session import factory as session_factory
from .task import factory as task_factory
from .trap import factory as trap_factory
from .unformatted import factory as unformatted_factory

message_descriptors = {
    str(asn1.sorm_message_filter): PayloadDescriptor(
        asn1.NRST_FilterMessageData, filter_factory.create_typed_message
    ),
    str(asn1.sorm_message_management): PayloadDescriptor(
        asn1.NRST_ManagementMessageData,
        management_factory.create_typed_message
    ),
    str(asn1.sorm_message_report): PayloadDescriptor(
        asn1.NRST_ReportMessageData, report_factory.create_typed_message
    ),
    str(asn1.sorm_message_session): PayloadDescriptor(
        asn1.NRST_SessionMessageData, session_factory.create_typed_message
    ),
    str(asn1.sorm_message_task): PayloadDescriptor(
        asn1.NRST_TaskMessageData, task_factory.create_typed_message
    ),
    str(asn1.sorm_message_trap): PayloadDescriptor(
        asn1.NRST_TrapMessageData, trap_factory.create_typed_message
    ),
    str(asn1.sorm_message_unformatted): PayloadDescriptor(
        asn1.NRST_UnformattedMessageData,
        unformatted_factory.create_typed_message
    )
}
