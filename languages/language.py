from abc import abstractmethod, ABCMeta
from forms.markers.verbmarker import VerbMarker
from forms.tokens.pronoun import Pronoun
from grammar.number import Number
from grammar.person import Person
from grammar.gender import Gender


class Language(object):

    __metaclass__ = ABCMeta

    def __init__(self, locale, lcid):
        self._locale = locale
        self._lcid = lcid

    @abstractmethod
    def get_verb_markers(self, tense, mood):
        pass

    @abstractmethod
    def get_pronouns(self):
        pass

    @property
    def locale(self):
        return self._locale

    @property
    def lcid(self):
        return self._lcid

    @staticmethod
    def create_verb_paradigm(markers, position):
        index = 0
        paradigm = []

        for number in Number:
            for person in Person:
                if index < len(markers):
                    paradigm.append(VerbMarker(markers[index], position, number, person))
                    index += 1
        return paradigm

    @staticmethod
    def create_pronoun_paradigm(forms, language):
        index = 0
        paradigm = []

        for number in Number:
            for person in Person:
                if index < len(forms):

                    form = forms[index]

                    if isinstance(form, str):
                        paradigm.append(Pronoun(form, language, person, number, Gender.Unexpressed))
                    elif isinstance(form, dict):
                        for key, value in form.items():
                            paradigm.append(Pronoun(value, language, person, number, key))
                    else:
                        paradigm.append()

                    index += 1
        return paradigm