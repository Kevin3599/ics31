line = int(input())
num = int(input())
head_width = int(input())
while head_width <= num:
    head_width = int(input())
for i in range(line):
    print(num * '*')
for i in range(head_width, 0, -1):
    print('*' * i)
