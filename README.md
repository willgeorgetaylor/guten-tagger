# Guten Tagger
## Introduction ##
Guten Tagger is a simple 'error tagger' for German language exercises.

Error tagging is the process of identifying, classifying and representing types of linguistic 'errors', or non-standard features, in natural and (often) non-natively authored texts. Guten Tagger is designed to tag errors in very short (1-20 words) written inputs by learners of the German language, by applying a 'generative' approach to the task. Thanks to the prescribed set of acceptable inputs in most online exercises, Guten Tagger successfully demonstrates that an exhaustive set of incorrect inputs can be found for each, and tagged with its grammatical properties.

## How it works ##
For each question, Guten Tagger needs two pieces of data from you (as the course developer):

* The question as phrased to the learner (e.g., 'Wie _____ von hier zur Schule?')
* The correct answer (e.g., 'komme ich')

To facilitate testing of Guten Tagger, an additional input of the entire english translation to show the tester as a prompt. This is not used at any stage.

## The results ##
The result of processing is a list of incorrect substitutions for each token/word in the input, each with its own grammatical annotations.

These can be used as error identifiers during the validation process for exercises. A basic implementation of this could be a substring/containment check for each error identifier in the user's input.

## Demo ##
Live demo coming soon!

## Notes ##
* At present, the correct answer is marked up with grammatical features at design time. However, this will soon be made automatic as part of the pipeline, making use of the Stanford PoS tagger (https://nlp.stanford.edu/software/tagger.shtml).