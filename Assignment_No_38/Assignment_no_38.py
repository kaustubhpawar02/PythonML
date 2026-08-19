import pandas as pd
import matplotlib.pyplot as plt

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

    # “The dataset is slightly imbalanced, with a 60-40 distribution.”
    
    print(Border)

    # 5. Based on the dataset values,analyze whether :
    # Higher StudyHours increase the chance of passing
    # Higher Attendance improves FinalResult.
    # Write your observations in 4-5 lines

    print(df.groupby("FinalResult")[["StudyHours","Attendance"]].mean())
    # Students who passed generally have average study hours
    # Students with higher attendance tend to pass more often.
    # Lower study hours are associated with more failures.
    # Attendance appears to positively influence the final result.
    # Both study hours and attendance contribute to better performance.

    print(Border)

    # 6.Plot a histogram of StudyHours.
    # Explain what the distribution tells you.

    plt.hist(df["StudyHours"],bins = 10,edgecolor ="black")
    plt.title("Histogram of study hours")
    plt.xlabel("Study Hours")
    plt.ylabel("No of students")
    plt.show()

    # 7. Create a scatter plot of :
    # StudyHours vs PreviousScore
    # Use different colors for Pas and Fail Students.

    colors ={0:"red",1:"green"}
    plt.scatter(
        df["StudyHours"],
        df["PreviousScore"],
        c = df["FinalResult"].map(colors)
    )

    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.title("Study Hours v/s PreviouScore")
    plt.grid(True)
    plt.show()

    print(Border)

    # 8. Draw a boxplot for Attendance.
    # Identity if any outliers are present

    plt.boxplot(df["Attendance"])
    plt.title("Attendance Boxplot")
    plt.ylabel("Attendance")
    plt.show()

    print(Border)

    # 9. Create a plot showing the relationship between
    # AssignmentsCmpleted and FinalResult.
    # Explain your observation.

    plt.scatter(df["AssignmentsCompleted"],df["FinalResult"])
    plt.xlabel("Assignment completed ")
    plt.ylabel("Final Result")
    plt.title("Assignment completed v/s Final result")
    plt.show()

    print(Border)

    # 10.Plot SleepHours against FinalResults.
    # Does sleeping more guarantee success ? Explain.

    plt.scatter(df["SleepHours"],df["FinalResult"])
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final result")
    plt.title("SleepHours v/s Final result")
    plt.show()

    
    



def main():
    df = Student_Result("student_performance_ml.csv")

if __name__ == "__main__":
    main()
