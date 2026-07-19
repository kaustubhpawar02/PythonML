""" Search a Word in File"""

""" WAP which accepts a file name and a word from the user and checks whether that word is present in that file or not"""
def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        fobj = open(filename,'r')
        data = fobj.read()

        if word in data:
            print(f"{word} is present in {filename}")
        else:
            print("Word is not present.")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()