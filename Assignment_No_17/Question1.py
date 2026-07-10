from Arithmetic import *


def main():
    print("Enter first number : ")
    value1 = int(input())

    print("Enter second  number : ")
    value2 = int(input())

    ret = Add(value1,value2) 

    print("Addition is : ",ret)

    ret = Sub(value1,value2) 

    print("Subtraction is :",ret)

    ret = Mult(value1,value2) 

    print("Multiplication is :",ret)

    ret = Div(value1,value2) 

    print("Divison is :",ret)

if __name__ == "__main__":
    main()