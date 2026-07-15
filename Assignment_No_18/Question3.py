
def Minimum(Data):
    mini = Data[0]
    for i in Data:
        if i < mini :
            mini = i
    return mini    



def main():
    Data = []
    print("Enter Number of elements in list")
    values = int(input())
    print("Enter elements in list :")
    for no in range (values):
        no = int(input())
        Data.append(no)
    print(Data)

    ret  = Minimum(Data)

    print("minimum from list is  :",ret)

if __name__ == "__main__":
    main()