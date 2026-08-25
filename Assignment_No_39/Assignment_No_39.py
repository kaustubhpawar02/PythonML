import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix

# Q1 
# Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().

df = pd.read_csv("student_performance_ml.csv")

print(df.head())

feature_cols = [
    "StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state = 42)

model = DecisionTreeClassifier(max_depth=5) # Limits the decision tree to a maximum depth of 5 levels , Maximum 5 levels deep to prevent overfitting

model = model.fit(X_train,Y_train) 

# Q2 .
# Use the trained model to predict results for X_test.
# Display predicted values along with actual values.

Y_pred = model.predict(X_test)

print("Actual Values :",Y_test)
print("Predicted Values :",Y_pred)

# Q3 
# Calculate model accuracy using accuracy_score.
# Display the result in percentage format.

Accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy is :",Accuracy)

# Q4 
# Generate confusion matrix using sklearn.
# Display it using ConfusionMatrixDisplay.

confusion_mat = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix is :",confusion_mat)