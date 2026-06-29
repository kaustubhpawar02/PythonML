# WAP which accept one number 
# and print number starting from 1

def Natural(No):
    Num = []

    for i in range(1,No+1):
        Num.append(i)
    return Num
         

def main():
    value = int(input("Enter a number :"))
    Result = Natural(value)
    print(Result)

if __name__ == "__main__":
    main() 