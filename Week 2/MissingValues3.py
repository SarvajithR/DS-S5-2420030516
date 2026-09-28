import pandas as pd 
import numpy as np
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40 , 35],
    'Department': ['HR' , 'Finance' , np.nan , 'Finance', 'IT']
})
print("Original Dataset (With Missing Values):")
print(df)
df_drop_rows = df.dropna()
print("After dropping rows:\n", df_drop_rows)