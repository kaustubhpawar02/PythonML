# WAP TO ACCEPT ONE NUMBER 
# AND PRINT Factorial  numbers


def main():
    No = int(input("Enter a number :"))

    mult = 1

    for i in range(No,1,-1):
        mult = mult*i
    print(mult)
    
    
if __name__ == "__main__":
    main()
