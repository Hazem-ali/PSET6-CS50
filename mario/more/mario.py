from cs50 import get_int


def main():
    while True:
        n = get_int("Height: ")
        if n > 0 and n < 9:
            bridge(n)
            break


def bridge(n):
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:  # condition of # drawing
                print("#", end="")
            else:
                print(" ", end="")
        print("  ", end="")
        for j in range(i + 1):  # because i when begins with 0 I must print one #
            print("#", end="")
        print()


main()