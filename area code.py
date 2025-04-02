
inputs = input().split()
area = int(inputs[0])
prefix = int(inputs[1])
line = int(inputs[2])

print("Country  Phone Number")
print("-------  ------------")

print(f"U.S.     +1 ({area}{prefix}-{line}")

print(f"Brazil   +55 ({area}){prefix + 100}-{line}")

print(f"Croatia  +385 ({area}){prefix}-{line+ 50}")

print(f"Egypt    +20 ({area + 30}){prefix}-{line}")

print(f"France   +33 ({prefix}){area}-{line}")
