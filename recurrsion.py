# recurrsion is a concept of a function calling itself
import sys

print(sys.getrecursionlimit()) # how to get recurrsion limit

# to increse limit below
sys.setrecursionlimit(2000)


def greet():
    print('hello')
    greet()


#greet()