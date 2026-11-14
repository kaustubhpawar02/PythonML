# WAPP to calculate the Euclidean distance between two points before and after applying
# feature scaling , and explain the difference in results

import numpy as np
from sklearn.preprocessing import StandardScaler

# Dataset

df = np.array([
    [25,20000],
    [30,40000],
    [35,80000]
])

# Select two points

p1 = df[0]
p2 = df[1]

# Euclidean distance before scaling
distance_before = np.sqrt(np.sum((p2 - p1)**2))   # np.linalg.norm(p2 - p1) can also be used to calculate Euclidean Distance

print("Distance Before Scaling :", distance_before)

# Feature Scaling
scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

# After Scaling 
p1 = scaled_data[0]
p2 = scaled_data[1]

distance_after = np.sqrt(np.sum((p2-p1)**2))
print("Distance After Scaling :",distance_after)


"""Before feature scaling, the Euclidean distance is very large because the income feature has much larger numerical values than age. After applying StandardScaler, both features are converted to a common scale, reducing the dominance of income. Therefore, feature scaling improves distance calculations in algorithms such as KNN and K-Means.

Important concept: The distance decreases here, but feature scaling does not always decrease Euclidean distance. It changes the contribution of each feature to the distance."""