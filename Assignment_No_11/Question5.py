# WAP which accept one number from user 
# check whether it is palindrome or not

def palin(No):
    Original = No
    Reverse = 0

    while No > 0:
        Digit = No % 10
        Reverse = Reverse * 10 + Digit
        No = No // 10

    if Original == Reverse:
        print("Number is Palindrome")
    else:
        print("Number is Not Palindrome")

def main():
    Value = int(input("Enter a number: "))
    palin(Value)

if __name__ == "__main__":
    main()

    