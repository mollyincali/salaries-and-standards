import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

#README Graph 1: Teacher Salary Graph
salary_graph = full.groupby('County Name').agg({'Avg Salary':'max'})\
                    .reset_index()\
                    .sort_values(by='Avg Salary')\
                    .rename(columns={"Avg Salary": "Max Salary"})

fontdict = {'fontname':'Helvetica', 'fontsize':20}

fig, ax = plt.subplots(figsize= (18,9))
ax.bar(salary_graph['County Name'], salary_graph['Max Salary'], color = '#b2df8a')
ax.set_ylabel('Max Salary', fontdict=fontdict)
ax.set_xlabel("County Name", fontdict=fontdict)
ax.axhline(82746, linestyle ='--', linewidth=6, color = '#8da0cb')

plt.xticks(rotation=90)
plt.ylim(40000, 120000)
plt.title('Max Teacher Salary in the County', fontdict=fontdict)
plt.show();

#----   README Graph 2: Scatter Salary vs Met
fontdict = {'fontname':'Helvetica', 'fontsize':20}
fig, ax = plt.subplots(figsize= (18,9))
ax.scatter(full['avg'], full['Met or Above'], color = '#8da0cb')
plt.title('Does Higher Pay Equal Better Success?', fontdict=fontdict)
ax.set_ylabel('Students Who Met or Exceeded Standard', fontdict=fontdict)
ax.set_xlabel("Average Teacher Salary", fontdict=fontdict)
fig.tight_layout
plt.show();


#----   README Graph 3: Scatter Salary GROUPED by County vs Met
by_county = full.groupby('Co').agg({'Met or Above':'mean', 'avg':'mean'}).reset_index()
fig, ax = plt.subplots(figsize= (18,9))
ax.scatter(by_county['avg'], by_county['Met or Above'], color = '#1f788bff', marker ='D')
plt.title('Does Higher Pay Equal Better Success?', fontdict=fontdict)
ax.set_ylabel('Students Who Met or Exceeded Standard', fontdict=fontdict)
ax.set_xlabel("Average Teacher Salary Grouped by County", fontdict=fontdict)
fig.tight_layout
plt.show();

#----   README GRAPH 4:
#Correlation full avg and met or above
temp_df = full[['avg','Met or Above']]
corrMatrix = temp_df.corr()
sns.heatmap(corrMatrix, annot=True, vmin=-0.85, vmax=0.85, cmap='PRGn');




"""
THROW AWAY CODE
##Attempt at side by side plot and salary
sc_math = fullmath[fullmath['County Code'] == 43].sort_values(['avg'])
sc_ela = fullela[fullela['County Code'] == 43].sort_values(['avg'])

x = sc_math['District Name']
data1 = sc_math['Met or Above']
data2 = sc_ela['Met or Above']
salary = sc_ela['avg']

fig, ax1 = plt.subplots(figsize=(18,9))

color = 'tab:red'
ax1.set_xlabel('District')
plt.xticks(rotation=60)
ax1.set_ylabel('Percentage Met or Above', color=color)
ax1.bar(x, data1, color = color)
ax1.bar(x, data2, color = 'blue')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 

color = 'tab:green'
ax2.set_ylabel('Salary', color=color)
ax2.scatter(x, salary, color=color, zorder=1)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout() 
plt.show()
"""
#------------------
"""
## Graph with bar chart of salary and dots of % proficient NOT GOOD
sc_3math = full3math[full3math['County Code'] == 43].sort_values(['avg'])
sc_3ela = full3ela[full3ela['County Code'] == 43].sort_values(['avg'])

x = sc_3math['District Name']
data1 = sc_3math['Met or Above']
data2 = sc_3ela['Met or Above']
salary = sc_3ela['avg']

fig, ax1 = plt.subplots(figsize=(18,9))

color = 'tab:red'
ax1.set_xlabel('District')
plt.xticks(rotation=60)
ax1.set_ylabel('Percentage Met or Above', color=color)
ax1.scatter(x, data1, color = color)
ax1.scatter(x, data2, color = 'blue')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 

color = 'tab:green'
ax2.set_ylabel('Salary', color=color)
ax2.bar(x, salary, color=color, edgecolor = 'None', alpha = 0.5)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout() 
plt.show()
"""