import numpy as np
import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
print(df.describe())
print(df.columns)
print(df.shape)
print(df.head())

