# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = "".join(sorted(self.word))

    def match(self, word_list):
        return [word for word in word_list if "".join(sorted(word.lower())) == self.sorted_word]
    