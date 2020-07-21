import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#ELA + Math all schools all district
df = pd.read_csv("./data/sb_ca2019_all_csv_v4.txt")

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
district = pd.read_csv("./data/districts.csv")
district = district.iloc[:, [0, 1, 5, 6]]

#import teacher salary and clean
teacher = pd.read_csv("./data/salary.csv")

teacher["avg"] = teacher['Average Salary Paid'].str.replace(',','')
teacher["avg"] = teacher["avg"].astype(float)

#pull only top 10 counties
top10 = teacher[(teacher['Co'] == 19) | (teacher['Co'] == 37) | (teacher['Co'] == 30)
                | (teacher['Co'] == 33) | (teacher['Co'] == 36) | (teacher['Co'] == 43)
                | (teacher['Co'] == 1) | (teacher['Co'] == 34) | (teacher['Co'] == 7)
                | (teacher['Co'] == 10)]

by_lea_top10 = teacher.groupby("LEA").agg({'avg':'mean',
                                        'Co':'max'}).reset_index()
by_lea_top10['District Name'] = by_lea_top10['LEA']
by_lea_top10 = by_lea_top10.dropna()

#pull only top 10 county
top10 = district[(district['County Code'] == 19) | (district['County Code'] == 37) | (district['County Code'] == 30)
                | (district['County Code'] == 33) | (district['County Code'] == 36) | (district['County Code'] == 43)
                | (district['County Code'] == 1) | (district['County Code'] == 34) | (district['County Code'] == 7)
                | (district['County Code'] == 10)]
top10 = top10[top10['District Code'] != 0]

#merge in salary of those districts
top10_salary = top10.merge(by_lea_top10, how = 'inner')
top10_salary = top10_salary.iloc[:,[0,1,2,3,5]]

#bring together sbac and district look at only all student group 381548 rows
full = sbac.merge(top10_salary, how = 'inner')
full = full[full['Subgroup ID'] == 1]

# Going to functionize below
# #look at grade 3 ELA and math
# full3ela = full[(full['Grade'] == 3) & (full['Test Id'] == 1)] 
# full3math = full[(full['Grade'] == 3) & (full['Test Id'] == 2)]

# #notice duplicated, drop them
# full3ela = full3ela.drop_duplicates(subset=['County Code','District Code', 'School Code', 
#                                 'Subgroup ID', 'Grade', 'Test Id', 'Students Tested', 
#                                 'Percentage Standard Met and Above'], keep="first", inplace=False)

# full3math = full3math.drop_duplicates(subset=['County Code','District Code', 'School Code', 
#                                 'Subgroup ID', 'Grade', 'Test Id', 'Students Tested', 
#                                 'Percentage Standard Met and Above'], keep="first", inplace=False)

# #grade 3 grouped by county and district
# full3ela = full3ela.groupby(['County Code', 'District Name']).agg({'Students Tested':'sum',
#                                             'avg':'max', 
#                                             'Grade':'max',
#                                             'Percentage Standard Met and Above': 'mean'}).reset_index()

# full3math = full3math.groupby(['County Code', 'District Name']).agg({'Students Tested':'sum',
#                                             'avg':'max', 
#                                             'Grade':'max',
#                                             'Percentage Standard Met and Above': 'mean'}).reset_index()