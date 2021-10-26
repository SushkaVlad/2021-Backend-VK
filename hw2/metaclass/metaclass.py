class CustomMeta(type):
    """CustomMeta is metaclass which adds prefix
    to all fields and methods of the produced class
    (except magic)"""

    prefix = 'custom_'

    def __new__(cls, name, bases, attrs):
        """rules of creation instance of class CustomMeta"""
        custom_attrs = {}
        for key, val in attrs.items():
            custom_attrs[CustomMeta.prefix + key if not (key.startswith('__') and key.endswith('__')) else key] = val

        def custom_setattr(self, key, value):
            self.__dict__[CustomMeta.prefix + key if not (key.startswith('__') and key.endswith('__')) else key] = value

        custom_attrs['__setattr__'] = custom_setattr

        return super().__new__(cls, name, bases, custom_attrs)


class CustomClass(metaclass=CustomMeta):
    """Class using metaclass CustomMeta"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100
