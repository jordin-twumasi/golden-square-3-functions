from lib.verify_grammar import *

#Return true if capital and appropriate punctuation
def test_given_capital_and_punctuation_return_true():
    result = verify_grammar('Hello, what is your name?')
    assert result == True

#Return false if no capital but ends with coorect punctuation
def test_given_no_capital_and_punctuation_return_false():
    result = verify_grammar('hello, my name is Jo.')
    assert result == False