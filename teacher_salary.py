import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

teacher = pd.read_csv("salary.csv")

teacher["avg"] = teacher['Average Salary Paid'].str.replace(',.','')
teacher['lowest'] = teacher['Lowest Scheduled Salary Offered'].str.replace(',.','')

teacher['avg'] = teacher['avg'].astype(float)
teacher['lowest'] = teacher['lowest'].astype(float)

top10 = teacher[(teacher['Co'] == 18) | (teacher['Co'] == 36) | (teacher['Co'] == 29)
                | (teacher['Co'] == 32) | (teacher['Co'] == 35) | (teacher['Co'] == 43)
                | (teacher['Co'] == 1) | (teacher['Co'] == 33) | (teacher['Co'] == 6)
                | (teacher['Co'] == 9)]

by_county_top10 = top10.groupby("Co").agg({'avg':'mean',
                                    'lowest':'mean',
                                    'LEA':'unique'}).reset_index()

by_lea_top10 = teacher.groupby("LEA").agg({'avg':'mean',
                                        'lowest':'mean',
                                        'Co':'unique'}).reset_index()