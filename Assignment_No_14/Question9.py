# Write a lambda function which accepts two numbers and return Multiplication

Mult = lambda No1 ,No2 : No1 * No2

def main():

    value1 = int(input("Enter a  number :"))

    value2 = int(input("Enter Second Number :"))

    Result = Mult(value1,value2)

    print(f"Multiplication of {value1} and {value2} is {Result}")

if __name__ == "__main__":
    main()