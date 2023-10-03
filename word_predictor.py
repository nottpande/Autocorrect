import re
import string
from collections import Counter

class SpellCheck:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            words = []
            for line in lines:
                words += re.findall(r'\w+', line.lower())

        self.vocab = set(words)
        self.word_count = Counter(words)
        total_words = float(sum(self.word_count.values()))
        self.word_probability = {word: self.word_count[word] / total_words for word in self.vocab}

    def one_edit_distances(self, word):
        letters = string.ascii_lowercase
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [l + r[1:] for l, r in splits if r]
        swaps = [l + r[0] + r[1] + r[2:] for l, r in splits if len(r) > 1]
        replaces = [l + c + r[1:] for l, r in splits if r for c in letters]
        inserts = [l + c + r for l, r in splits for c in letters]

        return set(deletes + swaps + replaces + inserts)

    def two_edit_distances(self, word):
        return set(e2 for e1 in self.one_edit_distances(word) for e2 in self.one_edit_distances(e1))

    def check(self, word):
        candidates = self.one_edit_distances(word) or self.two_edit_distances(word) or [word]
        valid_candidates = [w for w in candidates if w in self.vocab]

        return sorted([(c, self.word_probability[c]) for c in valid_candidates], key=lambda tup: tup[1], reverse=True)

def read_text(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        words = []

        for line in lines:
            words += re.findall(r'\w+', line.lower())

    return words

words = read_text('./SAMPLE.txt')
vocab = set(words)
word_count = Counter(words)
total_words = float(sum(word_count.values()))
word_probability = {word: word_count[word] / total_words for word in word_count.keys()}

print("Enter the misspelled word:")
misspelled_word = input()
checker = SpellCheck("./SAMPLE.txt")

print("The possible word(s) are:")
print(checker.check(misspelled_word))