# Write a lambda function which accept one number and returns True if divisible by 5

Check = lambda No : True if No % 5 == 0 else False


def main():

    value = int(input("Enter a number :"))

    Result = Check(value)

    print(f"{Result}")

if __name__ == "__main__":
    main()