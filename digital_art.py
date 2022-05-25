import matplotlib.pyplot as plt 
from functools import reduce

# Convert the number n to a list of digits in base b.
def to_base(n, b):
    return [n] if n < b else to_base(n//b, b) + [n%b]

# Convert a list of digits in base b to decimal.
def to_dec(l, b):
    return reduce(lambda x, y: b*x + y, l)

# The function we want to use when replacing digits. 
def p(n, d, b):
    return (d*n)%b

# The function replacing digits.
def a(n, b):
    return to_dec([p(n, d, b) for d in to_base(n, b)], b)

if __name__ == "__main__":
    base = int(input("Base: "))
    lower = int(input("Lower exponent: "))
    upper = int(input("Upper exponent: "))
    file_name = input("Enter filename: ")

    X = range(base**lower, base**upper)
    Y = [a(x, base) for x in X]

    fig = plt.figure() 
    plt.plot(X, Y, ".k", markersize=0.6)
    plt.show()
    fig.savefig(f"{file_name}.png", dpi=200, bbox_inches="tight")