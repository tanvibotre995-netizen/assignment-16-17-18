def prime(n):
    if n<=1:
        print("number is not prime")
        return
    
    for i in range(2,n-1):
        if n % i == 0:
            print("number is not prime")
            return
            
    print("number is prime")
        

def main():
    no=int(input("enter number:"))
    prime(no)
    
    
if __name__ == "__main__":
    main()

    
