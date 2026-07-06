def even(n):
    return (n%2 == 0)

def main():
    value = int(input("enter number:"))

    ret = even(value)

    print(ret)
if __name__ == "__main__":
    main()
