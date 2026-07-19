""" Display File Line by Line"""

""" WAP which aaccept a file name from the user and displays the contents of the file line by line on the screen"""

def main():

    filename = input("Enter File Nane :")
    fobj = open(filename,'r')
    Data = fobj.read()
    print(Data)


if __name__ == "__main__":
    main()