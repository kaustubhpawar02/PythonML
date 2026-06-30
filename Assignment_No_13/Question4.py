# WAP which accept one number and prints its binary equivalent

def Bin_Output(No):

    binary =""
    while No > 0:
        binary=str(No%2)+binary
        No = No // 2
    return binary

def main():
    Value = int(input("Enter a number : "))

    Ret = Bin_Output(Value)

    print("Binary equivalent is :", Ret)

if __name__ == "__main__":
    main()