# WAP which accept one number 
# and print nnultiplication table

def main():
  
    N = int(input("Enter a Number : "))

    Mult = 0

    i = 1

    print("Multiplication Table is :\n")

    while(i*N <= N*10):

        Mult = Mult + N

        print(Mult)

        i = i + 1

if __name__ == "__main__":
    main()