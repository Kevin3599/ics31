def golf_score(strokes, par):
    if par not in [3, 4, 5]:
        print(f"Par {par} in {strokes} strokes is Error")
        return

    diff = strokes - par

    if diff == -2:
        score = "Eagle"
    elif diff == -1:
        score = "Birdie"
    elif diff == 0:
        score = "Par"
    elif diff == 1:
        score = "Bogey"
    else:
        score = "Error"

    print(f"Par {par} in {strokes} strokes is {score}")

# 示例调用
strokes = int(input())
par = int(input())
golf_score(strokes, par)
