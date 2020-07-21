import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#ELA + Math all schools all district 2456071 rows
df = pd.read_csv("./data/sb_ca2019_all_csv_v4.txt")

#Drop high school scores
df = df[df['Grade'] < 9]

#clean sbac 2456071 rows
sbac = df.iloc[:, [0, 1, 2, 5, 9, 10, 12, 16]]
sbac = sbac[sbac['Percentage Standard Met and Above'] != '*']
sbac = sbac[sbac['Subgroup ID'] == 1]

#converts string to float
sbac['Students Tested'] = sbac['Students Tested'].astype(float)
sbac['Met or Above'] = sbac['Percentage Standard Met and Above'].astype(float)

#import districts and clean
district = pd.read_csv("./data/districts.csv")
district = district.iloc[:, [0, 1, 5, 6]]
district = district[district['District Code'] != 0]

#pull only top 10 county
top10_districts = district[(district['County Code'] == 19) | (district['County Code'] == 37) | (district['County Code'] == 30)
                | (district['County Code'] == 33) | (district['County Code'] == 36) | (district['County Code'] == 43)
                | (district['County Code'] == 1) | (district['County Code'] == 34) | (district['County Code'] == 7)
                | (district['County Code'] == 10)]

#import teacher salary and clean
teacher = pd.read_csv("./data/salary.csv")
teacher["avg"] = teacher['Average Salary Paid'].str.replace(',','').astype(float)
teacher['District Name'] = teacher['LEA']
teacher = teacher.dropna()

#pull only top 10 counties
salary_top10 = teacher[(teacher['Co'] == 19) | (teacher['Co'] == 37) | (teacher['Co'] == 30)
                | (teacher['Co'] == 33) | (teacher['Co'] == 36) | (teacher['Co'] == 43)
                | (teacher['Co'] == 1) | (teacher['Co'] == 34) | (teacher['Co'] == 7)
                | (teacher['Co'] == 10)]

salary_top10 = salary_top10.groupby("District Name").agg({'avg':'mean',
                                                'Co':'max'}).reset_index()

#merge in salary of those districts
salary_merge = top10_districts.merge(salary_top10, how = 'inner')

#bring together sbac and district look at only all student group 381548 rows
full = sbac.merge(salary_merge, how = 'inner')

#removes duplicates
full = full.drop_duplicates(subset=['County Code','District Code', 'School Code', 
                                'Subgroup ID', 'Grade', 'Test Id', 'Students Tested', 
                                'Met or Above'], keep="first", inplace=False)
full = full[full['School Code'] == 0]