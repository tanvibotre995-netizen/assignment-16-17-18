def AddDigit(n):
    Add = 0

    while n > 0:
        digit = n % 10
        Add = Add + digit
        n = n // 10

    print("Addition of digits:", Add)


def main():
    no = int(input("Enter number: "))
    AddDigit(no)


if __name__ == "__main__":
    main()
