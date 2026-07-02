#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with length of string and its first character."""
    if sentence == "":
        return (0, None)

    return (len(sentence), sentence[0])
