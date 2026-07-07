"""Write a lambda function using reduce() which accepts a list of numbers
and returns the maximum element"""


from functools import reduce

Maximum = lambda No1 , No2 : No1 if No1>No2 else No2

def main():

    Data = []

    print("Enter the number of elements in list :")
    values = int(input())

    print("Enter the Elements")

    for no in range(values):
        no = int(input())
        Data.append(no)
    print(Data)

    Max = reduce(Maximum,Data)

    print(f"Maximum of given list is {Max}")

if __name__ == "__main__":
    main()

