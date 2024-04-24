def main():
    amount = 50
    coin_machine = 0

    while amount > coin_machine:
        print("Amount Due: " + str(amount - coin_machine))
        user_input = int(input("Insert coin: "))
        coin_machine += process_amount(user_input)
    else:
        print("Change Owed: " + str(coin_machine - amount))


def process_amount(coin):
    valid_amount = [5, 10, 25]
    if coin in valid_amount:
        return coin
    else:
        return 0


main()
