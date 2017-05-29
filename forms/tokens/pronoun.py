from forms.tokens.token import Token


class Pronoun(Token):

    def __init__(self, noun, language, person, number, gender):
        super(Pronoun, self).__init__(noun, language)
        self._person = person
        self._number = number
        self._gender = gender

    def generate_flags(self):
        all_pronouns = self.language.get_pronouns()

        incorrect_pronouns = [p for p in all_pronouns
                              if not (p.person.value == self.person.value and p.number.value == self.number.value)]

        return self.wrap_flags(incorrect_pronouns)

    @property
    def person(self):
        return self._person

    @property
    def number(self):
        return self._number

    @property
    def gender(self):
        return self._gender
