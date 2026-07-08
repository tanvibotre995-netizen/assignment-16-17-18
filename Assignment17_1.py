from Arithmetic import *

def main():
    value1=int(input("enter number:"))
    value2=int(input("enter number:"))

    Ret = Addition(value1,value2)

    print("Addition is",Ret)

    Ret = Substraction(value1,value2)

    print("Substraction is",Ret)

    Ret = Multiplication(value1,value2)

    print("Multiplication is",Ret)

    Ret = Division(value1,value2)

    print("Division is",Ret)

if __name__ == "__main__":
    main()
    
