grocery_list = {}

while True:
    try:
        item = input()
        if not item:
            break

        item = item.upper()
        grocery_list[item] = grocery_list.get(item, 0) + 1

    except EOFError:
        break
print()
for item, count in sorted(grocery_list.items()):
    print(f"{count} {item}")
