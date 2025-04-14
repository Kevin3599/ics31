# (1) Get inputs
int_val = int(input('Enter integer (32 - 126):\n'))
float_val = float(input('Enter float:\n'))
char_val = input('Enter character:\n')
string_val = input('Enter string:\n')

# Output in original order
print(f"{int_val} {float_val} {char_val} {string_val}")

# (2) Output in reverse order
print(f"{string_val} {char_val} {float_val} {int_val}")

# (3) Convert integer to character
print(f"{int_val} converted to a character is {chr(int_val)}")
