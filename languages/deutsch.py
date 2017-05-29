from grammar.mood import Mood
from grammar.tense import Tense
from grammar.gender import Gender

from forms.markers.markerposition import MarkerPosition
from languages.language import Language


class Deutsch(Language):

    def __init__(self):
        super(Deutsch, self).__init__("Deutsch", "de-DE")

    def get_verb_markers(self, tense, mood):
        # Only handle the present indicative for now
        if tense == Tense.Present and mood == Mood.Indicative:
            return self.create_verb_paradigm(["e", "st", "t", "en", "t", "en"], MarkerPosition.suffix)

    def get_pronouns(self):
        return self.create_pronoun_paradigm(["ich",
                                             "du",
                                             {Gender.Masculine: "er", Gender.Feminine: "sie", Gender.Neuter: "es"},
                                             "wir",
                                             "ihr",
                                             "sie"], self)
