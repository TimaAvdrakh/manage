class PrintableObject:

    def __dir__(self):
        return []

    def __repr__(self):
        return '{0}({1})'.format(
            self.__class__.__name__,
            ', '.join([
                '{0}: "{1}"'.format(field, self.__dict__[field]) for field in self.__dir__() if self.__dict__[field] is not None
            ])
        )
