while True:
    try:
        user_input = input("Fraction: ")
        x, y = map(int, user_input.split("/"))
        user_input = x / y

        if user_input * 100 <= 1:
            print("E")
            break
        elif user_input * 100 >= 99:
            print("F")
            break
        else:
            print(f"{user_input:.0%}")
            break

    except (ZeroDivisionError, ValueError):
        pass
