""" WAP which accept number from user and return nuber of digits in that number"""

def digit_sum(No):
    sum = 0
    while No > 0:
        sum = sum + 1
        No = No // 10

    return sum

    

def main():
    print("Enter a number :")
    value = int(input())

    ret = digit_sum(value)

    print(f"Number of digit in {value} are {ret}")

if __name__ == "__main__":
    main()