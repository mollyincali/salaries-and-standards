import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import folium

from import_data import *

fonttitle = {'fontname':'Helvetica', 'fontsize':25}
fontaxis = {'fontname':'Helvetica', 'fontsize':18}
blue_color = '#1f788bff'
green_color = '#b2df8a'
purple_color = '#8da0cb'

#README Graph 1: Highest Avg Teacher Salary by County
salary_graph = full.groupby('County Name').agg({'Avg Salary':'max'})\
                    .reset_index()\
                    .sort_values(by='Avg Salary')\
                    .rename(columns={"Avg Salary": "Max Salary"})

fig, ax = plt.subplots(figsize= (18,9))
ax.bar(salary_graph['County Name'], salary_graph['Max Salary'], color = blue_color)
ax.set_ylabel('Highest Average Salary', fontdict=fontaxis)
ax.set_xlabel("County Name", fontdict=fontaxis)
ax.axhline(np.median(salary_graph['Max Salary']), linestyle ='--', linewidth=6, color = purple_color)
plt.xticks(rotation=90)
plt.ylim(40000, 120000)
plt.title('Highest Average Teacher Salary in the County', fontdict=fonttitle)
plt.show();


#----   README Graph 2: Scatter ALL Salary vs ALL Met
fig, ax = plt.subplots(figsize= (18,9))
ax.scatter(full['Avg Salary'], full['Met or Above'], color = blue_color, alpha = 0.3)
plt.title('Does Higher Pay Create Success?', fontdict=fonttitle)
ax.set_ylabel('All Students Who Met or Exceeded Standard', fontdict=fontaxis)
ax.set_xlabel("Average Teacher Salary by District", fontdict=fontaxis)
fig.tight_layout
plt.show();


#----   README Graph 3: Scatter District Salary vs All Met
graph = full.groupby('District Name').agg({'Avg Salary':'max', 'Met or Above':'mean'})
fig, ax = plt.subplots(figsize= (18,9))
ax.scatter(graph['Avg Salary'], graph['Met or Above'], color = blue_color, marker ='D')
plt.title('Does Higher Pay Create Success?', fontdict=fonttitle)
ax.set_ylabel('All Students Who Met or Exceeded Standard', fontdict=fontaxis)
ax.set_xlabel("Average Teacher Salary by District", fontdict=fontaxis)
fig.tight_layout
plt.show();


#----   README GRAPH 4 histograms:
fig, ax = plt.subplots(1, 2, figsize = (15, 9))

ax[0].hist(bottommath, alpha = .8, bins = 70, color = purple_color, label = 'Bottom paying districts')
ax[0].hist(topmath, alpha = .6, bins = 70, color = green_color, label = 'Top paying districts')
ax[0].legend(loc="upper left")
ax[0].set_title(f'Percentage of students \n proficient or higher \n in {test1} by District', fontdict=fonttitle)
ax[0].set_xlabel("Percent of Students", fontdict=fontaxis)
ax[0].set_ylabel("Number of Students", fontdict=fontaxis);

ax[1].hist(bottomela, alpha = .8, bins = 70, color = purple_color, label = 'Bottom paying districts')
ax[1].hist(topela, alpha = .6, bins = 70, color = green_color, label = 'Top paying districts')
ax[1].legend(loc="upper left")
ax[1].set_title(f'Percentage of students \n proficient or higher \n in {test2} by District', fontdict=fonttitle)
ax[1].set_xlabel("Percent of Students", fontdict=fontaxis)
ax[1].set_ylabel("Number of Students", fontdict=fontaxis)
plt.show();


#----   README GRAPH 5 cdfs:
#Both ELA and Math
make_cdf(topela, bottomela, 'ELA', topmath, bottommath, 'Math')

#----   README GRAPH 6 Correlation Maps:
#Math
make_heatmap(fullmath, 'Math')

#ELA
make_heatmap(fullela, 'ELA')