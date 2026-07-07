# Write a lambda function which accept two number and return maximum number

Maximum = lambda No1 , No2 : max(No1,No2)

def main():

    value1 = int(input())

    value2 = int(input())

    Result = Maximum(value1,value2)

    print(f"Among {value1} and {value2} : {Result} is Maximum")

if __name__ == "__main__":
    main()