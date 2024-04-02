def f(a, *, b):
    return a, b


c = f(1, b=2)
print(c)
