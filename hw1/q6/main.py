import pandas as pd
import sqlite3 as sql
import os
from pathlib import Path

d = pd.read_csv("Problem Set 0 _ 1 - data.csv")
d = pd.DataFrame(d)
conn = sql.connect("tablejp.db")
d.to_sql("tablejp",conn)

# 4.1	Which store had the highest mean sale in 2017?
d['year'] = pd.DatetimeIndex(d['Date']).year
d_2017 = d[d['year']==2017]
d_2017.describe()

d_2017.mean(axis=0)

### Store2 has the highest mean sale in 2017

# 4.2 Which day showed the highest variance in sales across different stores?
dd = d.var(axis=1)
df = dd.to_frame().reset_index()
df[df.loc[:,0]==max(df.loc[:,0])]
d.iloc[293,0]

### 2017-10-21

# 4.3 Which year showed the highest median sale for the store S5?
d.loc[:,("S5","year")].median(axis=0)

### Year 2018

# 4.4 Which store recorded the highest number of sales for the largest number of days?
d_44 = d.iloc[:,1:10].idxmax(axis=1)
df = pd.DataFrame(d_44)
df.groupby(d_44).size()

### Store2 has the largest number of days with highest number of sales.

# 4.5	Which store ranks 5th in the cumulative number of units sold over the 3-year interval?
a = d.iloc[:,1:11].sum(axis=0)
Output = sorted(a, key = float)
Output
a

### S7 is the fifth ranked store.

# 4.6 Repaired.csv

column_medians = d.median()
d_repaired = d.fillna(column_medians)
  
filepath = Path('/Users/jpark143g.ucla.edu/Downloads/Stats_418/hw1/q4/repaired.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
d_repaired.to_csv(filepath)  