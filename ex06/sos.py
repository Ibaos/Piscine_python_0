import sys


def main():
    """This program displays the encoded Morse Code of a string.

Args:
    text: the string argument
"""
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    text = sys.argv[1].upper()
    if not all(c.isalnum() for c in text if not c.isspace()):
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    MORSE = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'}

    res = []
    for c in text:
        if (c in MORSE):
            res.append(MORSE[c])
    print(' '.join(res))


if __name__ == "__main__":
    main()
