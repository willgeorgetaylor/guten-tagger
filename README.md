# Guten Tagger
## Introduction ##
Guten Tagger is a rapidly prototyped proof on concept, that predicts the forms (and grammatical rationale) of a set of erroneous responses, given a question and correct answer.

It demonstrates that with short, gap-fill exercises (here, in German), this approach provides a fast, predictable and scaleable way of providing learner feedback.

## How it works ##

```python
>>>de = Deutsch()
>>>answer = [verb.Verb("komme", de, "komm", person.Person.First, number.Number.Singular),
          pronoun.Pronoun("ich", de, person.Person.First, number.Number.Singular, gender.Gender.Unexpressed)]
>>>question = Question("Wie _ von hier zur Schule?", "How do I get to school?", answer)
>>>print(question.flags)
```

The results:
```python
[
(komme, [kommst, kommt, kommen, kommt, kommen]), # answer : [ errors... ]
(ich, [du, er, sie, es, wir, ihr, sie])			 # answer : [ errors... ]
]
```

## The results ##
The result is a list of possible incorrect answers for each token in the correct answer, each with its own grammatical annotations.

In a production system, the erroneous responses can be anticipated and could even be linked to helpful feedback, using the grammatical annotations to determine the type of L1 interference. In multi-word gaps, such as the example above (`komme ich`), it should be possible to anticipate composite responses (and possible overlapping error types) from the product of each token slot, using `itertools.product`.

## Notes ##
* This is only for demonstration purposes, and not intended to be used. For use in a production language-learning system, there are several areas to develop. For example, you would want to annotate linguistic features automatically, instead of manually.