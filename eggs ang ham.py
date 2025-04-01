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
# 第一行输出：10
print(eggs(5, 3))  # eggs(5,3)的计算过程:
                   # c = 5-3 = 2
                   # a = 3+2 = 5
                   # b = 5
                   # return 5+5 = 10

# 第二行输出：6 12
print(ham(5, 3))   # ham函数内部print(a,b)的输出
                   # a = eggs(3,5) = 6
                   # b = eggs(6,3) = 12

# 第三行输出：12
                   # ham函数的返回值
                   # return eggs(6,12) = 12

# 第四行输出：5 3
print(a, b)        # 原始变量的值保持不变
