def F(x):
    if x <= -2:
        return ((x * x) - 3 * x) / (1 + 4 * x)
    else:
        return (5 - 2 * x) / (1 + x * x)

print(F(10))