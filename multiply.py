# Multiplication of Two Unsigned Integer Binary Numbers By Patrial-Product Method

from nbitSubtract import binary_adder


def adjust_number(x, y):
    l1, l2 = len(x), len(y)
    # For n-bit multiplication, the result is 2n-bit
    max_bit = max(l1, l2)
    x = x.rjust(2 * max_bit, "0")
    y = y.rjust(2 * max_bit, "0")
    return (x, y)


def binary_multiplication(m, q, count):
    # partial product is initially started with zero
    sum = "0" * len(m)
    for i in range(count):
        # Test Yo, if it is 1 add content of X to the accumulator sum
        if q[-1] == "1":
            sum = binary_adder(sum, m)
        # Left shift X
        m = m[1:] + "0" #first bit replaced
        # Right shift Y
        q = "0" + q[:-1] #last bit exclusive not included
    return sum


if __name__ == "__main__":
    m = input("Enter multiplicand: ")
    q = input("Enter multiplier: ")
    count = len(q)  # no of bits in y
    m, q = adjust_number(m, q)
    product = binary_multiplication(m, q, count)
    print(f"Product = {product}")
