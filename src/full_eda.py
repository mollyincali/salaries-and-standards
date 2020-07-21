import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#---- SBAC DATA
#ELA + Math all schools all district
sbac = pd.read_csv("../data/sb_ca2019_all_csv_v4.txt")
#clean sbac 2456071 rows
sbac = sbac[sbac['Percentage Standard Met and Above'] != '*']
sbac = sbac[sbac['Subgroup ID'] == 1]
sbac = sbac[sbac['Grade'] <= 11]

#converts string to float
sbac['Students Tested'] = sbac['Students Tested'].astype(float)
sbac['Met or Above'] = sbac['Percentage Standard Met and Above'].astype(float)
sbac = sbac.iloc[:, [0, 1, 2, 5, 9, 10, 12, 32]] 


#---- DISTRICT CODES
#import districts and clean
district = pd.read_csv("../data/districts.csv") 
district = district.iloc[:, [0, 1, 5, 6]] 
#merge district and sbac to get names
district_sbac = pd.merge(sbac, district, how = 'inner')


#---- TEACHER SALARY
#import teacher salary and clean
teacher = pd.read_csv("../data/salary.csv")
teacher["avg"] = teacher['Average Salary Paid'].str.replace(',','').astype(float)
teacher['District Name'] = teacher['LEA']
teacher = teacher.dropna()
teacher = teacher.iloc[:,[0, 12, 13]] 


#---- CREATE DESIRED DF
full = pd.merge(district_sbac, teacher, how = 'inner')
full = full[full['School Code'] == 0]
full = full.drop_duplicates(subset=['County Code','District Code', 'School Code', 
                                'Subgroup ID', 'Grade', 'Test Id', 'Students Tested', 
                                'Met or Above'], keep="first", inplace=False)