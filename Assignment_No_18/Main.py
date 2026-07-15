import MarvellousNum


def ListPrime(lst):
    sum = 0

    for i in lst:
        if MarvellousNum.ChkPrime(i):
            sum = sum + i

    return sum


def main():
    n = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")

    for i in range(n):
        value = int(input())
        data.append(value)

    ans = ListPrime(data)

    print("Addition of prime numbers is:", ans)


if __name__ == "__main__":
    main()