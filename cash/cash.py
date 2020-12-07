from cs50 import get_float


def main():
    while True:
        n = get_float("Change owed: ")
        if n > 0:
            result = cash(n)
            print(result)
            break


def cash(n):
    counter = 0
    n *= 100
    while n >= 25:
        n -= 25
        counter += 1
    while n >= 10:
        n -= 10
        counter += 1
    while n >= 5:
        n -= 5
        counter += 1
    while n >= 1:
        n -= 1
        counter += 1
    return counter


main()