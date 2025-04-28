services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
service_choice1 = input()
service_choice2 = input()
if service_choice1 not in services:
    print('ZyCar Wash')
    print('Base car wash - $10')
    print('-----')
    print('Total price: $10')
    exit()
else:
    total = services[service_choice1] + base_wash
    print('ZyCar Wash')
    print('Base car wash - $10')
    print(f'{service_choice1} - ${services[service_choice1]}')
if service_choice2 not in services:
    print("-----")
    print(f'Total price: ${total}')
    exit()
else:
    print(f'{service_choice2} - ${services[service_choice2]}')
    print("-----")
    total = services[service_choice1] + services[service_choice2] + base_wash
    print(f'Total price: ${total}')