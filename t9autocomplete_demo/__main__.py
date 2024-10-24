from . import T9AutoComplete
from pathlib import Path
import sys

WORDS_FILE = (Path(__file__).parent / ".." / "words.txt").resolve().absolute()

if __name__ == "__main__":
    t9autocomplete = T9AutoComplete()
    t9autocomplete.initiate_from_file(WORDS_FILE)
    try:
        while True:
            t9 = input("Enter T9: ")
            if not t9.isdigit():
                print("T9 must be a number")
                continue
            suggestions = t9autocomplete.suggest(t9)
            print(suggestions)
    except KeyboardInterrupt:
        sys.exit(0)

