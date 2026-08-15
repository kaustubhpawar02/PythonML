""" """
""" """

import os


def main():
    filename = input("Enter File Name :")
    fobj = open(filename,'r')
    
    ret = os.path.exists(filename)

    if(ret == True):
        print("File is present in current directory")
    else:
        print("There is no such file")

    fobj.close()
        
if __name__ == "__main__":
    main()