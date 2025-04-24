#basic sets
my_fruit1 = input()
my_fruit2 = input()
my_fruit3 = input()

your_fruit1 = input()
your_fruit2 = input()

their_fruit = input()

# 1. TODO: Define a set, fruits, containing my_fruit1, my_fruit2, and my_fruit3
fruits = {my_fruit1, my_fruit2, my_fruit3}
print(sorted(fruits))

# 2. TODO: Add your_fruit1 and your_fruit2 to fruits
fruits.add(your_fruit1)
fruits.add(your_fruit2)
print(sorted(fruits))

# 3. TODO: Add their_fruit to fruits
fruits.add(their_fruit)
print(sorted(fruits))

# 4. TODO: Add your_fruit1 to fruits
fruits.add(your_fruit1)
print(sorted(fruits))

# 5. TODO: Remove my_fruit1 from fruits
fruits.remove(my_fruit1)

print(sorted(fruits))
