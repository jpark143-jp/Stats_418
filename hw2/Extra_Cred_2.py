# Plotly

import plotly.express as px


# First plot

fig = px.bar(d['year'].value_counts())
fig.show()

# Second plot

import numpy as np
import math

mean = d_gby_year['rating'].mean()
std = d_gby_year['rating'].std()
errory = 1.96/math.sqrt(84)

fig.add_scatter(x=d['year'].unique(), y=np.array(d_gby_year['rating'].mean()),
                 mode='makers', error_y= errory)
fig.show()
