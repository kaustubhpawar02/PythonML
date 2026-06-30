# WAP which accepts marks and displays grade

def DisplayGrade(Marks):
    if Marks >= 75:
        return "Distinction"
    elif Marks >= 60:
        return "First Class"
    elif Marks >= 50:
        return "Second Class"
    else:
        return "Fail"


def main():
    Marks = int(input("Enter marks: "))

    result = DisplayGrade(Marks)
    print("Grade :",result)


if __name__ == "__main__":
    main()