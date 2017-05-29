from forms.tokens.token import Token


class Noun(Token):

    def __init__(self, noun, language, number):
        super(Noun, self).__init__(noun, language)
        self._number = number

    def generate_flags(self):
        return self.wrap_flags([])

    def number(self):
        return self._number
