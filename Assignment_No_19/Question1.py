"""WAP which contain lambda function which accepts one parameter and return power of two"""

Power = lambda No : No ** 2

def main():
    no = int(input("Enter the number :"))

    ret = Power(no)

    print(f"Square of {no} is : {ret}")

if __name__ == "__main__":
    main()