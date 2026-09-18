import sys


def main():
    """This program takes a single string argument and displays the sums of :
- upper-case characters
- lower-case characters
- punctuation characters
- digits
- spaces

Args:
    text: the single string argument
"""
    try:
        ac = len(sys.argv)
        if ac == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
        elif ac > 2:
            raise AssertionError("more than one argument is provided")
        else:
            text = sys.argv[1]
        print(f"The text contains {len(text)} characters:")
        print(f"{sum(1 for c in text if c.isupper())} upper letters")
        print(f"{sum(1 for c in text if c.islower())} lower letters")
        punctuation = sum(1 for c in text if not (c.isalnum() or c.isspace()))
        print(f"{punctuation} punctuation marks")
        print(f"{sum(1 for c in text if c.isspace())} spaces")
        print(f"{sum(1 for c in text if c.isdigit())} digits")
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
