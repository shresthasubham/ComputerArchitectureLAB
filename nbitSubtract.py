# Subtraction of two unsigned integer binary number
from logic import *

#adjust
def adjust_number(x, y):
    l1, l2 = len(x), len(y)
    if l1 > l2:
        y = y.rjust(l1, "0")
    elif l2 > l1:
        x = x.rjust(l2, "0")
    return (x, y)

#fulladder
def full_adder(x, y, cin):
    sum = XOR(XOR(x, y), cin)
    cout = OR(OR(AND(x, y), AND(y, cin)), AND(x, cin))
    return (sum, cout)


def binary_adder(x, y, cin=0):
    l = len(x)
    sum = ""
    carry = cin
    for i in range(l - 1, -1, -1):
        bit_sum, carry = full_adder(int(x[i]), int(y[i]), carry)
        sum = str(int(bit_sum)) + sum
    return sum

#compliment 2s
def twos_complement(y):
    # leave all least significant 0's and first 1 unchanged,
    # and, replace 1's by 0's and 0's by 1's in all other higher significant bits
    n = len(y)
    i = n - 1
    y1 = ""
    for i in range(n - 1, -1, -1):
        y1 = y[i] + y1
        if y[i] == "1":
            i = i - 1  # first 1 found gives eg XX100
            break
        i = i - 1
    while i >= 0:#flips remaining set of numbers
        if y[i] == "0":
            y1 = "1" + y1
        else:
            y1 = "0" + y1
        i = i - 1
    return y1


if __name__ == "__main__":
    x = input("Enter first number A: ")
    y = input("Enter second number B: ")
    x, y = adjust_number(x, y)
    sum = binary_adder(x, twos_complement(y))
    print(f"Difference(A-B) is  {sum}")
