import math
# Step 1: Read inputs
wall_height = float(input())
wall_width = float(input())
paint_cost = float(input())

# Calculate wall area
wall_area = wall_height * wall_width
print(f"Wall area: {wall_area:.1f} sq ft")

# Step 2: Calculate paint needed (1 gallon covers 350 sq ft)
paint_needed = wall_area / 350
print(f"Paint needed: {paint_needed:.3f} gallons")

# Step 3: Calculate number of cans needed (round up)
cans_needed = math.ceil(paint_needed)
print(f"Cans needed: {cans_needed} can(s)")

# Step 4: Calculate cost
paint_total = cans_needed * paint_cost
sales_tax = paint_total * 0.07
total_cost = paint_total + sales_tax

print(f"Paint cost: ${paint_total:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")