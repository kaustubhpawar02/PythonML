""" WAP  which contains one function named as ChkNum() which accept one 
parameter as a number. If number is even then it should display Even number otherwise
display Odd number on console"""

def ChkNum(No):
    if No % 2 == 0:
        return True
    else :
        return False
    

def main():

    value = int(input("Enter a number :"))
    Result = ChkNum(value)

    if Result == True :
        print("Even Number")

    else :
        print("Odd Number")

if __name__ == "__main__":
    main()