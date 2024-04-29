months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        user_input = input("Date: ")
        if "/" in user_input:
            month, day, year = map(int, user_input.split("/"))
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(year, f"{month:02}", f"{day:02}", sep="-")
                break
        else:
            if "," in user_input:
                user_input = user_input.replace(",", "")
                month_name, day, year = user_input.split()
                month = months.index(month_name) + 1

                year = int(year)
                month = int(month)
                day = int(day)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(year, f"{month:02}", f"{day:02}", sep="-")
                    break
    except (ValueError, IndexError):
        pass
