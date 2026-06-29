# WAP which accept one number 
# and print number in reverse order 

def Natural(No):
    Num = []

    for i in range(No,0,-1):
        Num.append(i)
    return Num
         

def main():
    value = int(input("Enter a number :"))
    Result = Natural(value)
    print(Result)

if __name__ == "__main__":
    main() 