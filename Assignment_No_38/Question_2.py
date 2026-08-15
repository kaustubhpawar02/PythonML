import pandas as pd 

# Display total numbers of students in the dataset

def Student_Performance(DataPath):

    df = pd.read_csv(DataPath)

    print("Total number of students :",len(df))

    # Count how many students Passed (FinalResult = 1)

    print("Number of students passed:", (df['FinalResult'] == 1).sum())

    # Count how many students Passed (FinalResult = 0)

    print("Number of students failed :", (df['FinalResult'] == 0).sum())

def main():
    Student_Performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()