"""Write a lambda function using map() which accept a list of numbers and returns a 
list of squares of each number"""

Squares = lambda No : No * No

def main():

    Data = []
    print(f"Enter the number of elements in the List")
    value = int(input())
    print(f"Enter the elements :")
    for no in range(value):
        no = int(input())
        Data.append(no)
    print(f"list before Squaring each element: {Data}")

    Result = list(map(Squares,Data))

    print(f"After Squaring each elements in list is : {Result}\n")
    

if __name__ == "__main__":
    main()