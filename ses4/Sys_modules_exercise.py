
# Opgave 4
import sys

""" def greeting(x):
    print(x)

    if len(x) == 2 and x[1] == '-it':
        print('interactive terminal started')
    if len(x) == 3 and x[2] == '--rm':
        print('Will be removed at exit')

greeting(sys.argv) """

def greeting(x):
    print(x)
    if len(x) < 2:
        print('Usage: python Modules_exercise.py [-it]{--rm}')
        sys.exit()
    elif len(x) >= 2 and x[1] == '-it':
        print('All good!')
    else:
        print('Usage: python Modules_exercise.py [-it]{--rm}')
        sys.exit()

greeting(sys.argv)