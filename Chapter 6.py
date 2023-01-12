from operator import truediv
from pickle import FALSE, TRUE

#exercise1
def compare(x,y):
    if x > y:
        return 1
    if x < y:
        return -1
    if x == y:
        return 0

#exercise3
def is_between(x, y, z):
    if x <= y and y <=z:
        return True
    else:
        return False

#example
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#exercise7
def is_power():
    a = int(input('a = '))
    b = int(input('b = '))
    if a%b == 0 and a/b % b == 0:
        return True
    else:
        return False

#exercise6  
def middle_2(word2):
    return word2[1:-1]

def middle_1(word1):
    return word1[1:-1]

def middle_0(word0):
    return word0[1:-1]

def first(a_string):
    return a_string[0]

def last(a_string):
    return a_string[-1]

def middle(a_string):
    return a_string[1:-1]

def is_palindrome(a_string):
    a = len(a_string)
    if a <= 1:
        return True
    if a >= 1 and a % 2 == 0 and first(a_string) != last(a_string):
        return False
    return is_palindrome(middle(a_string))

# def exercise6(a_string):
#     if len(a_string) <= 1:
#         return  True
#     if a_string[0] != a_string[-1]:
#         return False
#     return exercise6(a_string[-1, ])

##exercise8
def gcd(a, b):
    
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

def gcd1(a,b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd1(b,a % b)
    
def main():
    print(is_palindrome('tailaelahkjfaw'))
    # print(exercise6('hi'))
    # a = int(input('a = '))
    # b = int(input('b = '))
    # # if b == 0 or b > a:
    # #     t = b
    # #     b = a
    # #     a = t

    # print(gcd1(a, b))
    
    pass

if __name__ == "__main__":
    main()