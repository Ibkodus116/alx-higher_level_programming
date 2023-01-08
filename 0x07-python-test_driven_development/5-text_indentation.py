#!/usr/bin/python3
"""

Module handling a function that prints a text
with 2 new lines after each of these characters: '.', '?' and ':'

"""


def text_indentation(text):
    """A function that prints a text with 2 new lines
    after each of these characters: '.', '?' and ':'

    Arg:
        text: a string of words

    Print:
        prints the given words with double new line where '.' or '?' or ':' are

    Raise:
        TypeError: when something else aside string is passed
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    words = ""
    lst = []

    if "." in text or "?" in text or ":" in text:
        for i in range(len(text)):
            words += text[i]

            if text[i] == "." or text[i] == "?" or text[i] == ":":
                j = i
                lst.append(words)
                words = ""
        for x in lst:
            print(x.strip(" ") + "\n")

        extra = text[j+1:i+1]
        if extra:
            print(extra.strip(" "), end="")
    else:
        if text:
            print(text)
