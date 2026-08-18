import pandas as pd


def Student_Result(filename):

    df = pd.read_csv(filename)

    Border = "-"*100
    print(Border)

    # Write a Python program to load the file student_performance_ml.csv using pandas
    # Display :

    # First 5 records
    print(df.head())

    print(Border)

    # Last 5 records
    print(df.tail())

    print(Border)

    # Total number of rows and columns
    print("Total no of rows and columns :",df.shape)
    print("Total no of rows :",df.shape[0])
    print("Total no of columns :",df.shape[1])

    print(Border)



def main():
    df = Student_Result("student_performance_ml.csv")

if __name__ == "__main__":
    main()
