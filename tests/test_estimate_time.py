from lib.estimate_time import *
import pytest


# return time 1 for 200 words
def test_given_200_estimate_time_1():
    text = " ".join(["word" for i in range(200)])
    assert estimate_time(text) == 1.0

#return time 2 for 400 words
def test_given_400_estimate_time_2():
    text = " ".join(["word" for i in range(400)])
    assert estimate_time(text) == 2.0

#return time 1.5 for 300 words
def test_given_300_estimate_time_1_and_half():
    text = " ".join(["word" for i in range(300)])
    assert estimate_time(text) == 1.5


#return error for empty text
def test_given_empty_text():
    text = ""
    with pytest.raises(Exception) as err:
        estimate_time(text)

    message = str(err.value)
    assert message == "Can't estimate reading time for an empty list"

