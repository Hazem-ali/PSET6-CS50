from cs50 import get_string


def main():
    codestring = get_string("Number: ")
    code = int(codestring)
    cardtype(code)


def getLuhn(code):
    # codestr 4003600000000014
    code1 = int(code / 10)
    summation = 0
    while int(code1) > 0:
        condition = 2 * (code1 % 10)
        if condition >= 10:
            summation += 1 + int(condition % 10)
        else:
            summation += condition
        code1 /= 100
        code1 = int(code1)
    while int(code) > 0:
        summation += int(code % 10)
        code /= 100
        code = int(code)
    return summation


def digits(code):
    count = 0
    while int(code) > 0:
        count += 1
        code /= 10
        code = int(code)
    return count


def cardtype(code):
    div = 1
    while div <= code:
        div *= 10
    div /= 10
    digcode = digits(code)
    block = int(code / div)
    if digcode < 13 or digcode > 16 or int((getLuhn(code)) % 10) != 0:
        print("INVALID")
    elif block == 4:
        print("VISA")
    elif int(code / (div / 10)) == 37 or int(code / (div / 10)) == 34:
        if digcode == 15:
            print("AMEX")
        else:
            print("INVALID")
    elif block == 5:
        div /= 10
        block = int(code / div)
        if int(block % 50) > 0 and int(block % 50) < 6:
            if digcode == 16:
                print("MASTERCARD")
            else:
                print("INVALID")
    else:
        print("INVALID")


main()