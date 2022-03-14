import pandas as pd
import sqlite3 as sql
import os
from pathlib import Path

d = pd.read_csv("Problem Set 2 - movies.csv")
d = pd.DataFrame(d)
conn = sql.connect("movieratings.db")
d.to_sql("movieratings",conn)
