import sys


def main():
    """This program accepts two arguments: a string (S) and an integer (N).
It displays the list of words from S that have a length greater than N.

Args:
    string: the string (S)
    length: the length (N)
"""
    ac = len(sys.argv)
    if ac != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    string = sys.argv[1]
    length = sys.argv[2]
    if not all(c.isalnum() for c in string if not c.isspace()):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if not length.isdigit():
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    N = int(length)
    result = list(filter(lambda word: len(word) > N, string.split()))
    print(list(result))


if __name__ == "__main__":
    main()
