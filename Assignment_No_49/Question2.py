# Write a Python program that calculates the variance and standard deviation of the dataset :

import numpy as np

dataset = [6,7,8,9,10,11,12]
print("Dataset is :",dataset)

df = np.array(dataset)
print("Variance of Dataset is :")
print(np.var(df))

print("Standard Deviation of Dataset is :")
print(np.std(df))



