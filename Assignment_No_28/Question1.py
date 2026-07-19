"""Count Lines in a File"""

""" WAP which accepts a file name from user and counts how many lines are present in the file"""

def main():
    try:
        fobj = open("Assignment28.txt",'r')

        lines = fobj.readlines()
        count = len(lines)


        print("Total lines :",count)

        fobj.close()

        print("file has closed")
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")
        
if __name__ == "__main__":
    main()