from functools import reduce

def CHK(no):
    return 70 <= no <= 90

def Inc(no):
    return no+10

Product = lambda x,y : x*y

def main():
    Data = []

    print("Number of elements:")
    No = int(input())

    print("Enter elements:")
    for i in range(No):
        Data.append(int(input()))

    Result1 = list(filter(CHK, Data))
    print("Data after filtr is :",Result1)

    Result2 = list(map(Inc,Result1))
    print("Data after map is :",Result2)

    Result3 = reduce(Product,Result2)
    print("Data after reduce is :",Result3)


if __name__ == "__main__":
    main()