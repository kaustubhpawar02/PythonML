def length(name):
    sum = 0
    for i in name:
        sum = sum + 1
    return sum




def main():
    name = input("Input any string :")

    result = length(name)
    print("The length of given string is :",result)

if __name__ == "__main__":
    main() 