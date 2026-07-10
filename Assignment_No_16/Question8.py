def Display(No):
    for i in range(1,No+1):
        print("*",end=" ")

     

def main():
    value = int(input("Enter a number :"))

    Display(value)

if __name__ == "__main__":
    main()