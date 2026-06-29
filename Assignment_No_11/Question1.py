# WAP which accept one number
# and checks whether it is prime or not

def CheckPrime(No):
    Count = 0

    for i in range(2, No):
        if No % i == 0:
            Count = Count + 1

    return Count

def main():
    Value = int(input("Enter a number: "))

    Result = CheckPrime(Value)

    if Value < 2:
        print("Number is Not Prime")
    elif Result == 0:
        print("Number is Prime")
    else:
        print("Number is Not Prime")

if __name__ == "__main__":
    main()