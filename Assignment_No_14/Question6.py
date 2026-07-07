# Write a lambda function which accepts one number and return True if number is odd otherwise False

Chk_Even_Odd = lambda No : True if No % 2 != 0 else False

def main():

    value = int(input("Enter a number :"))

    Result = Chk_Even_Odd(value)

    print(f"{Result}")

if __name__ == "__main__":
    main()