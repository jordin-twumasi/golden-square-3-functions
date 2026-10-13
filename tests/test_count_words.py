from lib.count_words import *
import pytest

#Simplest test - empty string returns 0
def test_empty_string_returns_zero():
    assert count_words("") == 0

#Given 4 words return 4
def test_four_words_returns_four():
    assert count_words("Once upon a time") == 4

#Given invalid data type
def test_given_inavlid_type_raise_error():
    with pytest.raises(Exception) as err:
        count_words(8)
    message = str(err.value)
    assert message == "Must input a string"