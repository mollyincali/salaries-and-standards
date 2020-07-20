import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#ELA + Math all schools all district
df = pd.read_csv("sb_ca2019_all_csv_v4.txt")

#Drop high school scores
df = df[df['Grade'] < 9]

#new df with wanted columns 2456071 rows
sbac = df.iloc[:, [0, 1, 2, 5, 9, 10, 12, 16]]

#remove unwanted *
sbac = sbac[sbac['Percentage Standard Met and Above'] != '*']
#look at just "all student"
sbac = sbac[sbac['Subgroup ID'] == 1]

#converts string to float
sbac['Students Tested'] = sbac['Students Tested'].astype(float)
sbac['Percentage Standard Met and Above'] = sbac['Percentage Standard Met and Above'].astype(float)

#import districts
district_code = pd.read_csv("districts.csv")
district = district.iloc[:, [0, 1, 5, 6]]

#pull only top 10 county
top10 = district[(district['County Code'] == 18) | (district['County Code'] == 36) | (district['County Code'] == 29)
                | (district['County Code'] == 32) | (district['County Code'] == 35) | (district['County Code'] == 43)
                | (district['County Code'] == 1) | (district['County Code'] == 33) | (district['County Code'] == 6)
                | (district['County Code'] == 9)]
top10 = top10[top10['District Code'] != 0]
#or top10 = top10.drop(top10[top10['District Code'] == 0].index)

#bring together sbac and district look at only all student group 381548 rows
full = sbac.merge(top10, how = 'inner')
full = full[full['Subgroup ID'] == 1]

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