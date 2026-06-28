# WAP TO accept one number and
# checks whether it is divisible by 3 and 5

def main():
    No =int(input("Enter a number :"))
    if (No%3 == 0 and No%5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()
    

    