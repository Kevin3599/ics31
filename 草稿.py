samples_count = int(input())

data_list = []
for i in range(samples_count):
    data_list.append(int(input()))
for numbers in data_list:
    if numbers  < 30:
        print(f'{numbers} {data_list.index(numbers)}')
    else:
        print("odd")