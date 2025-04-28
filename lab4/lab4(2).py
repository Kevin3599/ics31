is_leap_year = False
input_year = int(input())
input_last2 = input_year % 100
if input_year % 4 ==0 and input_last2 != 0:
    print(f"{input_year} - leap year")
elif input_year % 400 == 0: 
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")