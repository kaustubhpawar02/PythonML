# WAP which accepts marks and displays grade

def DisplayGrade(Marks):
    if Marks >= 75:
        return "Distinction"
    elif Marks >= 60:
        print("First Class")
    elif Marks >= 50:
        print("Second Class")
    else:
        print("Fail")


def main():
    Marks = int(input("Enter marks: "))
    DisplayGrade(Marks)

    result = DisplayGrade(Marks)
    print(result)


if __name__ == "__main__":
    main()