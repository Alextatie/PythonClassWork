# n! from n=0 to n=19
f, n = 1, 0
while n <= 19:
    print(n, "!=", f)
    n += 1
    f = f * n
