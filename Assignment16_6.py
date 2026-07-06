def number(n):
    if(n>0):
        print("positive")
    elif(n<0):
        print("Negative")
    else:
        print("Zero")

def main():
    n=int(input("enter number:"))

    number(n)

if __name__ == "__main__":
    main()
