# WAPP using Scikit-learn to generate a classification report
# for the following dataset.
# Display precision, recall, F1-score, and support.

from sklearn.metrics import classification_report

actual =    [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

report = classification_report(actual,predicted)

print("Classification Report :")
print(report)