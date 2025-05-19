def feet_to_steps(user_feet):
    inches = user_feet / 2.5
    inches = int(inches)
    return inches
def main():
    user_feet = float(input())
    steps = feet_to_steps(user_feet)
    print(steps)
if __name__ == '__main__':
    main()