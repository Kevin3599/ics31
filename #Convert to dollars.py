#Convert to dollars
nickels = float(input())
dimes = float(input())
quarters = float(input())
def calculate(nickels, dimes, quarters):
    total = (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    return total
total = calculate(nickels, dimes, quarters)
print(f"Amount:$ {total:.2f}")