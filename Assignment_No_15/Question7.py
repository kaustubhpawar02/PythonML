"""Write a lambda function using filter() which accepts
a list of strings and returns a list of Strings having
length greater than 5
"""
from functools import reduce

String = lambda str: len(str)>5


def main():

    ch = []
    print("Enter no of strings in list")
    values = int(input())

    print(f"Enter {values} String")

    for str in range(values):
        str = input()
        ch.append(str)
    print(ch)

    Result = list(filter(String,ch))

    print(f"String having length greater than 5 is : {Result}")


if __name__ == "__main__":
    main()