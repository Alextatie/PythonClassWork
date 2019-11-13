# GCD with Euclidean algorithm
print("Enter two integers:")
a, b, c = int(input()), int(input()), 0
print("GCD(", a, ",", b, ")=")
while b != 0:
    c = a
    a = b
    b = c % b
print("gcd=", a)
