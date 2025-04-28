month = input()
day = int(input())

dict_month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
              'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

if month in dict_month:
    month_number = dict_month[month]
    if 1 <= day <= month_days[month_number]:
        if (month_number == 3 and day >= 20) or (3 < month_number < 6) or (month_number == 6 and day <= 20):
            print('Spring')
        elif (month_number == 6 and day >= 21) or (6 < month_number < 9) or (month_number == 9 and day <= 21):
            print('Summer')
        elif (month_number == 9 and day >= 22) or (9 < month_number < 12) or (month_number == 12 and day <= 20):
            print('Autumn')
        elif (month_number == 12 and day >= 21) or (month_number < 3) or (month_number == 3 and day <= 19):
            print('Winter')
    else:
        print('Invalid')
else:
    print('Invalid')