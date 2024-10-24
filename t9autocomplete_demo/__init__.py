from pathlib import Path
from random import choices

class T9AutoComplete:

    mapping = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    def __init__(self):
        self.registery: dict[str, dict] = {}


    def get_t9_combinations(self, t9: str) -> list[str]:
        if not t9:
            return []
        combinations = []
        for digit in t9:
            mapping = self.mapping.get(int(digit))
            if not mapping:
                continue
            if not combinations:
                combinations = list(mapping)
            else:
                new_combinations = []
                for letter in mapping:
                    for combination in combinations:
                        new_combinations.append(combination + letter)
                combinations = new_combinations
        return combinations

    def initiate_from_file(self, file_path: Path) -> 'T9AutoComplete':
        with file_path.open() as file:
            for line in file:
                self.register(line.strip())

    def register(self, word: str):
        if not word:
            return
        registery = self.registery
        for letter in word:
            if letter not in registery:
                registery[letter] = {}
            registery = registery[letter]
        registery["is_word"] = True

    def find_words_by_phrase(self, phrase: str) -> list[str]:
        found_words = []
        registery = self.registery
        for letter in phrase:
            if letter not in registery:
                return found_words
            registery = registery[letter]
        for key in registery:
            if key == "is_word":
                found_words.append(phrase)
                continue
            found_words.extend(self.find_words_by_phrase(phrase + key))
        return found_words
        

    def suggest(self, t9: str, number_of_suggestions: int = 5) -> list[str]:
        phrases = self.get_t9_combinations(t9)
        suggestions = []
        for phrase in phrases:
            words = self.find_words_by_phrase(phrase)
            suggestions.extend(words)
        if len(suggestions) <= number_of_suggestions:
            return suggestions
        return choices(suggestions, k=number_of_suggestions)
