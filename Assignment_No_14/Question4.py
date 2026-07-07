# Write a lambda function which accept two number and return minimum number

Minimum = lambda No1 , No2 : No1 if No1<No2 else No2
print(Minimum)



def main():

    value1 = int(input("Enter a Number :"))

    value2 = int(input("Enter second number :"))

    Result = Minimum(value1,value2)

    print(f"Among {value1} and {value2} : {Result} is Minimum")

if __name__ == "__main__":
    main()