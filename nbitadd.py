from logic import *

def adjust(x, y):
    l1, l2 = len(x), len(y)
    if l1 > l2:
        y = y.rjust(l1, "0")
        print (y)
    elif l2 > l1:
        x = x.rjust(l2, "0")
    return (x, y)


def full_adder(x, y, cin):
    sum = XOR(XOR(x, y), cin)
    cout = OR(OR(AND(x, y), AND(y, cin)), AND(x, cin))
    return (sum, cout)


def binary_adder(x, y, cin=0):
    l = len(x)
    sum = ""
    carry = cin
    for i in range(l - 1, -1, -1): #reverse by using loop
        bit_sum, carry = full_adder(int(x[i]), int(y[i]), carry)
        sum = str(int(bit_sum)) + sum
    return (sum, carry)


if __name__ == "__main__":
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    x, y = adjust(x, y) #adjusting and adding 0 to balance
    sum, cout = binary_adder(x, y)
    print(f"Sum = {sum}, Carry out = {cout}")