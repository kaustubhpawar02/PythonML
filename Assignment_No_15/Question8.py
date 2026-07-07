"""Write a lambda function using filter() which accepts a list of numbers 
and returns a list of numbers divisible by both 3 and 5"""


from functools import reduce

Chk_Divisibility = lambda No : No % 3 == 0 and No % 5 == 0

def main():

    Data = []

    print("Enter the number of elements in the list :")
    value = int(input())

    print("Enter number of elements :")
    
    for no in range(value):
        no = int(input())
        Data.append(no)
    print(Data)

    Check = list(filter(Chk_Divisibility,Data))

    print(f"{Check}")
        
if __name__ == "__main__":
    main()