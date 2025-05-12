''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

for i in range(-10,10):
    for j in range(-10,10):
        if a*i + b*j == c and d*i + e*j == f:
            print(f'x = {i},y = {j}')
            break
    else:  # 只有当内层循环正常完成(没找到解)时才继续
        continue
    break  # 只有当找到解时才会执行到这里
else:  # 只有当外层循环正常完成(完全没找到解)时才会执行
    print('There is no solution')