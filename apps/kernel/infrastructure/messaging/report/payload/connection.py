from pyasn1.codec.ber.decoder import decode as ber_decode

from apps.kernel.infrastructure.messaging.report.payload.general import identifiers
from apps.system.lib import (
    exceptions,
    basic,
    asn1,
)
from apps.kernel.infrastructure.messaging import (
    tools,
    locations,
    network,
)
from apps.kernel.infrastructure.messaging.report import report


class PSTNConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_PstnRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, PSTNConnectionReportRecord.create
        )
        return PSTNConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class PSTNConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_PstnRecordContent):
        return PSTNConnectionReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-connection-time']),
            int(payload_['duration']),
            int(payload_['call-type-id']),
            int(payload_['supplement-service-id']),
            int(payload_['in-abonent-type']),
            int(payload_['out-abonent-type']),
            str(payload_['switch-id']),
            int(payload_['inbound-bunch']),
            int(payload_['outbound-bunch']),
            int(payload_['term-cause']),
            tools.get_optional_str(payload_['phone-card-number']),
            tools.get_optional_value(payload_['in-info'], identifiers.create),
            str(payload_['dialed-digits']),
            tools.get_optional_value(payload_['out-info'], identifiers.create),
            tools.get_optional_str(payload_['forwarding-identifier']),
            tools.get_optional_str(payload_['border-switch-id']),
            tools.get_optional_str(payload_['message']),
            tools.get_optional_str(payload_['ss7-opc']),
            tools.get_optional_str(payload_['ss7-dpc']),
            tools.get_optional_str(payload_['data-content-id'])
        )

    def __init__(self, telco_id_, begin_connection_time_, duration_,
                 call_type_id_, supplement_service_id_, in_abonent_type_,
                 out_abonent_type_, switch_id_, inbound_bunch_,
                 outbound_bunch_, term_cause_, phone_card_number_, in_info_,
                 dialed_digits_, out_info_, forwarding_identifier_,
                 border_switch_id_, message_, ss7_opc_, ss7_dpc_,
                 data_content_id_):
        self.telco_id = telco_id_
        self.begin_connection_time = begin_connection_time_
        self.duration = duration_
        self.call_type_id = call_type_id_
        self.supplement_service_id = supplement_service_id_
        self.in_abonent_type = in_abonent_type_
        self.out_abonent_type = out_abonent_type_
        self.switch_id = switch_id_
        self.inbound_bunch = inbound_bunch_
        self.outbound_bunch = outbound_bunch_
        self.term_cause = term_cause_
        self.phone_card_number = phone_card_number_
        self.in_info = in_info_
        self.dialed_digits = dialed_digits_
        self.out_info = out_info_
        self.forwarding_identifier = forwarding_identifier_
        self.border_switch_id = border_switch_id_
        self.message = message_
        self.ss7_opc = ss7_opc_
        self.ss7_dpc = ss7_dpc_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'telco_id', 'begin_connection_time', 'duration', 'call_type_id',
            'supplement_service_id', 'in_abonent_type', 'out_abonent_type',
            'switch_id', 'inbound_bunch', 'outbound_bunch', 'term_cause',
            'phone_card_number', 'in_info', 'dialed_digits', 'out_info',
            'forwarding_identifier', 'border_switch_id', 'message', 'ss7_opc',
            'ss7_dpc', 'data_content_id'
        ]


class MobileConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_MobileRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, MobileConnectionReportRecord.create
        )
        return MobileConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class MobileConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_MobileRecordContent):
        return MobileConnectionReportRecord(
            int(payload_['telco-id']),
            str(payload_['begin-connection-time']),
            int(payload_['duration']),
            int(payload_['call-type-id']),
            int(payload_['supplement-service-id']),
            int(payload_['in-abonent-type']),
            int(payload_['out-abonent-type']),
            str(payload_['switch-id']),
            int(payload_['term-cause']),
            tools.get_optional_value(
                payload_['inbound-bunch'], network.Bunch.create
            ),
            tools.get_optional_value(
                payload_['outbound-bunch'], network.Bunch.create
            ),
            tools.get_optional_value(
                payload_['in-info'], identifiers.create
            ),
            tools.get_optional_value(
                payload_['in-end-location'], locations.Location.create
            ),
            tools.get_optional_value(
                payload_['in-begin-location'], locations.Location.create
            ),
            tools.get_optional_value(
                payload_['out-info'], identifiers.create
            ),
            tools.get_optional_value(
                payload_['out-end-location'], locations.Location.create
            ),
            tools.get_optional_value(
                payload_['out-begin-location'], locations.Location.create
            ),
            tools.get_optional_str(payload_['forwarding-identifier']),
            tools.get_optional_int(payload_['roaming-partner-id']),
            tools.get_optional_str(payload_['border-switch-id']),
            tools.get_optional_str(payload_['message']),
            tools.get_optional_str(payload_['data-content-id'])
        )

    def __init__(self, telco_id_, begin_connection_time_, duration_,
                 call_type_id_, supplement_service_id_, in_subscriber_type_,
                 out_subscriber_type_, switch_id_, term_cause_,
                 inbound_bunch_, outbound_bunch_, in_info_, in_end_location_,
                 in_begin_location_, out_info_, out_begin_location_,
                 out_end_location_, forwarding_identifier_,
                 roaming_partner_id_, border_switch_id_, message_,
                 data_content_id_):
        self.telco_id = telco_id_
        self.begin_connection_time = begin_connection_time_
        self.duration = duration_
        self.call_type_id = call_type_id_
        self.supplement_service_id = supplement_service_id_
        self.in_subscriber_type = in_subscriber_type_
        self.out_subscriber_type = out_subscriber_type_
        self.switch_id = switch_id_
        self.term_cause = term_cause_
        self.inbound_bunch = inbound_bunch_
        self.outbound_bunch = outbound_bunch_
        self.in_info = in_info_
        self.in_end_location = in_end_location_
        self.in_begin_location = in_begin_location_
        self.out_info = out_info_
        self.out_begin_location = out_begin_location_
        self.out_end_location = out_end_location_
        self.forwarding_identifier = forwarding_identifier_
        self.roaming_partner_id = roaming_partner_id_
        self.border_switch_id = border_switch_id_
        self.message = message_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'telco_id', 'begin_connection_time', 'duration', 'call_type_id',
            'supplement_service_id', 'in_subscriber_type',
            'out_subscriber_type', 'switch_id', 'term_cause', 'inbound_bunch',
            'outbound_bunch', 'in_info', 'in_end_location',
            'in_begin_location', 'out_info', 'out_begin_location',
            'out_end_location', 'forwarding_identifier', 'roaming_partner_id',
            'border_switch_id', 'message', 'data_content_id'
        ]


class AAAConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(bytes(report_payload_), asn1.NRST_DataAAARecordData())
        records = tools.sequence_of_to_list(sequence_of, AAAConnectionReportRecord.create)
        return AAAConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']), records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class AAAConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataAAARecordContent):
        return AAAConnectionReportRecord(
            int(payload_['telco-id']),
            int(payload_['point-id']),
            str(payload_['aaa-connection-time']),
            int(payload_['aaa-login-type']),
            str(payload_['aaa-session-id']),
            network.IPAddress.create(payload_['aaa-allocated-ip']),
            str(payload_['aaa-user-name']),
            int(payload_['aaa-connect-type']),
            str(payload_['aaa-calling-number']),
            str(payload_['aaa-called-number']),
            network.NetworkPeerInfo.create(payload_['aaa-nas']),
            int(payload_['aaa-in-bytes-count']),
            int(payload_['aaa-out-bytes-count']),
            tools.get_optional_str(payload_['aaa-user-password']),
            tools.get_optional_value(
                payload_['aaa-user-equipment'],
                network.DataNetworkEquipment.create
            ),
            tools.get_optional_str(payload_['aaa-apn']),
            tools.get_optional_value(
                payload_['aaa-sgsn-ip'], network.IPAddress.create
            ),
            tools.get_optional_value(
                payload_['aaa-ggsn-ip'], network.IPAddress.create
            ),
            tools.get_optional_int(payload_['aaa-service-area-code']),
            tools.get_optional_value(
                payload_['aaa-location-start'], locations.Location.create
            ),
            tools.get_optional_value(
                payload_['aaa-location-end'], locations.Location.create
            ),
            tools.get_optional_str(payload_['phone-card-number']),
            tools.get_optional_str(payload_['aaa-imsi']),
            tools.get_optional_str(payload_['aaa-imei']),
            tools.get_optional_str(payload_['aaa-esn']),
            tools.get_optional_str(payload_['aaa-pool-number']),
            tools.get_optional_str(payload_['aaa-mcc']),
            tools.get_optional_str(payload_['aaa-mnc']),
            tools.get_optional_value(
                payload_['aaa-allocated-ip-mask'], network.IPMask.create
            )
        )

    def __init__(self, telco_id_, point_id_, connection_time_, login_type_,
                 session_id_, allocated_ip_, user_name_, connect_type_,
                 calling_number_, called_number_, nas_, in_bytes_count_,
                 out_bytes_count_, user_password_, user_equipment_, apn_,
                 sgsn_ip_, ggsn_ip_, service_area_code_, location_start_,
                 location_end_, phone_card_number_, imsi_, imei_, esn_,
                 pool_number_, mcc_, mnc_, allocated_ip_mask_):
        self.telco_id = telco_id_
        self.point_id = point_id_
        self.connection_time = connection_time_
        self.login_type = login_type_
        self.session_id = session_id_
        self.allocated_ip = allocated_ip_
        self.user_name = user_name_
        self.connect_type = connect_type_
        self.calling_number = calling_number_
        self.called_number = called_number_
        self.nas = nas_
        self.in_bytes_count = in_bytes_count_
        self.out_bytes_count = out_bytes_count_
        self.user_password = user_password_
        self.user_equipment = user_equipment_
        self.apn = apn_
        self.sgsn_ip = sgsn_ip_
        self.ggsn_ip = ggsn_ip_
        self.service_area_code = service_area_code_
        self.location_start = location_start_
        self.location_end = location_end_
        self.phone_card_number = phone_card_number_
        self.imsi = imsi_
        self.imei = imei_
        self.esn = esn_
        self.pool_number = pool_number_
        self.mcc = mcc_
        self.mnc = mnc_
        self.allocated_ip_mask = allocated_ip_mask_

    def __dir__(self):
        return [
            'telco_id', 'point_id', 'connection_time', 'login_type',
            'session_id', 'allocated_ip', 'user_name', 'connect_type',
            'calling_number', 'called_number', 'nas', 'in_bytes_count',
            'out_bytes_count', 'user_password', 'user_equipment', 'apn',
            'sgsn_ip', 'ggsn_ip', 'service_area_code', 'location_start',
            'location_end', 'phone_card_number', 'imsi', 'imei', 'esn',
            'pool_number', 'mcc', 'mnc', 'allocated_ip_mask'
        ]


class HTTPConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_DataResourceRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, HTTPConnectionReportRecord.create
        )
        return HTTPConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']), records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class HTTPConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataResourceRecordContent):
        return HTTPConnectionReportRecord(
            DataNetworkCdrHeader.create(payload_['res-cdr-header']),
            str(payload_['res-url']),
            int(payload_['res-bytes-count']),
            int(payload_['res-term-cause']),
            tools.get_optional_value(
                payload_['res-aaa-info'], IPAAAInformation.create
            ),
            tools.get_optional_int(payload_['res-http-method']),
            tools.get_optional_str(payload_['res-abonent-id']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['res-nat-info']),
                network.NetworkPeerInfo.create
            ),
            tools.get_optional_value(
                payload_['res-location'], locations.Location.create
            ),
            tools.get_optional_str(payload_['res-data-content-id'])
        )

    def __init__(self, cdr_header_, url_, bytes_count_, term_cause_, aaa_info_,
                 http_method_, subscriber_id_, nat_info_, location_,
                 data_content_id_):
        self.cdr_header = cdr_header_
        self.url = url_
        self.bytes_count = bytes_count_
        self.term_cause = term_cause_
        self.aaa_info = aaa_info_
        self.http_method = http_method_
        self.subscriber_id = subscriber_id_
        self.nat_info = nat_info_
        self.location = location_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'cdr_header', 'url', 'bytes_count', 'term_cause', 'aaa_info',
            'http_method', 'subscriber_id', 'nat_info', 'location',
            'data_content_id'
        ]


class EMailConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_DataEmailRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, create_email_connection_report_record
        )
        return EMailConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_,
            id_, request_id_, task_id_, total_blocks_,
            data_block_number_
        )
        self.records = records_


def create_email_connection_report_record(
        payload_: asn1.NRST_DataEmailRecordContent):
    component_name = payload_.getName()
    if component_name == 'mail-aaa':
        return EMailConnectionReportRecordAAA.create(payload_.getComponent())
    if component_name == 'mail-ipdr':
        return EMailConnectionReportRecordIPDR.create(payload_.getComponent())
    raise exceptions.GeneralFault(
        'unable to create EMail connection report record by ' +
        'the "{}" chosen component name'.format(component_name)
    )


class EMailConnectionReportRecordAAA(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataEmailRecordContentAAA):
        return EMailConnectionReportRecordAAA(
            DataNetworkCdrHeader.create(payload_['mail-cdr-header']),
            int(payload_['mail-event']),
            IPAAAInformation.create(payload_['mail-aaa-info']),
            tools.get_optional_str(payload_['mail-message']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['mail-nat-info']),
                network.NetworkPeerInfo.create
            ),
            tools.get_optional_value(
                payload_['mail-location'], locations.Location.create
            ),
            tools.get_optional_str(payload_['mail-data-content-id'])
        )

    def __init__(self, cdr_header_, event_, aaa_info_, message_, nat_info_,
                 location_, data_content_id_):
        self.cdr_header = cdr_header_
        self.event = event_
        self.aaa_info = aaa_info_
        self.message = message_
        self.nat_info = nat_info_
        self.location = location_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'cdr_header', 'event', 'aaa_info', 'message', 'nat_info',
            'location', 'data_content_id'
        ]


class EMailConnectionReportRecordIPDR(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataEmailRecordContentIPDR):
        return EMailConnectionReportRecordIPDR(
            DataNetworkCdrHeader.create(payload_['mail-cdr-header']),
            int(payload_['mail-event']),
            str(payload_['mail-sender']),
            tools.sequence_of_to_list(payload_['mail-receiver']['data'], str),
            tools.sequence_of_to_list(payload_['mail-cc']['data'], str),
            str(payload_['mail-subject']),
            int(payload_['mail-size']),
            int(payload_['attachements']),
            tools.sequence_of_to_list(payload_['mail-servers']['data'], str),
            int(payload_['mail-term-cause']),
            tools.get_optional_str(payload_['mail-reply-to']),
            tools.get_optional_int(payload_['mail-protocol']),
            tools.get_optional_str(payload_['mail-abonent-id']),
            tools.get_optional_str(payload_['mail-message']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['mail-nat-info']),
                network.NetworkPeerInfo.create
            ), tools.get_optional_value(
                payload_['mail-location'],
                locations.Location.create
            ),
            tools.get_optional_str(payload_['mail-data-content-id'])
        )

    def __init__(self, cdr_header_, event_, sender_, receiver_, cc_, subject_,
                 size_, attachments_, servers_, term_cause_, reply_to_,
                 protocol_, subscriber_id_, message_, nat_info_, location_,
                 data_content_id_):
        self.cdr_header = cdr_header_
        self.event = event_
        self.sender = sender_
        self.receiver = receiver_
        self.cc = cc_
        self.subject = subject_
        self.size = size_
        self.attachments = attachments_
        self.servers = servers_
        self.term_cause = term_cause_
        self.reply_to = reply_to_
        self.protocol = protocol_
        self.subscriber_id = subscriber_id_
        self.message = message_
        self.nat_info = nat_info_
        self.location = location_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'cdr_header', 'event', 'sender', 'receiver', 'cc', 'subject',
            'size', 'attachments', 'servers', 'term_cause', 'reply_to',
            'protocol', 'subscriber_id', 'message', 'nat_info', 'location',
            'data_content_id'
        ]


class IMConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_DataImRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, IMConnectionReportRecord.create
        )
        return IMConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class IMConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataImRecordContent):
        return IMConnectionReportRecord(
            DataNetworkCdrHeader.create(payload_['im-cdr-header']),
            str(payload_['im-user-login']),
            str(payload_['im-user-password']),
            str(payload_['im-sender-screen-name']),
            str(payload_['im-sender-uin']),
            tools.sequence_of_to_list(
                payload_['im-receivers'], IMReceiver.create
            ),
            int(payload_['im-size']),
            int(payload_['im-term-cause']),
            tools.get_optional_int(payload_['im-protocol']),
            tools.get_optional_str(payload_['im-abonent-id']),
            tools.get_optional_int(payload_['im-event']),
            tools.get_optional_str(payload_['im-message']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['im-nat-info']),
                network.NetworkPeerInfo.create
            ),
            tools.get_optional_value(
                payload_['im-location'], locations.Location.create
            ),
            tools.get_optional_str(payload_['im-data-content-id'])
        )

    def __init__(self, cdr_header_, user_login_, user_password_,
                 sender_screen_name_, sender_uin_, receivers_, size_,
                 term_cause_, protocol_, subscriber_id_, event_,
                 message_, nat_info_, location_, data_content_id_):
        self.cdr_header = cdr_header_
        self.user_login = user_login_
        self.user_password = user_password_
        self.sender_screen_name = sender_screen_name_
        self.sender_uin = sender_uin_
        self.receivers = receivers_
        self.size = size_
        self.term_cause = term_cause_
        self.protocol = protocol_
        self.subscriber_id = subscriber_id_
        self.event = event_
        self.message = message_
        self.nat_info = nat_info_
        self.location = location_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'cdr_header', 'user_login', 'user_password', 'sender_screen_name',
            'sender_uin', 'receivers', 'size', 'term_cause', 'protocol',
            'subscriber_id', 'event', 'message', 'nat_info', 'location',
            'data_content_id'
        ]


class IMReceiver(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_ImReceiver):
        return IMReceiver(
            str(payload_['im-receiver-screen-name']),
            str(payload_['im-receiver-uin'])
        )

    def __init__(self, screen_name_, uin_):
        self.screen_name = screen_name_
        self.uin = uin_

    def __dir__(self):
        return [
            'screen_name', 'uin'
        ]


class VOIPConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_DataVoipRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, VOIPConnectionReportRecord.create
        )
        return VOIPConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']), records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_,
            id_, request_id_, task_id_, total_blocks_,
            data_block_number_
        )
        self.records = records_


class VOIPConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataVoipRecordContent):
        return VOIPConnectionReportRecord(
            DataNetworkCdrHeader.create(payload_['voip-cdr-header']),
            str(payload_['voip-session-id']),
            str(payload_['voip-conference-id']),
            int(payload_['voip-duration']),
            str(payload_['voip-originator-name']),
            int(payload_['voip-call-type-id']),
            network.DataVoipNumber.create(payload_['voip-calling-number']),
            network.DataVoipNumber.create(payload_['voip-called-number']),
            int(payload_['voip-in-bytes-count']),
            int(payload_['voip-out-bytes-count']),
            bool(payload_['voip-fax']),
            int(payload_['voip-term-cause']),
            tools.get_optional_value(
                payload_['inbound-bunch'], network.Bunch.create
            ),
            tools.get_optional_value(
                payload_['outbound-bunch'], network.Bunch.create
            ),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['voip-gateways']),
                network.IPAddress.create
            ),
            tools.get_optional_int(payload_['voip-protocol']),
            tools.get_optional_int(payload_['supplement-service-id']),
            tools.get_optional_str(payload_['voip-abonent-id']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['voip-nat-info']),
                network.NetworkPeerInfo.create
            ),
            tools.get_optional_value(
                payload_['voip-location'], locations.Location.create
            ),
            tools.get_optional_int(payload_['voip-event']),
            tools.get_optional_str(payload_['voip-data-content-id'])
        )

    def __init__(self, cdr_header_, session_id_, conference_id_, duration_,
                 originator_name_, call_type_id_, calling_number_,
                 called_number_, in_bytes_count_, out_bytes_count_, fax_,
                 term_cause_, inbound_bunch_, outbound_bunch_, gateways_,
                 protocol_, supplement_service_id_, subscriber_id_, nat_info_,
                 location_, event_, data_content_id_):
        self.cdr_header = cdr_header_
        self.session_id = session_id_
        self.conference_id = conference_id_
        self.duration = duration_
        self.originator_name = originator_name_
        self.call_type_id = call_type_id_
        self.calling_number = calling_number_
        self.called_number = called_number_
        self.in_bytes_count = in_bytes_count_
        self.out_bytes_count = out_bytes_count_
        self.fax = fax_
        self.term_cause = term_cause_
        self.inbound_bunch = inbound_bunch_
        self.outbound_bunch = outbound_bunch_
        self.gateways = gateways_
        self.protocol = protocol_
        self.supplement_service_id = supplement_service_id_
        self.subscriber_id = subscriber_id_
        self.nat_info = nat_info_
        self.location = location_
        self.event = event_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'cdr_header', 'session_id', 'conference_id', 'duration',
            'originator_name', 'call_type_id', 'calling_number',
            'called_number', 'in_bytes_count', 'out_bytes_count', 'fax',
            'term_cause', 'inbound_bunch', 'outbound_bunch', 'gateways',
            'protocol', 'supplement_service_id', 'subscriber_id',
            'nat_info', 'location', 'event', 'data_content_id'
        ]


class FTPConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_DataFileTransferRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, FTPConnectionReportRecord.create
        )
        return FTPConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_,
            operator_name_, id_, request_id_, task_id_,
            total_blocks_, data_block_number_
        )
        self.records = records_


class FTPConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataFileTransferRecordContent):
        return FTPConnectionReportRecord(
            DataNetworkCdrHeader.create(payload_['file-cdr-header']),
            str(payload_['file-server-name']),
            str(payload_['file-user-name']),
            str(payload_['file-user-password']),
            tools.get_optional_bool(payload_['file-server-type']),
            int(payload_['file-in-bytes-count']),
            int(payload_['file-out-bytes-count']),
            int(payload_['file-term-cause']),
            tools.get_optional_str(payload_['file-abonent-id']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['file-nat-info']),
                network.NetworkPeerInfo.create
            ),
            tools.get_optional_value(
                payload_['file-location'],
                locations.Location.create
            ),
            tools.get_optional_str(payload_['file-data-content-id'])
        )

    def __init__(self, cdr_header_, server_name_, user_name_, user_password_,
                 server_type_, in_bytes_count_, out_bytes_count_, term_cause_,
                 subscriber_id_, nat_info_, location_, data_content_id_):
        self.cdr_header = cdr_header_
        self.server_name = server_name_
        self.user_name = user_name_
        self.user_password = user_password_
        self.server_type = server_type_
        self.in_bytes_count = in_bytes_count_
        self.out_bytes_count = out_bytes_count_
        self.term_cause = term_cause_
        self.subscriber_id = subscriber_id_
        self.nat_info = nat_info_
        self.location = location_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'cdr_header', 'server_name', 'user_name', 'user_password',
            'server_type', 'in_bytes_count', 'out_bytes_count', 'term_cause',
            'subscriber_id', 'nat_info', 'location', ' data_content_id'
        ]


class TerminalConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_DataTermAccessRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, TerminalConnectionReportRecord.create
        )
        return TerminalConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_,
                 data_block_number_, records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_,
            id_, request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class TerminalConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataTermAccessRecordContent):
        return TerminalConnectionReportRecord(
            DataNetworkCdrHeader.create(payload_['term-cdr-header']),
            int(payload_['term-in-bytes-count']),
            int(payload_['term-out-bytes-count']),
            tools.get_optional_int(payload_['term-protocol']),
            tools.get_optional_str(payload_['term-abonent-id']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['term-nat-info']),
                network.NetworkPeerInfo.create
            ),
            tools.get_optional_value(
                payload_['term-location'], locations.Location.create
            ),
            tools.get_optional_str(payload_['term-data-content-id'])
        )

    def __init__(self, cdr_header_, in_bytes_count_, out_bytes_count_,
                 protocol_, subscriber_id_, nat_info_, location_,
                 data_content_id_):
        self.cdr_header = cdr_header_
        self.in_bytes_count = in_bytes_count_
        self.out_bytes_count = out_bytes_count_
        self.protocol = protocol_
        self.subscriber_id = subscriber_id_
        self.nat_info = nat_info_
        self.location = location_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'cdr_header', 'in_bytes_count', 'out_bytes_count', 'protocol',
            'subscriber_id', 'nat_info', 'location', 'data_content_id'
        ]


class RawFlowsConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_), asn1.NRST_DataRawFlowsRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, RawFlowsConnectionReportRecord.create
        )
        return RawFlowsConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_,
                 records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_,
            request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class RawFlowsConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataRawFlowsRecordContent):
        return RawFlowsConnectionReportRecord(
            DataNetworkCdrHeader.create(payload_['flow-cdr-header']),
            int(payload_['flow-in-bytes-count']),
            int(payload_['flow-out-bytes-count']),
            tools.get_optional_int(payload_['flow-protocol']),
            tools.get_optional_str(payload_['flow-abonent-id']),
            tools.sequence_of_to_list(
                tools.get_optional_value(payload_['flow-nat-info']),
                network.NetworkPeerInfo.create
            ),
            tools.get_optional_value(
                payload_['flow-location'], locations.Location.create
            ),
            tools.get_optional_str(payload_['flow-data-content-id'])
        )

    def __init__(self, cdr_header_, in_bytes_count_, out_bytes_count_,
                 protocol_, subscriber_id_, nat_info_, location_,
                 data_content_id_):
        self.cdr_header = cdr_header_
        self.in_bytes_count = in_bytes_count_
        self.out_bytes_count = out_bytes_count_
        self.protocol = protocol_
        self.subscriber_id = subscriber_id_
        self.nat_info = nat_info_
        self.location = location_
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
            'cdr_header', 'in_bytes_count', 'out_bytes_count', 'protocol',
            'subscriber_id', 'nat_info', 'location', 'data_content_id'
        ]


class NATConnectionReport(report.BaseReport):

    @staticmethod
    def create(raw_message_, message_payload_, report_payload_):
        sequence_of, rest = ber_decode(
            bytes(report_payload_),
            asn1.NRST_DataAddressTranslationRecordData()
        )
        records = tools.sequence_of_to_list(
            sequence_of, NATConnectionReportRecord.create
        )
        return NATConnectionReport(
            raw_message_['version'],
            raw_message_['message-id'],
            raw_message_['message-time'],
            tools.get_optional_str(raw_message_['operator-name']),
            raw_message_['id'],
            int(message_payload_['request-id']),
            int(message_payload_['task-id']),
            int(message_payload_['total-blocks-number']),
            int(message_payload_['block-number']),
            records
        )

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_, data_block_number_, records_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_,
            id_, request_id_, task_id_, total_blocks_, data_block_number_
        )
        self.records = records_


class NATConnectionReportRecord(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataAddressTranslationRecordContent):
        return NATConnectionReportRecord(
            int(payload_['telco-id']),
            int(payload_['point-id']),
            int(payload_['translation-type']),
            str(payload_['translation-time']),
            int(payload_['record-type']),
            network.NetworkPeerInfo.create(payload_['private-ip']),
            network.NetworkPeerInfo.create(payload_['public-ip']),
            network.NetworkPeerInfo.create(payload_['destination-ip'])
        )

    def __init__(self, telco_id_, point_id_, translation_type_,
                 translation_time_, record_type_, private_ip_, public_ip_,
                 destination_ip_):
        self.telco_id = telco_id_
        self.point_id = point_id_
        self.translation_type = translation_type_
        self.translation_time = translation_time_
        self.record_type = record_type_
        self.private_ip = private_ip_
        self.public_ip = public_ip_
        self.destination_ip = destination_ip_

    def __dir__(self):
        return [
            'telco_id', 'point_id', 'translation_type', 'translation_time',
            'record_type', 'private_ip', 'public_ip', 'destination_ip'
        ]


class DataNetworkCdrHeader(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_DataNetworkCdrHeader):
        if payload_['id'] != asn1.sorm_report_connection_ipdr_header:
            raise exceptions.GeneralFault(
                'unable to create "{0}", invalid OID - {1}'.format(
                    DataNetworkCdrHeader.__name__, str(payload_['id'])
                )
            )
        data = payload_['data']
        return DataNetworkCdrHeader(
            int(data['telco-id']),
            str(data['begin-connection-time']),
            str(data['end-connection-time']),
            network.NetworkPeerInfo.create(data['client-info']),
            network.NetworkPeerInfo.create(data['server-info']),
            int(data['protocol-code']),
            tools.get_optional_int(data['point-id'])
        )

    def __init__(self, telco_id_, begin_connection_time_, end_connection_time_,
                 client_info_, server_info_, protocol_code_, point_id_):
        self.telco_id = telco_id_
        self.begin_connection_time = begin_connection_time_
        self.end_connection_time = end_connection_time_
        self.client_info = client_info_
        self.server_info = server_info_
        self.protocol_code = protocol_code_
        self.point_id = point_id_

    def __dir__(self):
        return [
            'telco_id', 'begin_connection_time', 'end_connection_time',
            'client_info', 'server_info', 'protocol_code', 'point_id'
        ]


class IPAAAInformation(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_IP_AAAInformation):
        return IPAAAInformation(
            str(payload_['username']),
            tools.get_optional_int(payload_['aaaResult'])
        )

    def __init__(self, user_name_, result_):
        self.user_name = user_name_
        self.result = result_

    def __dir__(self):
        return [
            'user_name', 'result'
        ]


def create(raw_message_, payload_):
    component = payload_['report-block']['connections']
    oid = component['id']
    creator = report_creators.get(oid, None)
    if creator is None or not callable(creator):
        raise exceptions.GeneralFault(
            f'unable to create connection report data block' +
            f' by the "{str(oid)}" OID'
        )
    return creator(raw_message_, payload_, component['data'])


report_creators = {
    asn1.sorm_report_connection_pstn: PSTNConnectionReport.create,
    asn1.sorm_report_connection_mobile: MobileConnectionReport.create,
    asn1.sorm_report_connection_aaa_login: AAAConnectionReport.create,
    asn1.sorm_report_connection_resource: HTTPConnectionReport.create,
    asn1.sorm_report_connection_email: EMailConnectionReport.create,
    asn1.sorm_report_connection_im: IMConnectionReport.create,
    asn1.sorm_report_connection_voip: VOIPConnectionReport.create,
    asn1.sorm_report_connection_file_transfer: FTPConnectionReport.create,
    asn1.sorm_report_connection_term_access: TerminalConnectionReport.create,
    asn1.sorm_report_connection_raw_flows: RawFlowsConnectionReport.create,
    asn1.sorm_report_connection_address_translations: NATConnectionReport.create
}
