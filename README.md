# Word-Predictor (Python Project)

Overview
This Python project is a simple spell checker that reads a text file and builds a vocabulary from its contents. When given an input word that is not in the vocabulary, the program suggests the word from the vocabulary that is most likely the correct one, along with a probability score.

How it Works
Reading a Text File: The program starts by reading a text file provided by the user. This text file should contain a list of words to build the program's vocabulary.

Building the Vocabulary: The program analyzes the text file, tokenizes it into words, and creates a vocabulary from these words. It keeps track of the frequency of each word in the text, which helps determine the probability of a word being correct.

Input Word Check: When the user provides an input word, the program checks if it exists in the vocabulary. If the word is present, no suggestions are provided as it is considered correct.

Finding Suggestions: If the input word is not in the vocabulary, the program looks for similar words within the vocabulary. It calculates the probability of each word being the correct suggestion based on factors like edit distance (how similar the word is in terms of character edits) and word frequency in the vocabulary.

Displaying Suggestions: The program presents the user with the word from the vocabulary that has the highest probability of being the correct replacement for the input word. It also displays the calculated probability score.
