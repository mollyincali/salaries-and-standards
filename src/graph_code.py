import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

fonttitle = {'fontname':'Helvetica', 'fontsize':25}
fontaxis = {'fontname':'Helvetica', 'fontsize':18}
blue_color = '#1f788b4'
green_color = '#b2df8a'
purple_color = '#8da0cb'

#README Graph 1: Highest Avg Teacher Salary by County Graph
salary_graph = full.groupby('County Name').agg({'Avg Salary':'max'})\
                    .reset_index()\
                    .sort_values(by='Avg Salary')\
                    .rename(columns={"Avg Salary": "Max Salary"})

fig, ax = plt.subplots(figsize= (18,9))
ax.bar(salary_graph['County Name'], salary_graph['Max Salary'], color = '#b2df8a')
ax.set_ylabel('Highest Average Salary', fontdict=fontaxis)
ax.set_xlabel("County Name", fontdict=fontaxis)
ax.axhline(np.median(salary_graph['Max Salary']), linestyle ='--', linewidth=6, color = '#8da0cb')
plt.xticks(rotation=90)
plt.ylim(40000, 120000)
plt.title('Highest Average Teacher Salary in the County', fontdict=fonttitle)
plt.show();


#----   README Graph 2: Scatter Salary vs Met for ALL
fig, ax = plt.subplots(figsize= (18,9))
ax.scatter(full['Avg Salary'], full['Met or Above'], color = '#8da0cb', alpha = 0.3)
plt.title('Does Higher Pay Create Success?', fontdict=fonttitle)
ax.set_ylabel('All Students Who Met or Exceeded Standard', fontdict=fontaxis)
ax.set_xlabel("Average Teacher Salary by District", fontdict=fontaxis)
fig.tight_layout
plt.show();


#----   README Graph 3: Scatter Salary vs Met by District
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
ax[0].set_title(f'Percentage of students \n proficient or higher \n in Math by District', fontdict=fonttitle)
ax[0].set_xlabel("Percent of Students", fontdict=fontaxis)
ax[0].set_ylabel("Number of Students", fontdict=fontaxis);

ax[1].hist(bottomela, alpha = .8, bins = 70, color = purple_color, label = 'Bottom paying districts')
ax[1].hist(topela, alpha = .6, bins = 70, color = green_color, label = 'Top paying districts')
ax[1].legend(loc="upper left")
ax[1].set_title(f'Percentage of students \n proficient or higher \n in ELA by District', fontdict=fonttitle)
ax[1].set_xlabel("Percent of Students", fontdict=fontaxis)
ax[1].set_ylabel("Number of Students", fontdict=fontaxis);


#----   README GRAPH 5 cdfs:





#---    CHECK OUT?!
for i in range(1, 59):
        temp_df = full.groupby('Co').agg({'Avg Salary':'mean', 'Met or Above':'mean'}).sort_values(by='Avg Salary')
        plt.scatter(temp_df['Avg Salary'], temp_df['Met or Above'])
        plt.title(i)
        plt.show()
"""
THROW AWAY CODE
#Correlation full avg and met or above
temp_df = full[['avg','Met or Above']]
corrMatrix = temp_df.corr()
sns.heatmap(corrMatrix, annot=True, vmin=-0.85, vmax=0.85, cmap='PRGn');
#------------------
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
#------------------
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