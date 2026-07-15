from functools import reduce

def ChkPrime(No):
    if No<=1:
        return False
    
    for i in range (2,No):
        if No % i == 0:
            return False
        
    return True

def Inc(no):
    return no*2

Maximum = lambda x,y : x if x>y else y

def main():
    Data = []

    print("Number of elements:")
    No = int(input())

    print("Enter elements:")
    for i in range(No):
        Data.append(int(input()))

    Result1 = list(filter(ChkPrime, Data))
    print("Data after filtr is :",Result1)

    Result2 = list(map(Inc,Result1))
    print("Data after map is :",Result2)

    Result3 = reduce(Maximum,Result2)
    print("Data after reduce is :",Result3)


if __name__ == "__main__":
    main()