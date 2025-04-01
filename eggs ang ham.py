def eggs(a: int, b: int)-> int:
    c = a - b
    a = b + c
    b = a
    return a + b
def ham(a: int, b: int) -> int:
    a = eggs(b, a)
    b = eggs(a, b)
    print(a, b)
    return eggs(a, b)
a = 5
b = 3
print(eggs(a, b))
print(ham(a, b))
print(a, b)
