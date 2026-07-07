# Write a lambda function which accept one number and returns square of that number


Square = lambda No : No * No

def main():
    
    value = int(input("Enter the number :"))

    Result = Square(value)

    print(f"The Square of {value} is {Result}")

if __name__ == "__main__":
    main()




