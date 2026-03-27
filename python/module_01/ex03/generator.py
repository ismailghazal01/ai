import random

def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        yield "ERROR"
        return

    words = text.split(sep)

    if option == "shuffle":
        random.shuffle(words)
    elif option == "unique":
        words = list(set(words))
    elif option == "ordered":
        words.sort()
    elif option not in [None]:
        yield "ERROR"
        return

    for word in words:
        yield word