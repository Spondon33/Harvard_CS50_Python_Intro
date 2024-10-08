import sys


def main():
    check_command_line_arg()

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")

    count_lines = 0
    for line in lines:
        if not check_comment_or_empty_line(line):
            count_lines += 1
    print(count_lines)


def check_command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def check_comment_or_empty_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False


if __name__ == "__main__":
    main()
