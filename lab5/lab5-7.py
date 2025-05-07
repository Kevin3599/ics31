while True:
    text = input()
    
    if text == "Done" or text == "done" or text == "d":
        break
    else:
        print(text[::-1])
