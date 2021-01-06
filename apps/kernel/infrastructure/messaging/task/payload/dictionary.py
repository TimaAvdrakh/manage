from pyasn1.type import tag
from pyasn1.type import useful

from apps.kernel.infrastructure.messaging import base
from apps.system.lib import asn1


class DictionaryTask(base.ASN1Constructable):

    def __init__(self, data_):
        self.id = asn1.sorm_request_dictionaries

        if isinstance(data_, useful.ObjectDescriptor):
            self.data = data_
        else:
            self.data = useful.ObjectDescriptor(data_)

    def __dir__(self):
        return ['id', 'data']

    def to_asn1(self):
        task = asn1.NRST_DictionaryTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
                )
            )
        )
        task['id'] = self.id
        task['data'] = self.data
        return task
