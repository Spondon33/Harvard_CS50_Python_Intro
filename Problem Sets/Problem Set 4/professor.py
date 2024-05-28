import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        ans = x + y

        for attempt in range(3):
            try:
                user_ans = int(input(f"{x} + {y} = "))
                if user_ans == ans:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                break
        else:
            print(ans)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            user_input = input("Level: ")
            if user_input.isdigit():
                level = int(user_input)
                if level in [1, 2, 3]:
                    return level
                else:
                    continue
        except ValueError:
            raise


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y
    else:
        raise ValueError


if __name__ == "__main__":
    main()
