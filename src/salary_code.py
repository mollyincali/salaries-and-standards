import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#---- TEACHER SALARY
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