items = []
prices = []
quantities = []

print("Enter food item name:")
items.append(input())
print("Enter item price:")
prices.append(float(input()))
print("Enter item quantity:")
quantities.append(int(input()))

print("\nRECEIPT")
cost = prices[0] * quantities[0]
print(f"{quantities[0]} {items[0]} @ ${prices[0]:.2f} = ${cost:.2f}")
print(f"Total cost: ${cost:.2f}\n")

print("Enter second food item name:")
items.append(input())
print("Enter item price:")
prices.append(float(input()))
print("Enter item quantity:")
quantities.append(int(input()))

print("\nRECEIPT")
for i in range(2):
    cost = prices[i] * quantities[i]
    print(f"{quantities[i]} {items[i]} @ ${prices[i]:.2f} = ${cost:.2f}")

total_cost = sum(p * q for p, q in zip(prices, quantities))
gratuity = total_cost * 0.15

print(f"Total cost: ${total_cost:.2f}")
print(f"\n15% gratuity: ${gratuity:.2f}")
print(f"Total with tip: ${total_cost + gratuity:.2f}")
