def factorial(x: int):
    return 1 if x == 1 else factorial(x-1)*x


print(factorial(10))
