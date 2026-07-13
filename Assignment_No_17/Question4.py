""" WAP which accept one number from user and return adition of its factors"""

def Factor_Sum(No):
    Sum = 0
    for i in range(1,No):
        if (No%i == 0):
            Sum = Sum + i
    return Sum  

def main():
    
    print("Enter value :")
    value = int(input())

    result = Factor_Sum(value)

    print("sum of its factor is :",result)

if __name__ == "__main__":
    main()