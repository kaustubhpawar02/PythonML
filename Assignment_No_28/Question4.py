""" Copy File Contents into Another File"""

""" WAP which accepts two file names from user"""

""" first file is an existing file """

""" second file is a new file """

""" Copy all contents from the first file into the second file"""

def main():
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    try:
        fsrc = open(source, "r")
        fdest = open(destination, "w")

        data = fsrc.read()
        fdest.write(data)

        print("Data copied successfully.")

        fsrc.close()
        fdest.close()

    except FileNotFoundError:
        print("Source file not found.")

if __name__ == "__main__":
    main()