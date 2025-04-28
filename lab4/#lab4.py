#lab4
highway_number = int(input())
if 1 < highway_number < 100:
    number = highway_number % 2
    if number == 0:
        print(f'I-{highway_number} is primary, going east/west.')
    else:
        print(f'I-{highway_number} is primary, going north/south.')
elif 100 < highway_number < 999:
    primary_number = highway_number % 100
    if 0 < primary_number < 100:
        if primary_number % 2 == 0:
            print(f'I-{highway_number} is auxiliary, serving I-{primary_number}, going east/west.')
        else:
            print(f'I-{highway_number} is auxiliary, serving I-{primary_number}, going north/south.')
    else:
        print(f'{highway_number} is not a valid interstate highway number.')
else:
    print(f'{highway_number} is not a valid interstate highway number.')


