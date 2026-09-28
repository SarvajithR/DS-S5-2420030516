import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
mu = 0
sigma = 1
data = np.random.normal(mu,sigma,1000)
sns.histplot(data,kde=True,stat="density")
plt.title(f'Normal Distribution (mean={mu},std={sigma})')
plt.xlabel("value")
plt.ylabel("Desnity")
plt.show()