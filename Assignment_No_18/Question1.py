
def add(Data):
    sum = 0
    for no in Data:
        sum = sum + no
    return sum 

def main():
    Data = []
    print("Enter Number of elements in list")
    values = int(input())
    print("Enter elements in list :")
    for no in range (values):
        no = int(input())
        Data.append(no)
    print(Data)

    ret  = add(Data)

    print("Addition is :",ret)

if __name__ == "__main__":
    main()