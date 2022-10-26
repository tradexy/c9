import sys

print('Hello, World!')

print('The sum of 4 and 5 is 9.')

sum = int(sys.argv[1]) + int(sys.argv[2])

print('The sum of {0} and {1} is {2}.'.format(sys.argv[1], sys.argv[2], sum))