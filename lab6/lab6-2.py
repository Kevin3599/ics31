title_data = input('Enter a title for the data:')
print('You entered', title_data)
column1 = input('Enter the column 1 header:')
print(f'You entered:', column1)
column2 = input('Enter the column 2 header:')
print(f'You entered:', column2)
author_dict = {}
while True:
    data_point = input('Enter a data point (-1 to stop input):')
    if data_point == '-1':
        break
    elif ',' not in data_point:
        print('Error: No comma in string.')
        continue
    elif data_point.count(',') != 1:
        print('Error: Too many commas in input.')
        continue
    text, number = data_point.split(',')
    number = number.strip()
    print(f'Data string:{text}')
    print(f'Number integer:{number}')
    if not number.isdigit():
        print('Error: Comma not followed by an integer.')
        continue
    number = int(number)
    author_dict[text] = number

print(f'{title_data:>33}')
print(f'{column1:<20}|{column2:>23}')
print('-' * 43)
for index in author_dict:
    print(f'{index:<20}|{author_dict[index]:>23}')
for index in author_dict:
    print (f'{index:<20}')
    print('*' * author_dict[index])
