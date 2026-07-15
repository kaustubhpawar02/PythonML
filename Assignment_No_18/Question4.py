
def Frequency(Data):
    ele = int(input())
    count = 0
    for i in Data:
        if i == ele:
           count = count + 1
    return count

def main():
    Data = []
    print("Enter Number of elements in list")
    values = int(input())
    print("Enter elements in list :")
    for no in range (values):
        no = int(input())
        Data.append(no)
    print(Data)

    print("element to search")

    ret  = Frequency(Data)

    print("Frequency of that element is :",ret)

if __name__ == "__main__":
    main()