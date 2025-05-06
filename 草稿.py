while True:
    num = input()
    if num.isdigit():
        num2 = int(num)
        if num2 > 0:
            print("Thanks!")
            break
    print("That's not a positive integer! Try again:")