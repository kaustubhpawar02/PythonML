# WAP which accept one number and prints
# count of digit in that number

def chkCount(no):
    Count = 0

    while no>0:
        no = no//10
        Count = Count + 1

    return Count

def main():

    value = int(input("Enter a number :"))

    ret = chkCount(value)

    print("Number of digits are :",ret)

if __name__ == "__main__":
    main()