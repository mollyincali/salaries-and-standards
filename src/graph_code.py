import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from full_eda import *

#graph grade 3 ela and math
x = full3ela['District Name']
y = full3ela['Percentage Standard Met and Above']
y2 = full3math['Percentage Standard Met and Above']

fig, ax = plt.subplots(figsize = (10, 6))
plt.xticks(rotation=90)
ax.scatter(x, y, color = 'green')
ax.scatter(x, y2, color = 'pink');

#graph salary
x = full3ela['District Name']
y2 = full3ela['avg']

fig, ax = plt.subplots(figsize = (10, 6))
plt.xticks(rotation=90)
ax.bar(x, y2, color = 'blue');

# BELOW need to work on transparency
x = full3ela['District Name']
data1 = full3ela['Percentage Standard Met and Above']
data2 = full3math['Percentage Standard Met and Above']
salary = full3ela['avg']

fig, ax1 = plt.subplots(figsize=(18,9))

color = 'tab:red'
ax1.set_xlabel('District')
ax1.set_ylabel('Percentage Met or Above', color=color)
ax1.scatter(x, data1, color=color)
ax1.scatter(x, data2, color = 'blue')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:green'
ax2.set_ylabel('Salary', color=color) 
ax2.bar(x, salary, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()