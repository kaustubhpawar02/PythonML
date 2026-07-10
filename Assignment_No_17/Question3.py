import sys

def fact(No):
    Mult = 1
    for i in range(1,No+1):
        Mult = Mult * i

    return Mult

def main():

    sys.set_int_max_str_digits(10000000)
    value = int(input("Enter the Number :"))

    result = fact(value)

    print(f"factorial of {value} is : {result}")

if __name__ == "__main__":
    main()
