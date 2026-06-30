# WAP which accept one number and
# check it is perfect number or not

def Perfect_Number(No):
    sum = 0
    for i in range(1,No):
        if No%i==0:
            sum=sum+i
    if sum == No:
        print("Perfect")
    else:
        print("Not Perfect")


def main():
    Value = int(input("Enter a number :"))
    Perfect_Number(Value)

if __name__ == "__main__":
    main()