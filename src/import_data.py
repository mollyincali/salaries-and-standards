import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#---- SBAC DATA
# Drop * values, choose "all student" subgroup, disregard students > grade 11
# Look at entire district with School code 0
sbac = pd.read_csv("../data/sb_ca2019_all_csv_v4.txt")
sbac = sbac[sbac['Percentage Standard Met and Above'] != '*']
sbac = sbac[sbac['Subgroup ID'] == 1]
sbac = sbac[sbac['Grade'] <= 11]
sbac = sbac[sbac['School Code'] == 0]

# Converts string to float
sbac['Students Tested'] = sbac['Students Tested'].astype(float)
sbac['Met or Above'] = sbac['Percentage Standard Met and Above'].astype(float)

# Get desired df
sbac = sbac[['County Code', 'District Code', 'Grade', 
             'Test Id', 'Students Tested', 'Met or Above']].drop_duplicates()

#---- DISTRICT CODES
district = pd.read_csv("../data/districts.csv")
district = district[['County Code', 'County Name', 
                     'District Code', 'District Name']].drop_duplicates()

# Merge district and sbac
district_sbac = pd.merge(district, sbac, how = 'inner', on = 'District Code')


#---- TEACHER CODES
teacher = pd.read_csv("../data/salary.csv")
teacher["Avg Salary"] = teacher['Average Salary Paid'].str.replace(',','').astype(float)

# Change column name so we can merge with district_sbac table
teacher['District Name'] = teacher['LEA']
teacher = teacher.dropna()
teacher = teacher[['District Name', 'Avg Salary', 'Co']].drop_duplicates()

# Noticed not all District Names match up, trying to catch all
teacher2 = teacher.copy()
teacher2['District Name'] = teacher2['District Name'].str.replace(' Elementary', '')
teacher2['District Name'] = teacher2['District Name'].str.replace(' High', '')
teacher2['District Name'] = teacher2['District Name'].str.replace(' Elem.', '')

# Bring two df together
teacher = pd.concat([teacher, teacher2]).drop_duplicates()


#---- FULL & FINAL DATA FRAME 
full = pd.merge(district_sbac, teacher, how = 'inner', on = 'District Name')
full = full[['County Name', 'Co', 'District Name', 'District Code', 'Grade', 
            'Test Id', 'Students Tested', 'Met or Above', 'Avg Salary']].reset_index()

# Creating ELA and MATH df
fullela = full[full['Test Id'] == 1]
fullmath = full[full['Test Id'] == 2]