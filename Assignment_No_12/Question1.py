# WAP which accept one character and
# check whether it is vowel or constant

def chkvowel_consonant(vc):
    vowel = ('a','e','i','o','u')

    
    if len(vc)!=1 or not vc.isalpha():
        return "Invalid Input"
    
    elif vc in vowel:
        return "Vowel"
    
    else:
        return "Consonant"



def main():
    
    ch = input("Enter character :")

    result=chkvowel_consonant(ch.lower())

    print("Enter Input is :",result)


if __name__ == "__main__":
    main()