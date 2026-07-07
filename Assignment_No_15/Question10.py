"""Write a lambda function using filter() and return even numbers """

Even_Numbers = lambda No : No % 2 == 0


def main():

    Data =[]

    print("Enter the number of elements in the list : ")

    values = int(input())

    print(f"Enter {values} elements in list :")

    for no in range(values):
        no = int(input())
        Data.append(no)
    print(Data)

    Result = list(filter(Even_Numbers,Data))

    print(f"Even number of list is : {Result}")
    print("Count of Even Numbers is : ",len(Result))



if __name__ == "__main__":
    main()
