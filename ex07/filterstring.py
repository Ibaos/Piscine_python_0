import sys


def main():
    """This program accepts two arguments: a string (S) and an integer (N).
It displays the list of words from S that have a length greater than N.

Args:
    string: the string (S)
    length: the length (N)
"""
    try:
        ac = len(sys.argv)
        if ac != 3:
            raise AssertionError("the arguments are bad")
        string = sys.argv[1]
        length = sys.argv[2]
        if not all(c.isalpha() for c in string if not c.isspace()):
            raise AssertionError("the arguments are bad")
        if not length.isdigit():
            raise AssertionError("the arguments are bad")
        N = int(length)
        result = list(filter(lambda word: len(word) > N, string.split()))
        print(list(result))
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)
        


if __name__ == "__main__":
    main()
