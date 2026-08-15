""" Write a Python program to load the file student_performance_ml.csv using pandas"""

""" Display the following : """


import pandas as pd

def Student_Performance(DataPath):

    df = pd.read_csv(DataPath)

    # Display first 5 records

    print(df.head())

    # Display last 5 records

    print(df.tail())

    # Display total number of rows and columns

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # List of columns names

    print(df.columns.tolist())

    # Datatype of each column

    print(df.dtypes)
    

def main():
    Student_Performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()

    

