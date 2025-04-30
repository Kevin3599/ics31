def make_change(cents):
    if cents <= 0:
        print("No change")
        return

    coins = [
        ("Dollar", "Dollars", 100),
        ("Quarter", "Quarters", 25),
        ("Dime", "Dimes", 10),
        ("Nickel", "Nickels", 5),
        ("Penny", "Pennies", 1)
    ]

    for singular, plural, value in coins:
        count = cents // value
        if count > 0:
            name = singular if count == 1 else plural
            print(f"{count} {name}")
            cents %= value

change = int(input())
make_change(change)
