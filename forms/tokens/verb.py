from grammar.mood import Mood
from grammar.tense import Tense
from forms.tokens.token import Token
from forms.markers.markerposition import MarkerPosition


class Verb(Token):

    def __init__(self, verb, language, stem, person, number):
        super(Verb, self).__init__(verb, language)
        self._stem = stem
        self._person = person
        self._number = number

    def conjugate(self, verb_marker):
        conjugated_form = (verb_marker.form + self.stem)
        if verb_marker.position == MarkerPosition.suffix:
            conjugated_form = (self.stem + verb_marker.form)

        return Verb(conjugated_form, self.language, self.stem, verb_marker.person, verb_marker.number)

    def generate_flags(self):
        # Just flagging erroneous conjugations in the present indicative for now
        all_verb_markers = self.language.get_verb_markers(Tense.Present, Mood.Indicative)

        # Remove the marker representing the correct verb
        incorrect_verb_markers = [m for m in all_verb_markers
                                  if not (m.person.value == self.person.value and m.number.value == self.number.value)]

        # Conjugate
        return self.wrap_flags(list(map(self.conjugate, incorrect_verb_markers)))


    @property
    def stem(self):
        return self._stem

    @property
    def person(self):
        return self._person

    @property
    def number(self):
        return self._number
