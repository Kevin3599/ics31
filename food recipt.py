items = []
prices = []
quantities = []

for i in range(2):
    if i == 1:
        print("\nEnter second food item name:")
    else:
        print("Enter food item name:")
    items.append(input())
    
    print("Enter item price:")
    prices.append(float(input()))
    
    print("Enter item quantity:")
    quantities.append(int(input()))

def receipt(items, prices, quantities):
    print("\nRECEIPT")
    subtotal = 0
    
    for i in range(2):
        cost = prices[i] * quantities[i]
        subtotal += cost
        print(f"{quantities[i]} {items[i]} @ ${prices[i]:.2f} = ${cost:.2f}")

    tip = subtotal * 0.15
    total = subtotal + tip
    

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"15% tip: ${tip:.2f}")
    print(f"Total with tip: ${total:.2f}")

receipt(items, prices, quantities)
