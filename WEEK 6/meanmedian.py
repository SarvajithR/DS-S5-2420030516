import pandas as pd
from sklearn.datasets import load_iris
from statistics import mode

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("First 5 rows of dataset:")
print(df.head())

# Mean (average)
mean_values = df.mean()
print("\nMean values:")
print(mean_values)

# Median (middle value)
median_values = df.median()
print("\nMedian values:")
print(median_values)

# Mode (most frequent value)
# Pandas mode returns a DataFrame (can be multiple modes)
mode_values = df.mode().iloc[0]
print("\nMode values:")
print(mode_values)

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
print("First 5 rows of dataset:")
print(df.head())
# Range (max- min)
range_values  = df.max() - df.min()
print("\nRange values:")
print(range_values)
#Variance
variance_values = df.var()
print("\nVariance values:")
print(variance_values)
#Standard Deviation
std_values = df.std()
print("\nStandard Deviation values:")
print(std_values)
#Interquartile Range(IQR)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print("\nInterquartile Range (IQR): ")
print(IQR)

import scipy as a
from scipy.starts import kurtosis
data = [10, 25, 14, 26, 35, 45, 67, 90, 40, 50, 60, 10, 16, 18, 20]
s.stats.skew(data, axis=0, bias = True)
kurtosis(data, axis=0, bias = True)

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, column=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
skewness_values = df.skew()
print("\nSkewness values:")
print(skewness_values)
kurtosis_values = df.kurt()
print("\nKurtosis values:")
print(kurtosis_values)
