import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#ELA + Math all schools all district
df = pd.read_csv("sb_ca2019_all_csv_v4.txt")

#Drop high school scores
df = df[df['Grade'] < 9]

#new df with wanted columns 2456071 rows
sbac = df.iloc[:, [0, 1, 2, 5, 6, 9, 10, 12, 16]]

#removes * 1273325 rows
sbac = sbac[sbac['Percentage Standard Met and Above'] != '*']
#converts string to float
sbac['Percentage Standard Met and Above'] = sbac['Percentage Standard Met and Above'].astype(float)

#import districts
district_code = pd.read_csv("districts.csv")

#bring together sbac and district 
full = sbac.merge(district_code, how = 'inner')

#pull only top 10 county
top10 = full[(full['County Code'] == 18) | (full['County Code'] == 36) | (full['County Code'] == 29)
                | (full['County Code'] == 32) | (full['County Code'] == 35) | (full['County Code'] == 43)
                | (full['County Code'] == 1) | (full['County Code'] == 33) | (full['County Code'] == 6)
                | (full['County Code'] == 9)]

#Drop district code 0, county office scores 264158 rows
top10 = top10[top10['District Code'] != 0]
#or top10 = top10.drop(top10[top10['District Code'] == 0].index)

#Look at subgroup 'all students' in top10 12508 rows
top10all = top10[top10['Subgroup ID'] == 1]

#Below worked! Look over again
group_test = top10all.groupby(['District Code', 'Grade']).agg({'Students Tested':'sum', 
                                                               'Percentage Standard Met and Above': 'mean', 
                                                               'County Name':'unique',
                                                               'District Name':'unique',
                                                               'School Name':'unique'}).reset_index()

#graph, CAN I COLOR BY COUNTY?
x = group_test['Grade']
y = group_test['Percentage Standard Met and Above']
fig, ax = plt.subplots(figsize = (18, 9))

ax.scatter(x, y);