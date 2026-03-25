def text_analyzer(text=None):
    if text is None:
        text = input("What is the text to analyze?\n>> ")

    if not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return

    upper = 0
    lower = 0
    space = 0
    punct = 0

    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            space += 1
        else:
            punct += 1

    total = len(text)

    print(f"The text contains {total} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punct} punctuation mark(s)")
    print(f"- {space} space(s)")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()