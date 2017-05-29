class Question(object):

    def __init__(self, question, translation, answer):
        self._question = question
        self._translation = translation
        self._answer = answer
        self._flags = []
        for token in answer:
            generated_flags = token.generate_flags()
            if generated_flags:
                self.flags.append(generated_flags)

    @property
    def question(self):
        return self._question

    @property
    def translation(self):
        return self._translation

    @property
    def answer(self):
        return self._answer

    @property
    def flags(self):
        return self._flags