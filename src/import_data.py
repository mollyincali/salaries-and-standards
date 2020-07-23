import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import scipy.stats as stats

#---- SBAC DATA
#Import all schools all district and clean
sbac = pd.read_csv("./data/sb_ca2019_all_csv_v4.txt").set_index('District Code')
sbac = sbac[sbac['Percentage Standard Met and Above'] != '*']
sbac = sbac[sbac['Subgroup ID'] == 1]
sbac = sbac[sbac['Grade'] <= 11]

#When school code == 0 shares report for entire district
sbac = sbac[sbac['School Code'] == 0]

#converts string to float
sbac['Students Tested'] = sbac['Students Tested'].astype(float)
sbac['Met or Above'] = sbac['Percentage Standard Met and Above'].astype(float)
sbac = sbac[['County Code', 'Grade', 'Test Id', 'Students Tested', 'Met or Above', 'Number Proficient']].drop_duplicates()


#---- DISTRICT CODES
#import districts and clean
district = pd.read_csv("./data/districts.csv").set_index('District Code')
district = district[['County Code', 'County Name', 'District Name']].drop_duplicates()

#merge district and sbac to get names
district_sbac = district.join(sbac, lsuffix = '_district', how = 'inner')


#---- TEACHER CODES
teacher = pd.read_csv("./data/salary.csv")
teacher["Avg Salary"] = teacher['Average Salary Paid'].str.replace(',','').astype(float)
teacher['District Name'] = teacher['LEA']
teacher = teacher.dropna()
teacher = teacher[['District Name', 'Avg Salary', 'Co']].drop_duplicates()

#Noticed not all District Names match up, trying to catch all
teacher2 = teacher.copy()
teacher2['District Name'] = teacher2['District Name'].str.replace(' Elementary', '')
teacher2['District Name'] = teacher2['District Name'].str.replace(' High', '')
teacher2['District Name'] = teacher2['District Name'].str.replace(' Elem.', '')

#Bring two df together
teacher = pd.concat([teacher, teacher2]).drop_duplicates().set_index(['District Name'])


#---- FULL & FINAL DATA FRAME
full = district_sbac.reset_index().set_index('District Name').join(teacher, how = 'inner')
full = full[['District Code', 'County Name', 'Grade', 
            'Test Id', 'Students Tested', 'Met or Above', 'Number Proficient', 'Avg Salary', 'Co']].reset_index()