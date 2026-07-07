"""Write a lambda function using filter() which accept a list of numbers and returns a 
list of Even of each number"""

Odd = lambda No : No % 2 != 0

def main():

    Data = []
    print(f"Enter the number of elements in the List")
    value = int(input())
    print(f"Enter the elements :")
    for no in range(value):
        no = int(input())
        Data.append(no)
    print(f"list before Filtering each element: {Data}")

    Odd_Numbers = list(filter(Odd,Data))

    print(f"After filter returing the list of Odd Numbers : {Odd_Numbers}\n")
    

if __name__ == "__main__":
    main()