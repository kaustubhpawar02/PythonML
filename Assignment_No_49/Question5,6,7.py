
# ============================================================
# Q5. Explain the concept of a Classification Report in
# Machine Learning. Why is it used and what type of models
# require it?
# ============================================================

# A Classification Report is a performance evaluation tool
# in Machine Learning used to measure how accurately a
# classification model predicts the output classes.
#
# It provides the following metrics:
# 1. Precision
# 2. Recall
# 3. F1-score
# 4. Support
# 5. Accuracy
#
# Why is it used?
# 1. To evaluate the performance of a classification model.
# 2. To identify incorrect predictions.
# 3. To understand how well a model identifies each class.
# 4. To compare different classification models.
#
# Which models require it?
# 1. Logistic Regression
# 2. Decision Tree Classifier
# 3. Random Forest Classifier
# 4. K-Nearest Neighbors (KNN)
# 5. Support Vector Machine (SVM)
# 6. Naive Bayes
#
# Conclusion:
# A classification report helps evaluate and understand
# the performance of Machine Learning classification models.


# ============================================================
# Q6. In a Classification Report, explain the meaning of
# the following metrics:
# Precision, Recall, F1 Score, Support and Accuracy.
# ============================================================

# 1. Precision:
# Precision measures how many predicted positive values
# are actually positive.
#
# Formula:
# Precision = TP / (TP + FP)
#
#
# 2. Recall:
# Recall measures how many actual positive values are
# correctly predicted by the model.
#
# Formula:
# Recall = TP / (TP + FN)
#
#
# 3. F1-Score:
# F1-score is the harmonic mean of Precision and Recall.
# It balances both metrics.
#
# Formula:
# F1 = 2 * (Precision * Recall) / (Precision + Recall)
#
#
# 4. Support:
# Support represents the total number of actual occurrences
# of each class in the dataset.
#
# Example:
# If a dataset contains 4 positive and 4 negative values:
# Support for class 0 = 4
# Support for class 1 = 4
#
#
# 5. Accuracy:
# Accuracy measures the percentage of total predictions
# that are correct.
#
# Formula:
# Accuracy = (TP + TN) / (TP + TN + FP + FN)


# ============================================================
# Q7. Consider the following data:
#
# Actual Values:
# [1, 1, 1, 1, 0, 0, 0, 0]
#
# Predicted Values:
# [1, 1, 0, 1, 0, 1, 0, 0]
#
# Determine:
# True Positive (TP)
# True Negative (TN)
# False Positive (FP)
# False Negative (FN)
# ============================================================

# Step 1: Compare actual and predicted values.
#
# Position   Actual   Predicted   Result
#    1          1         1         TP
#    2          1         1         TP
#    3          1         0         FN
#    4          1         1         TP
#    5          0         0         TN
#    6          0         1         FP
#    7          0         0         TN
#    8          0         0         TN
#
# Step 2: Calculate all four values.
#
# 1. True Positive (TP):
# Actual = 1 and Predicted = 1
# TP = 3
#
# 2. True Negative (TN):
# Actual = 0 and Predicted = 0
# TN = 3
#
# 3. False Positive (FP):
# Actual = 0 and Predicted = 1
# FP = 1
#
# 4. False Negative (FN):
# Actual = 1 and Predicted = 0
# FN = 1
#
# Final Answer:
# TP = 3
# TN = 3
# FP = 1
# FN = 1
#
# Confusion Matrix:
#
#                 Predicted 0    Predicted 1
# Actual 0             3              1
# Actual 1             1              3
#
# Conclusion:
# The program's classification results contain 3 True
# Positives, 3 True Negatives, 1 False Positive and
# 1 False Negative.
