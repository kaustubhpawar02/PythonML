# WAP TO ACCEPT ONE NUMBER 
# AND PRINT all Even Numbers till that number

def main():
    No = int(input("Enter a number :"))

    for i in range(2,No+1,2):
        print(i)
    
    
if __name__ == "__main__":
    main()
