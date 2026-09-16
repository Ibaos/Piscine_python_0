import sys

ac = len(sys.argv)
if ac == 1:
	sys.exit(0)
elif ac > 2:
	print("AssertionError: more than one argument is provided")
	sys.exit(1)

try:
	int(sys.argv[1])
except:
	print("AssertionError: argument is not an integer")
	sys.exit(1)

if (int(sys.argv[1]) % 2) == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")
