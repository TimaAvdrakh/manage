import argparse


class ArgumentParsingError(Exception):

    def __init__(self, message_):
        super().__init__(message_)


class ThrowableArgumentParser(argparse.ArgumentParser):

    def error(self, message_):
        raise ArgumentParsingError(message_)


class Option:

    def __init__(self, short_, long_):
        self.short = short_
        self.long = long_

    def combined_string(self):
        if self.short is not None:
            if self.long is not None:
                return '/'.join((self.short, self.long))
        if self.short is not None:
            return self.short
        else:
            if self.long is not None:
                return self.long
            return
