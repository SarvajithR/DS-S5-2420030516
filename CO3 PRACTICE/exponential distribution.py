import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Iam = 1.5
data = np.random.exponential(scale=1 / Iam, size=1000)
sns.histplot(data, kde=True, stat='density')
plt.title('Exponential Distribution (λ = 1.5)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
