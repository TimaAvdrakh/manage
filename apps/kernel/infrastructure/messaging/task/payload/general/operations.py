from apps.system.lib import basic


class LogicalOperation(basic.PrintableObject):

    def __init__(self, code_, name_):
        self.code = code_
        self.name = name_

    def __dir__(self):
        return ['name']


OPEN_BRACKET = LogicalOperation(0, 'open-bracket')
CLOSE_BRACKET = LogicalOperation(1, 'close-bracket')
OR = LogicalOperation(2, 'or')
AND = LogicalOperation(3, 'and')
NOT = LogicalOperation(4, 'not')
