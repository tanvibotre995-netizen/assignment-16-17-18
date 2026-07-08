def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact=fact*i
    return fact
    

def main():
    No=int(input("enter number:"))

    Ret=Factorial(No)

    print("factorial is",Ret)

if __name__ == "__main__":
    main()
