# WAP using StandardScaler to perform feature scaling on the following dataset

import numpy as np
from sklearn.preprocessing import StandardScaler

df = np.array([
    [25 , 20000],
    [30 , 40000],
    [35 , 80000]
])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

print("Original Dataset:")
print(df)

print("Scaled Dataset:")
print(scaled_data)


"""Original Dataset:
[[   25 20000]
 [   30 40000]
 [   35 80000]]
 
Scaled Dataset:
[[-1.22474487 -1.06904497]
 [ 0.         -0.26726124]
 [ 1.22474487  1.33630621]] """