# Write a lambda function which accepts one number and returns cube of that number

Number_Cube = lambda No : No ** 3

def main():
    value = int(input("Enter a number :"))
    Result = Number_Cube(value)

    print(f"The Cube of {value} is {Result}")
     
if __name__ == "__main__":
    main()