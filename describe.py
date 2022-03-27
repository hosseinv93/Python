#describe a value based on one or more groups of other values
from glob import glob
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import os
import pandas as pd
import subprocess

data=np.loadtxt("your data")

df = pd.DataFrame({'X': data[:,1], 'Y': data[:,2], 'Z': data[:,3]})

bins_x=np.arange(-20,20,0.2)
bins_y=np.arange(-20,20,0.2)

df['TX'] = pd.cut(df['X'],bins=bins_x)
df['TY'] = pd.cut(df['Y'],bins=bins_y)

df_out = df.groupby(['TX','TY'])['Z'].describe()
idx = pd.MultiIndex.from_product((df_out.index.levels[0],df_out.index.levels[1]))
df_out = df_out.reindex(idx,fill_value=0)

print(df_out)
df_out.to_csv ('out_2d.csv', header=True)
