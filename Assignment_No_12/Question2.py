# WAP which accept one number and print its factors

def Factors(No):

    fact = []

    for i in range(1,No+1,1):
        if No % i == 0:
            fact.append(i)
    return fact
        
    

def main():
    value = int(input("Enter a number :"))

    Ret = Factors(value)

    print("Factors of given numbers is :",Ret)

if __name__ == "__main__":
    main()