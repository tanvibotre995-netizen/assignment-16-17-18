def prime(no):
    count=0

    for i in range(1,no+1):
        if no % i==0:
            count=count+1
    return count == 2

def main():
    list =[10,7,4,11,17]

    sum=0
    for no in list:
        if prime(no):
            sum = sum+no

    print("list is",list)
    print("addition of prime numbers:",sum)

if __name__ == "__main__":
    main()
