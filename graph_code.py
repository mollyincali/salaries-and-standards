import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import eda_code 

#by district name and graph
by_district3ela = full3ela.groupby(['District Name']).agg({'Students Tested':'sum', 
                                                    'Percentage Standard Met and Above': 'mean'}).reset_index()
x = by_district3ela['District Name']
y = by_district3ela['Percentage Standard Met and Above']
fig, ax = plt.subplots(figsize = (18, 9))
plt.xticks(rotation=90)
ax.scatter(x, y, color = 'green');

#by county and graph
by_county3ela = full3ela.groupby(['County Name']).agg({'Students Tested':'sum', 
                                                    'Percentage Standard Met and Above': 'mean'}).reset_index()
x = by_county3ela['County Name']
y = by_county3ela['Percentage Standard Met and Above']
fig, ax = plt.subplots(figsize = (10, 6))
plt.xticks(rotation=90)
ax.scatter(x, y, color = 'green');