import pandas as pd


def Student_Result(filename):

    df = pd.read_csv(filename)

    Border = "-"*100
    print(Border)

    # 1.Write a Python program to load the file student_performance_ml.csv using pandas
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

    # List column names
    print("Columns names are :",df.columns)

    print(Border)

    # Data types of each column
    print("Data type of each column :\n",df.dtypes)

    print(Border)

    # 2.WAP to :

    #Display total number of students in the dataset
    print("Total no of students in dataset :",len(df))

    print(Border)

    # Count how many students passed (FinalResult = 1)
    print("Count of Students Passed :",(df["FinalResult"]==1).sum())

    print(Border)

    # Count how many students Failed (FinalResult = 0)
    print("Count of Students Failed :",(df["FinalResult"]==0).sum())

    print(Border)

    # 3.Using pandas functions,calculate and display:

    # Average StudyHours
    print("Average StudyHours :",(df["StudyHours"]).mean())

    print(Border)

    # Average Attendance
    print("Average Attendance :",(df["Attendance"]).mean())

    print(Border)

    # Maximum PreviousScore
    print("Max PreviousScore :",df["PreviousScore"].max())

    print(Border)

    # Minimum SleepHours
    print("Minimum SleepHours :",df["SleepHours"].min())

    print(Border)

    # 4. Use value_counts() to analyze the distribution of FinalResult.
    # Calculate the percentage of Pass and Fail student
    # Is the dataset balanced ? Justify your answer

    print(df["FinalResult"].value_counts())

    print(Border)

    print("Percentage of Pass Students :",(df["FinalResult"]==1).mean()*100)
    print("Percentage of Fail Students :",(df["FinalResult"]==0).mean()*100)

    print(Border)

    # “The dataset is slightly imbalanced, with a 60-40 distribution.”
    
    print(Border)



def main():
    df = Student_Result("student_performance_ml.csv")

if __name__ == "__main__":
    main()
