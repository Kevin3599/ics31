num_in = int(input())
if 11<= num_in <=99:
    while True:
        print(num_in)
        if num_in % 10 == num_in // 10:
            break
        num_in -= 1
else:
    print('Input must be 11-99')
