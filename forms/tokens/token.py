from abc import abstractmethod, ABCMeta


class Token(object):

    metaclass__ = ABCMeta

    def __init__(self, form, language):
        self._form = form
        self._language = language

    @abstractmethod
    def generate_flags(self):
        pass

    @abstractmethod
    def generate_flags(self):
        pass

    def wrap_flags(self, flags):
        return self, flags

    def __repr__(self):
        return self.form

    @property
    def form(self):
        return self._form

    @property
    def language(self):
        return self._language

