#Given two integer numbers return their product only if the product is greater than 1000, else return their sum.

x = int(input(": "))
xx = int(input(": "))
xxx = x * xx
if xxx >= 1000:
    print(x + xx)
else:
    print(xxx)
