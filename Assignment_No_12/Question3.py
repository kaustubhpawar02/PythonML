# WAP which accept two numbers and
# print add ,sub,multand division


def Add(No1,No2):
    return No1+No2

def Sub(No1,No2):
    return No1-No2

def Mult(No1,No2):
    return No1*No2

def Div(No1,No2):
    if No2 == 0:
        return "Error"
    else:
        return No1//No2

def main():
    value1 = int(input("Enter Value 1 :"))
    value2 = int(input("Enter Value 2 :"))

    print("Addition is :\n",Add(value1,value2))
    print("Subtraction is :\n",Sub(value1,value2))
    print("Multiplication is :\n",Mult(value1,value2))
    print("Division  is :\n",Div(value1,value2))

if __name__ == "__main__":
    main()