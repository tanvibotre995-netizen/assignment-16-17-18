def ChkNum(n):
    if(n%2== 0):
        print("even number")
    else:
        print("odd number")

def main():
    n=int(input("enter number:"))

    ChkNum(n)

if __name__ == "__main__":
    main()
