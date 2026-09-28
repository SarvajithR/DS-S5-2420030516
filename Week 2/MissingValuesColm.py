import pandas as pd 
import numpy as np
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40 , 35],
    'Department': ['HR' , 'Finance' , np.nan , 'Finance', 'IT']
})
print("Original Dataset (With Missing Values):")
print(df)
df_drop_cols = df.dropna(axis=1)
print("After dropping columns:\n", df_drop_cols)