import sys


def main():
    """This program displays the encoded Morse Code of a string.

Args:
    text: the string argument
"""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1].upper()
        if not all(c.isalnum() for c in text if not c.isspace()):
            raise AssertionError("the arguments are bad")

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
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
