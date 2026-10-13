## The Problem
```
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

```


## The Function
``` python

def estimate_time(text):
    # Parameters
    # text: string representing text
    # Return
    # float: decimal representing reading time
    #Side Effects?
    pass
```

## Examples
``` python
"""
Given a text of 200 words
it will return a time of 1

"""
estimate_time("....200....") => 1.0

"""
Given a text of 400 words
it will return a time of 2

"""
estimate_time("....400....") => 2.0

"""
Given a text of 300 words
it will return a time of 1.5

"""
estimate_time("....300....") => 1.5
"""
Given an empty text
it will raise an error

"""
estimate_time("") => raise Exeption("Can't estimate reading time for an empty list")
```