import sys
try:
    ac = len(sys.argv)
    if ac == 1:
        sys.exit(0)
    elif ac > 2:
        raise AssertionError("more than one argument is provided")
    
    try:
        int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    if (int(sys.argv[1]) % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print("AssertionError:", e)
    sys.exit(1)