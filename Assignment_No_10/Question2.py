# WAP TO ACCEPT ONE NUMBER 
# AND PRINT sum of first N natural numbers

def main():
    No = int(input("Enter a number :"))

    Sum = 0

    for i in range(1,No+1,1):
        Sum = Sum + i

    print("Sum of FIRST ",No,"Numbers is :",Sum)

if __name__ == "__main__":
    main()