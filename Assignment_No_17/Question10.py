""" WAP which accept number from user and return addition of 
digits in that number """

def Sum(No):
    Sum = 0
   
    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():

    print("Enter value :")
    value = int(input())

    Result = Sum(value)
    print("Addition of given digit is :",Result)

if __name__ == "__main__":
    main()