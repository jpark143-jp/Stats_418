import pandas as pd
import sqlite3 as sql
import os
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

# Setup
d = pd.read_csv("Problem Set 2 - movies.csv")
d = pd.DataFrame(d)
conn = sql.connect("movieratings.db")
d.to_sql("movieratings",conn)

## Answer 1

d['year'].value_counts().plot(kind='barh', figsize=(3, 10), rot=0)
plt.xlabel("Movie Count each year", labelpad=14)
plt.ylabel("Year", labelpad=14)
plt.title("Count of Year", y=1.02);

## Answer 2

x = d['year'].unique()
y = np.array(d_gby_year['rating'].mean())

mean = d_gby_year['rating'].mean()
std = d_gby_year['rating'].std()

plt.scatter(x, y)
plt.errorbar(mean.index, mean, xerr=0.5, yerr=2*std, linestyle='')

plt.xticks([5*r + 1920 for r in range(21)])
plt.yticks(list(range(1,10+1)))
plt.rcParams["figure.figsize"] = [10,2]
plt.axhline(y=mean.mean(), color='r', linestyle='--')
plt.show()
