def main(x):
    def inner(y):
        return x * y
    return inner


main10 = main(10)
print(main10(8))
