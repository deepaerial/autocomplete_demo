from pathlib import Path
from t9autocomplete_demo import T9AutoComplete
import pytest

TESTS_PATH = Path(__file__).parent

TEST_WORDS_FILE = TESTS_PATH / "test_words.txt"

@pytest.fixture()
def t9autocomplete():
    return T9AutoComplete()

def test_letters_combination(t9autocomplete: T9AutoComplete):
    t9autocomplete = T9AutoComplete()
    combinations = t9autocomplete.get_t9_combinations("23")
    assert set(combinations) == set(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

def test_suggest(t9autocomplete: T9AutoComplete):
    t9autocomplete.initiate_from_file(TEST_WORDS_FILE)
    suggestions = t9autocomplete.suggest("23")
    expected_suggestions = set(["adactyl", "adactylia", "aeacides", "aeacides", "aeacus", "afaint"])
    assert suggestions is not None and len(suggestions) == 5
    assert set(suggestions) <= expected_suggestions