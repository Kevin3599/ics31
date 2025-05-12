n = int(input())

numbers = []
for i in range(n):
    number = float(input())
    numbers.append(number)

max_value = max(numbers)

for number in numbers:
    normalized = number / max_value
    print(f'{normalized:.2f}')