def factor(n):
    sum=0

    for i in range(1,n+1):
        if n % i==0:
            sum=sum+i
    return sum
def main():
    no=int(input("enter number:"))

    result=factor(no)

    print("addition of factor is",result)

if __name__ == "__main__":
    main()
