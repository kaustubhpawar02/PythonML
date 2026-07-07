"""Write function using reduce() which accepts a list of numbers and 
returns the product of all elements"""


from functools import reduce

Mult = lambda No1 , No2 : No1*No2

def main():

    Data = []

    print("Enter the number of elements in the list :")
    value = int(input())

    print("Enter number of elements :")
    
    for no in range(value):
        no = int(input())
        Data.append(no)
    print(Data)

    Multiplication = reduce(Mult,Data)

    print(f"Multiplication of all elements in list is : {Multiplication}")
        
if __name__ == "__main__":
    main()