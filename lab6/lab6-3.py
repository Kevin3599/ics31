title = input("Enter a title for the data:\n")
print(f"You entered: {title}\n")

col1 = input("Enter the column 1 header:\n")
print(f"You entered: {col1}\n")
col2 = input("Enter the column 2 header:\n")
print(f"You entered: {col2}\n")

names = []
values = []

while True:
    data_point = input("Enter a data point (-1 to stop input):\n")
    if data_point == "-1":
        break

    if data_point.count(",") == 0:
        print("Error: No comma in string.\n")
        continue
    elif data_point.count(",") > 1:
        print("Error: Too many commas in input.\n")
        continue

    name_part, value_part = data_point.split(",")
    name_part = name_part.strip()
    value_part = value_part.strip()

    if not value_part.isdigit():
        print("Error: Comma not followed by an integer.\n")
        continue

    print(f"Data string: {name_part}")
    print(f"Data integer: {value_part}\n")
    names.append(name_part)
    values.append(int(value_part))

print()
print(f"{title:>33}")
print(f"{col1:<20}|{col2:>23}")
print("-" * 44)
for i in range(len(names)):
    print(f"{names[i]:<20}|{values[i]:>23}")

print()
for i in range(len(names)):
    print(f"{names[i]:>20} {'*' * values[i]}")
