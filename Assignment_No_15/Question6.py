"""Write a lambda function using reduce() which accepts list of numbers and returns the minimum elements"""


from functools import reduce

Minimum = lambda No1 , No2 : No1 if No1<No2 else No2

def main():

    Data = []

    print("Enter the number of elements in list :")
    values = int(input())

    print("Enter the Elements")

    for no in range(values):
        no = int(input())
        Data.append(no)
    print(Data)

    Min = reduce(Minimum,Data)

    print(f"Minimum of given list is {Min}")

if __name__ == "__main__":
    main()

