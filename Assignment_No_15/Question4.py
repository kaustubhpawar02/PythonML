"""Write a lambda function using reduce() which accept
a list of numbers and returns the addition of all elements"""

from functools import reduce

Add = lambda No1 , No2 : No1+No2

def main():

    Data = []

    print("Enter the number of elements in the list :")
    value = int(input())

    print("Enter number of elements :")
    
    for no in range(value):
        no = int(input())
        Data.append(no)
    print(Data)

    Addition = reduce(Add,Data)

    print(f"Addition of all elements in list is : {Addition}")
        
if __name__ == "__main__":
    main()

    