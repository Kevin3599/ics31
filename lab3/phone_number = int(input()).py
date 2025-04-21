phone_number = int(input())
lst = phone_number % 10000 #last four
frtsix = phone_number // 10000 #first three
mid3 = frtsix % 1000 #middle three
frs3 = frtsix // 1000 #first three
print(f"({frs3}) {mid3}-{lst}")