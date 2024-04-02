def outter(a):
    def inner(b):
        return a**b
    return inner


outter10 = outter(10)
print(outter10(8))
