def Display(No):
    if No % 5 == 0:
        return True
    else :
        return False 



def main():
    value = int(input("enter a number :"))

    result = Display(value)

    if result == True:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()