import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

from import_data import *

#FROM LAND
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
stats.ttest_ind(test_topmath, test_bottommath)

#HIST from LAND
fig, ax = plt.subplots(figsize = (10, 8))
plt.hist(topela, alpha = .6, bins = 75, color = '#1f788bff')
plt.hist(bottomela, alpha = .8, bins = 75, color = '#b2df8a');

fig, ax = plt.subplots(figsize = (10, 8))
plt.hist(topmath, alpha = .9, bins = 75, color = '#b2df8a')
plt.hist(bottommath, alpha = .5, bins = 75, color = '#1f788bff');


#LAND test
def cdf(value, array):
    return (array<value).sum()/len(array)

vcdf = np.vectorize(cdf, excluded = ['array'])
top_cdf = vcdf(value = topela, array = topela)
bottom_cdf = vcdf(value = bottomela, array = bottomela)
plt.scatter(topela, top_cdf, marker = '.', color = '#1f788bff')
plt.scatter(bottomela, bottom_cdf, marker = '.', color = '#b2df8a')
plt.show();

print(topela.mean(), bottomela.mean())

#MY data
def cdf(value, array):
    return (array<value).sum()/len(array)

vcdf = np.vectorize(cdf, excluded = ['array'])

testtop_cdf = vcdf(value = test_topela, array = test_topela)
testbot_cdf = vcdf(value = test_bottomela, array = test_bottomela)

plt.scatter(test_topela, testtop_cdf, marker = 'o', color = '#1f788bff')
plt.scatter(test_bottomela, testbot_cdf, marker = 'o', color = '#b2df8a')
plt.show();

print(test_topela.mean(), test_bottomela.mean())