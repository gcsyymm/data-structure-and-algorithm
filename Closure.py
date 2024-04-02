def deco(fn):
    def inner():
        return "A" + fn
    return inner
