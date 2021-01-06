from . import base
from . import tools


class FindRange(base.ASN1Copyable):

    def __init__(self, begin_find_, end_find_):
        self.begin_find = tools.to_date_and_time(begin_find_)
        self.end_find = tools.to_date_and_time(end_find_)

    def __dir__(self):
        return [
         'begin_find', 'end_find']

    def copy_to(self, target_):
        if self.begin_find is not None:
            target_['begin-find'] = self.begin_find
        if self.end_find is not None:
            target_['end-find'] = self.end_find
