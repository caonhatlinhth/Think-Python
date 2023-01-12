
from traceback import print_stack
import math


def example():
    bruce = 5
    print (bruce)

    bruce = 7
    print (bruce)

#exercise1
def print_n(s,n):
    while n > 0:
        print(s)
        n = n-1

#exercise2
def square_root(a):
    x = a/2
    epsilon = 1e-21
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

#exercise3
def test_square_root(a):
    while a < 10:
        t = abs(square_root(a) - math.sqrt(a))
        print(f"{a} {square_root(a):<18} {math.sqrt(a):<18} {t:<18}")
        a = a+1

#exercise4
def eval_loop(input_string):
    while True:
        input_string = input("Your string ")
        if eval(input_string) == 'done':
            break
        print(eval(input_string))
    return eval(input_string)

#exercise5
def estimate_pi():
    last_term = 1
    sum = 0
    k = 0
    while last_term > 10**(-15):
        last_term = ((math.factorial(4*k) * (1103 + 26390 * k))) / ((math.factorial(k)**4) * 396*(4*k))
        sum = sum + last_term
        # k = 0
        # pi = (9801 * math.factorial(k)**4 * 396**4*k) / (2 * math.sqrt(2) * math.factorial(4*k) * (1103 + 2630*k))
        # k = k+1
    return pi

def main():
    print(estimate_pi())
    pass

if __name__ == "__main__":
    main()


# ((2 * math.sqrt(2))/9801) / 