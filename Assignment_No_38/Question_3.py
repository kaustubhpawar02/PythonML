
"""Using pandas functions,calculate and display"""

import pandas as pd 

def Student_Performance(DataPath):

    df = pd.read_csv(DataPath)

    # Average Study Hours

    print("Average Study Hours : ",df['StudyHours'].mean())

    # Average Attendence 

    print("Average Attendence :",df['Attendance'].mean())

    # Maximum Attendence

    print("Maximum Attendence is :",df['Attendance'].max())

    # Minimum SleepHours

    print("Minimum Sleephours :",df['SleepHours'].min())

def main():
    Student_Performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()