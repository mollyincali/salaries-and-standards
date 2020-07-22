import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



#README Graph 1: Teacher Salary Graph
salary_county = full.groupby('County Name').agg({'avg':'mean'}).reset_index().sort_values(by='avg')
fontdict = {'fontname':'Helvetica', 'fontsize':20}

fig, ax = plt.subplots(figsize= (18,9))
ax.bar(salary_county['County Name'], salary_county['avg'], color = 'pink')
ax.set_ylabel('Salary', fontdict=fontdict)
ax.axhline(72590, linestyle ='--', color = 'purple')

plt.xticks(rotation=90)
plt.ylim(40000, 95000)
plt.title('Average Teacher Salary By County', fontdict=fontdict)
plt.show();

#----   README Graph 2: Scatter Salary %ELA


#----   README Graph 3: Scatter Salary %Math



#----   README GRAPH 4: Correlation map options below: 
#correlation all of ela and math
corrMatrix = (fullela.iloc[:, [7, 11]]).corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()

corrMatrix = (fullmath.iloc[:, [7, 11]]).corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()

#COORELATION DATA all counties
corr_list = []
for i in range(1, 59):
    try:
        temp_df = fullela[fullela['County Code'] == i][['avg','Met or Above']]
        corrMatrix = temp_df.corr()
        corr_list.append(corrMatrix.iloc[0, 1])
        sn.heatmap(corrMatrix, annot=True)
        plt.title(i)
        plt.show()
    except:
        print("Bummer!!")

#make a PD series of county num and correlation
corr_series = pd.Series(corr_list, index = range(1,59)).sort_values()

#Look at top 5 and bottom 5: [20, 53, 44, 11, 25, 48, 42, 43, 31, 41]:



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