''' Type your code here. '''
first = int(input())
second = int(input())

if second < first:
    print("Second integer can't be less than the first.",end='')
else:
    current = first
    while current <= second:
        print(current, end=' ')
        current += 5
print('')