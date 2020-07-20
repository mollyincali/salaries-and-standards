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