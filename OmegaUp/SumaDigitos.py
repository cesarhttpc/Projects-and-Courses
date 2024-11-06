number_chain = input()


integer = int(number_chain)
if integer < 0 or integer > 99999:
    print(0)
else:
    split_numbers = [int(num) for num in number_chain]
    sum = 0
    for digito in split_numbers:
        sum = sum + (digito)

    print(sum)
    