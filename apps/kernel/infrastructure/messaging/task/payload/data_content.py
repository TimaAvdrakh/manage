from pyasn1.type import tag

from apps.kernel.infrastructure.messaging import base
from apps.system.lib import asn1


class DataContentTask(base.ASN1Constructable):

    def __init__(self, data_content_id_):
        self.data_content_id = data_content_id_

    def __dir__(self):
        return [
         'data_content_id']

    def to_asn1(self):
        return asn1.SkrDataContentTask(
            (self.data_content_id),
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9)
                )
            )
        )
