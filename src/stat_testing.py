import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#p value ELA = 5.4839 e-64
topela = fullela[fullela['Avg Salary'] > fullela['Avg Salary'].median()]['Met or Above']
bottomela = fullela[fullela['Avg Salary'] <= fullela['Avg Salary'].median()]['Met or Above']
stats.ttest_ind(topela, bottomela)

#p value MATH = 1.4068 e-60
topmath = fullmath[fullmath['Avg Salary'] > fullmath['Avg Salary'].median()]['Met or Above']
bottommath = fullmath[fullmath['Avg Salary'] <= fullmath['Avg Salary'].median()]['Met or Above']
stats.ttest_ind(topmath, bottommath)