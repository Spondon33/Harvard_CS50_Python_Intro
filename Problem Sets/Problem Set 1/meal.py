def main():
    answer = input("What time is it? ")
    time = convert(answer)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")
    else:
        print(None)


def convert(time):
    hours, minutes = time.split(":")
    new_minute = float(minutes) / 60
    return float(hours) + new_minute


if __name__ == "__main__":
    main()
