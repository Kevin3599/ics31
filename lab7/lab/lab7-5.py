def swap_values(user_val1, user_val2, user_val3, user_val4):
    num_list = [user_val1, user_val2, user_val3, user_val4]
    return num_list[1], num_list[0], num_list[3], num_list[2]

def main():
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())
    val1, val2, val3, val4 = swap_values(user_val1, user_val2, user_val3, user_val4)
    print(val1, val2, val3, val4)

if __name__ == '__main__':
    main()