Mult = lambda No1, No2 : No1*No2

def main():
    no1 = int(input("Enter the no1 :"))
    no2 = int(input("Enter the no2 :"))

    ret = Mult(no1,no2)

    print(f"Multiplication is  : {ret}")

if __name__ == "__main__":
    main()