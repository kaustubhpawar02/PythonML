import pandas as pd


def Student_Result(filename):

    df = pd.read_csv(filename)

    # Write a Python program to load the file student_performance_ml.csv using pandas
    # Display :

    # First 5 records
    print(df.head())

    # Last 5 records
    print(df.tail())


def main():
    df = Student_Result("student_performance_ml.csv")

if __name__ == "__main__":
    main()
