from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.system.lib import asn1
from apps.kernel.infrastructure.messaging import (
    base,
    tools,
)


class ConnectRequest(base.OutgoingMessage):

    def __init__(self, session_timeout_, max_data_length_,
                 data_packet_window_size_, data_load_timeout_,
                 request_response_timeout_, data_packet_response_timeout_):
        super().__init__(None, asn1.sorm_message_session)
        self.session_timeout = session_timeout_
        self.max_data_length = max_data_length_
        self.data_packet_window_size = data_packet_window_size_
        self.data_load_timeout = data_load_timeout_
        self.request_response_timeout = request_response_timeout_
        self.data_packet_response_timeout = data_packet_response_timeout_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend([
            'session_timeout',
            'max_data_length',
            'data_packet_window_size',
            'data_load_timeout',
            'request_response_timeout',
            'data_packet_response_timeout'
        ])
        return fields

    def encode_data(self):
        reqs = asn1.NRST_ConnectRequest(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
                )
            )
        )
        reqs['session-timeout'] = 60
        reqs['max-data-length'] = 1000
        reqs['data-packet-window-size'] = 5
        reqs['data-load-timeout'] = 60
        reqs['request-response-timeout'] = 60
        reqs['data-packet-response-timeout'] = 60

        reqs.getComponentByName(
            'session-timeout'
        )._value = self.session_timeout
        reqs.getComponentByName(
            'max-data-length'
        )._value = self.max_data_length
        reqs.getComponentByName(
            'data-packet-window-size'
        )._value = self.data_packet_window_size
        reqs.getComponentByName(
            'data-load-timeout'
        )._value = self.data_load_timeout
        reqs.getComponentByName(
            'request-response-timeout'
        )._value = self.request_response_timeout
        reqs.getComponentByName(
            'data-packet-response-timeout'
        )._value = self.data_packet_response_timeout
        return der_encode(reqs)


class ConnectResponse(base.IncomingMessage):

    @staticmethod
    def create(raw_message_, payload_):
        return ConnectResponse(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_value(raw_message_['operator-name']),
            raw_message_['id'],
            payload_['confirmed-data-packet-window-size'],
            payload_['confirmed-session-timeout'],
            payload_['confirmed-data-load-timeout'],
            payload_['confirmed-request-response-timeout'],
            payload_['supports']
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, confirmed_data_packet_window_size_,
                 confirmed_session_timeout_, confirmed_data_load_timeout_,
                 confirmed_request_response_timeout_, supports_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
        self.confirmed_data_packet_window_size = confirmed_data_packet_window_size_
        self.confirmed_session_timeout = confirmed_session_timeout_
        self.confirmed_data_load_timeout = confirmed_data_load_timeout_
        self.confirmed_request_response_timeout = confirmed_request_response_timeout_
        self.supports = tools.sequence_of_to_list(
            supports_, lambda item: bytes(item).decode()
        )

    def __dir__(self):
        fields = super().__dir__()
        fields.extend([
            'confirmed_data_packet_window_size',
            'confirmed_session_timeout',
            'confirmed_data_load_timeout',
            'confirmed_request_response_timeout',
            'supports'
        ])
        return fields
