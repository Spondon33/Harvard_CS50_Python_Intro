def main():
    camel_case_input = input("camelCase: ")
    snake_case_output = snake_case(camel_case_input)
    print("snake_case: " + snake_case_output)


def snake_case(sc):
    sc_result = sc[0].lower() + ""
    for char in sc[1:]:
        if char.isupper():
            sc_result += "_" + char.lower()
        else:
            sc_result += char
    return sc_result


main()
