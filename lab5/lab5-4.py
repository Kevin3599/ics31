roster = {}

# 初始输入五个球员信息
for i in range(1, 6):
    jersey = int(input("Enter player {}'s jersey number:\n".format(i)))
    rating = int(input("Enter player {}'s rating:\n".format(i)))
    roster[jersey] = rating

# 打印初始名册
print("ROSTER")  # 移除了额外的换行符
for jersey in sorted(roster):
    print("Jersey number: {}, Rating: {}".format(jersey, roster[jersey]))

def print_menu():
    print("MENU")  # 移除了额外的换行符
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")

while True:
    print_menu()
    option = input("Choose an option:\n")  # 移除了额外的换行符

    if option == 'q':
        break

    elif option == 'o':
        print("ROSTER")  # 移除了额外的换行符
        for jersey in sorted(roster):
            print("Jersey number: {}, Rating: {}".format(jersey, roster[jersey]))

    elif option == 'a':
        jersey = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        roster[jersey] = rating

    elif option == 'd':
        jersey = int(input("Enter a jersey number:\n"))
        if jersey in roster:
            del roster[jersey]

    elif option == 'u':
        jersey = int(input("Enter a jersey number:\n"))
        if jersey in roster:
            rating = int(input("Enter a new rating for player:\n"))
            roster[jersey] = rating

    elif option == 'r':
        rating = int(input("Enter a rating:\n"))
        print("ABOVE {}".format(rating))  # 移除了额外的换行符
        for jersey in sorted(roster):
            if roster[jersey] > rating:
                print("Jersey number: {}, Rating: {}".format(jersey, roster[jersey]))

    else:
        print("Invalid option.")
