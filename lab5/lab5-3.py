num  = int(input())
while num>0:
    print(f'{num % 2}', end='')
    num //= 2
print('\n')