#LAB: Pizza party
from math import *
people = int(input())
num_pizzas = ceil(people*2 / 12)
cost = num_pizzas * 14.95
print(f"People: {people}")
print(f'Pizza(s): {num_pizzas}')
print(f'Cost for {num_pizzas} pizza(s): ${cost:.2f}')
