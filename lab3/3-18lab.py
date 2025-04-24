#dict
phonebook = {}
namephone = input().split()
name= input()
for i in namephone:
    cont,phone = i.split(",")
    phonebook[cont] = phone
print(phonebook[name])
