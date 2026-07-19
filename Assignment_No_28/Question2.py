""" Count Words in a File"""

""" WAP which accepts a file name from user and counts the total number of words in that file"""

def main():
    try:
        filename = input("Enter file name : ")
        fobj = open(filename,'r')
        data = fobj.read()

        words = data.split()

        print("Total Words :",len(words))


        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()