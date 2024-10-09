import sys
import csv
from tabulate import tabulate


def main():
    check_command_line_arg()

    try:
        if sys.argv[1] == 'sicilian.csv':
            pizzas = sicilian()
        elif sys.argv[1] == 'regular.csv':
            pizzas = regular()
        else:
            sys.exit("Unknown file")

        if pizzas:
            print(tabulate(pizzas, headers="keys", tablefmt="grid"))
        else:
            sys.exit("No pizzas found")

    except IndexError:
        sys.exit(":)")


def sicilian():
    sicilian_pizza = []
    try:
        with open("sicilian.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                sicilian_pizza.append({
                    "Sicilian Pizza": row["Sicilian Pizza"],
                    "Small": row["Small"], "Large": row["Large"]
                })
        return sicilian_pizza

    except FileNotFoundError:
        sys.exit("File does not exist")


def regular():
    regular_pizza = []
    try:
        with open("regular.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                regular_pizza.append({
                    "Regular Pizza": row["Regular Pizza"],
                    "Small": row["Small"], "Large": row["Large"]
                })
        return regular_pizza

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith('.csv'):
        sys.exit("Not a CSV file")


if __name__ == '__main__':
    main()
