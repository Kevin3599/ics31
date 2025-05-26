def calc_toll(hour, is_morning, is_weekend):
    if is_morning:
        hour24 = hour % 12
    else:
        hour24 = (hour % 12) + 12

    if is_weekend:
        if hour24 < 7:
            return 6.05
        elif hour24 < 20:
            return 7.15
        else:
            return 6.10
    else:
        if hour24 < 7:
            return 6.15
        elif hour24 < 10:
            return 7.95
        elif hour24 < 15:
            return 6.90
        elif hour24 < 20:
            return 8.95
        else:
            return 6.40

if __name__ == '__main__':
    print(calc_toll(8, True, False))
    print(calc_toll(1, False, False))
    print(calc_toll(3, False, True))
    print(calc_toll(5, True, True))