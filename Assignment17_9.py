def CountDigit(n):
    count = 0

    while n > 0:
        n = n // 10
        count = count + 1

    print("Number of digits:", count)


def main():
    no = int(input("Enter number: "))
    CountDigit(no)


if __name__ == "__main__":
    main()
