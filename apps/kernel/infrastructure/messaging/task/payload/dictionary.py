from pyasn1.type import tag
from pyasn1.type import useful

from apps.kernel.infrastructure.messaging import base
from apps.system.lib import asn1


class DictionaryTask(base.ASN1Constructable):

    def __init__(self, data):
        self.id = asn1.sorm_request_dictionaries

        if isinstance(data, useful.ObjectDescriptor):
            self.data = data
        else:
            self.data = useful.ObjectDescriptor(data)

    def __dir__(self):
        return ['id', 'data']

    def to_asn1(self):
        task = asn1.SkrDictionaryTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
                )
            )
        )
        task['id'] = self.id
        task['data'] = self.data
        return task
