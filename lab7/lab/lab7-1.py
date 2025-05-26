def int_to_reverse_binary(integer_value):
    if integer_value == 0:
        return '0'
    
    binary = ''
    while integer_value > 0:
        remain = integer_value % 2
        binary += str(remain)
        integer_value = integer_value // 2
    return binary

def string_reverse(input_string):
    return input_string[::-1]

def main():
    usr_in = int(input())
    binary = int_to_reverse_binary(usr_in)
    reversed_string = string_reverse(binary)
    print(reversed_string)

if __name__ == '__main__':
    main()