def frequency(data,no):
    count=0
    for i in data:
        if i == no:
            count=count+1
    return count

def main():
    data=[20,45,79,56,90]

    print("list is",data)

    no=int(input("enter number to find frequency:"))

    result=frequency(data,no)

    print("frequency of",no,"is:",result)

if __name__ == "__main__":
    main()

