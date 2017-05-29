from abc import ABCMeta, abstractmethod


class Marker(object):

    __metaclass__ = ABCMeta

    def __init__(self, form, position):
        self.form = form
        self.position = position