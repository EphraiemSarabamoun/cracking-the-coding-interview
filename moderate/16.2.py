from collections import Counter

class WordFreq:
    def __init__(self, book: str):
        words = book.lower().split()  # Simple split, adjust for punctuation
        self.freq = Counter(words)

    def get_freq(self, word: str) -> int:
        return self.freq.get(word.lower(), 0)