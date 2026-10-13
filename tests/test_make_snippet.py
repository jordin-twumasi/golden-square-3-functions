from lib.make_snippet import *
import pytest 

#Simplest test case - returning an empty string if given one
def test_given_empty_return_empty():
    assert make_snippet("") == ""

#Return string of five words
def test_given_five_words():
    assert make_snippet("There was a young girl.") == "There was a young girl."

#Given string of 6 return first 5 and a ...
def test_given_6_words_returns_5_and_ellipses():
    assert make_snippet("Once upon a time there was a young girl.") == "Once upon a time there..."

#Given an invalid data type
def test_return_error_for_invalid_type():
    with pytest.raises(Exception) as err:
        make_snippet(8) 
    message = str(err.value)
    assert message == "Must input a string"