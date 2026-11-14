# WAPP that calculates TP , TN , FP , FN for the following array
#  Display all four values

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(actual,predicted)

TN , FP , FN , TP = cm.ravel()

print("True Positive (TP):", TP)
print("True Negative (TN):", TN)
print("False Positive (FP):", FP)
print("False Negative (FN):", FN)

print("Confusion Matrix:")
print(cm)
