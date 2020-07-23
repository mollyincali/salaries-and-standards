import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import seaborn as sn
import scipy.stats as stats

fonttitle = {'fontname':'Helvetica', 'fontsize':25}
fontaxis = {'fontname':'Helvetica', 'fontsize':18}
blue_color = '#1f788b4'
green_color = '#b2df8a'
purple_color = '#8da0cb'

#p value ELA = 5.4839 e-64
topela = fullela[fullela['Avg Salary'] > fullela['Avg Salary'].median()]['Met or Above']
bottomela = fullela[fullela['Avg Salary'] <= fullela['Avg Salary'].median()]['Met or Above']
stats.ttest_ind(topela, bottomela)

#p value MATH = 1.4068 e-60
topmath = fullmath[fullmath['Avg Salary'] > fullmath['Avg Salary'].median()]['Met or Above']
bottommath = fullmath[fullmath['Avg Salary'] <= fullmath['Avg Salary'].median()]['Met or Above']
stats.ttest_ind(topmath, bottommath)

#HIST ELA
fig, ax = plt.subplots(figsize = (10, 8))
plt.hist(topela, alpha = .6, bins = 75, color = blue_color)
plt.hist(bottomela, alpha = .8, bins = 75, color = green_color);

#HIST Math
fig, ax = plt.subplots(figsize = (10, 8))
plt.hist(topmath, alpha = .9, bins = 75, color = blue_color)
plt.hist(bottommath, alpha = .5, bins = 75, color = green_color);

#CDF Graph
def cdf(value, array):
    return (array<value).sum()/len(array)

vcdf = np.vectorize(cdf, excluded = ['array'])
etop_cdf = vcdf(value = topela, array = topela)
ebottom_cdf = vcdf(value = bottomela, array = bottomela)
plt.scatter(topela, etop_cdf, marker = '.', color = blue_color)
plt.scatter(bottomela, ebottom_cdf, marker = '.', color = green_color)
plt.show();

vcdf = np.vectorize(cdf, excluded = ['array'])
mtop_cdf = vcdf(value = topmath, array = topmath)
mbottom_cdf = vcdf(value = bottommath, array = bottommath)
plt.scatter(topmath, mtop_cdf, marker = '.', color = blue_color)
plt.scatter(bottommath, mbottom_cdf, marker = '.', color = green_color)
plt.show();



#---- THROW AWAY
"""#FROM LAND
topela = fullela[fullela['Avg Salary'] > fullela['Avg Salary'].mean()]['Met or Above']
bottomela = fullela[fullela['Avg Salary'] <= fullela['Avg Salary'].mean()]['Met or Above']
stats.ttest_ind(topela, bottomela)

#FROM LAND
topmath = fullmath[fullmath['Avg Salary'] > fullmath['Avg Salary'].mean()]['Met or Above']
bottommath = fullmath[fullmath['Avg Salary'] <= fullmath['Avg Salary'].mean()]['Met or Above']
stats.ttest_ind(topmath, bottommath)

#---- Ran another versions CHECK WITH INSTRUCTOR 
#NEW df grouped by Co
test_ela = fullela.groupby("Co").agg({'Avg Salary':'mean', 'Students Prof':'sum', 'Students Tested':'sum'})
test_ela['Percent Prof'] = test_ela['Students Prof'] / test_ela['Students Tested']

#ELA testing group by county with avg of avg salary then avg, and actual prof avg p = 0.0058
test_topela = test_ela[test_ela['Avg Salary'] > test_ela['Avg Salary'].mean()]['Percent Prof']
test_bottomela = test_ela[test_ela['Avg Salary'] <= test_ela['Avg Salary'].mean()]['Percent Prof']
stats.ttest_ind(test_topela, test_bottomela)

#NEW df grouped by Co
test_math = fullmath.groupby("Co").agg({'Avg Salary':'mean', 'Students Prof':'sum', 'Students Tested':'sum'})
test_math['Percent Prof'] = test_math['Students Prof'] / test_math['Students Tested']

#Math testing group by county with avg of avg salary p = 0.02
test_topmath = test_math[test_math['Avg Salary'] > test_math['Avg Salary'].mean()]['Percent Prof']
test_bottommath = test_math[test_math['Avg Salary'] <= test_math['Avg Salary'].mean()]['Percent Prof']
stats.ttest_ind(test_topmath, test_bottommath)"""