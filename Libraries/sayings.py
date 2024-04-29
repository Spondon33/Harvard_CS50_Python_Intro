def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello {name}")


def goodbye(name):
    print(f"Good bye, {name}")


# checks if the script is run directly or imported as a module
if __name__ == "__main__":
    main()
