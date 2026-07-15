
def Maximum(Data):
    maxim = Data[0]
    for i in Data:
        if i > maxim :
            maxim = i
    return maxim    



def main():
    Data = []
    print("Enter Number of elements in list")
    values = int(input())
    print("Enter elements in list :")
    for no in range (values):
        no = int(input())
        Data.append(no)
    print(Data)

    ret  = Maximum(Data)

    print("maximum from list is  :",ret)

if __name__ == "__main__":
    main()