# WAP which accept one number 
# and print reverse of that number

def rev(no):
    revs = 0

    while no>0:
        digit = no%10
        revs =revs*10 +digit
        no = no//10

    return revs

def main():

    value = int(input("Enter a number :"))

    ret = rev(value)

    print("Reverse number is :",ret)

if __name__ == "__main__":
    main()