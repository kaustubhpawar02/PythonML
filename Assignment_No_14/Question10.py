# Write a lambda function which accept two number and return largest number

Largest = lambda No1 , No2 : No1 if No1>No2 else No2


def main():

    value1 = int(input("Enter a Number :"))

    value2 = int(input("Enter second number :"))

    Result = Largest(value1,value2)

    print(f"Among {value1} and {value2} : {Result} is Largest")

if __name__ == "__main__":
    main()