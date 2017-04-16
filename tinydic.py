# coding: utf-8
"""
TinyDIC
-------

Tiny Python Dependency Injection Container
"""


class Container(object):
    """Dependency Container class"""

    def __init__(self):
        self.__dict__['_values'] = {}

    def register(self, key, value, constant=False):
        """Registers a new value into the Dependency Injection Container.
        :param key: The key used to resolve the value after registration
        :param value: The value to be registered. Usually a function/lambda that takes the container
        as it's unique parameter and returns a new object.
        :param constant: flag indicating if the value should be registered as a constant or not.
        If `False` then value must a `callable` which will be called with the container as unique
        parameter when resolving the key.
        """
        if constant:
            self._values[key] = lambda c: value
        else:
            self._values[key] = value

    def __setattr__(self, key, value):
        """Registers a new value
        :param key: The key used to resolve the value after registration
        :param value: The value to be registered. Usually a function/lambda that takes the container
        as it's unique parameter and returns a new object.
        If value is `callable`, then registration will be done as variable, otherwise will be as
        constant.
        """
        if callable(value):
            return self.register(key, value, False)

        self.register(key, value, True)

    def __getattr__(self, key):
        """
        Resolves and returns the value associated with the given key
        :param key: the key which identifies the value that we want to resolve
        :return: The resolved value associated with the key
        :raises AttributeError: if there's no value associated with the given key yet.
        """
        if key not in self._values:
            raise AttributeError("'{}' is not registered.".format(key))

        return self._values[key](self)
