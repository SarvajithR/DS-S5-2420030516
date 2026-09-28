import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Iam = 4
data = np.random.poisson(Iam, 1000)
sns.histplot(data,kde=False,stat='density',bins=range(min(data),max(data)+1))
plt.title('Poisson Distribution (λ = {})'.format(Iam))
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

