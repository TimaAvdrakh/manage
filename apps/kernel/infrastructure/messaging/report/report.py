from pyasn1 import error
from pyasn1.type import tag
from pyasn1.codec.der.encoder import encode as der_encode

from apps.kernel.infrastructure.messaging import base
from apps.system.lib import (
    exceptions,
    logger,
    asn1,
)


class Acknowledgement(base.OutgoingMessage):

    def __init__(self, message_id_, successful_, broken_record_,
                 error_description_):
        super().__init__(message_id_, asn1.sorm_message_report)
        self.successful = successful_
        self.broken_record = broken_record_
        self.error_description = error_description_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend(['successful', 'broken_record', 'error_description'])
        return fields

    def encode_data(self):
        ack = asn1.SkrAcknowledgement(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
                )
            )
        )
        ack.setComponentByName('successful', self.successful)
        if self.broken_record is not None:
            ack.setComponentByName('broken-record', self.broken_record)
        if self.error_description is not None:
            ack.setComponentByName('error-description', self.error_description)
        return der_encode(ack)


class BaseReport(base.IncomingMessage):

    def __init__(self, version_, message_id_, message_time_, operator_name_,
                 id_, request_id_, task_id_, total_blocks_,
                 data_block_number_):
        super().__init__(
            version_, message_id_, message_time_, operator_name_, id_
        )
        self.request_id = request_id_
        self.task_id = task_id_
        self.total_blocks = total_blocks_
        self.data_block_number = data_block_number_

    def __dir__(self):
        fields = super().__dir__()
        fields.extend([
            'request_id', 'task_id', 'total_blocks', 'data_block_number'
        ])
        return fields


def create(raw_message_, payload_):
    name = payload_['report-block'].getName()
    creator = report_creators.get(name, None)
    if creator is None or not callable(creator):
        raise exceptions.GeneralFault(
            f'unable to chose report data block by "{name}" name'
        )
    try:
        return creator(raw_message_, payload_)
    except error.PyAsn1Error:
        if isinstance(payload_, asn1.SkrReport):
            task_id = int(payload_.getComponentByName('task-id'))
            block_number = int(payload_.getComponentByName('block-number'))
            logger.instance().error(
                f'Unable to parse ASN.1 data of report ' +
                f'block #{block_number} of the task #{task_id}'
            )
        raise


from .payload import connection
from .payload import data_content
from .payload import dictionary
from .payload import location
from .payload import non_formalized
from .payload import payment
from .payload import presence
from .payload import subscriber

report_creators = {
    'dictionary': dictionary.create,
    'abonents': subscriber.create,
    'connections': connection.create,
    'locations': location.create,
    'payments': payment.create,
    'presense': presence.create,
    'nonFormalized': non_formalized.create,
    'data-content': data_content.create
}
