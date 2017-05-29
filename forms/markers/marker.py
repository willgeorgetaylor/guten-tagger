from abc import ABCMeta, abstractmethod


class Marker(object):

    __metaclass__ = ABCMeta

    def __init__(self, form, position):
        self._form = form
        self._position = position

    @property
    def form(self):
        return self._form

    @property
    def position(self):
        return self._position
