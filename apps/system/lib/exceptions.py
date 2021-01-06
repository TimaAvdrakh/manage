class GeneralFault(Exception):

    def __init__(self, message_):
        super().__init__(message_)
