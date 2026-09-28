import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

low = 0
high = 10
data = np.random.uniform(low, high, 1000)
sns.histplot(data, kde=True, stat='density')
plt.title('Uniform Distribution ({low}, {high})')
plt.xlabel('Value') 
plt.ylabel('Density')
plt.show()