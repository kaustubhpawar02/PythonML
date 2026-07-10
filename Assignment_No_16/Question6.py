def Check(No):
    if No == 0:
        print("Zero")
    elif No > 0:
        print("Positive Number")
    else:
        print("Negative Number")
    

def main():

    value = int(input("Enter a number :"))

    Check(value)

if __name__ == "__main__":
    main()

