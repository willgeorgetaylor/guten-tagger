from forms.tokens import pronoun, verb
from languages.deutsch import Deutsch
from grammar import person, number, gender
from question import Question

de = Deutsch()

answer = [verb.Verb("komme", de, "komm", person.Person.First, number.Number.Singular),
          pronoun.Pronoun("ich", de, person.Person.First, number.Number.Singular, gender.Gender.Unexpressed)]

q = Question("Wie _ von hier zur Schule?", "How do I get to school?", answer)

print(q.flags)