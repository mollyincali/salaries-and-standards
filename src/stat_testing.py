import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#FROM LAND
topela = fullela[fullela['Avg Salary'] > fullela['Avg Salary'].mean()]['Met or Above']
bottomela = fullela[fullela['Avg Salary'] <= fullela['Avg Salary'].mean()]['Met or Above']
stats.ttest_ind(topela, bottomela)

#FROM LAND
topmath = fullmath[fullmath['Avg Salary'] > fullmath['Avg Salary'].mean()]['Met or Above']
bottommath = fullmath[fullmath['Avg Salary'] <= fullmath['Avg Salary'].mean()]['Met or Above']
stats.ttest_ind(topmath, bottommath)

#---- Ran two other versions CHECK WITH INSTRUCTOR 
#ELA testing group by county with avg of avg salary then avg, and actual prof avg p = 0.0058
test_ela = fullela.groupby("Co").agg({'Avg Salary':'mean', 'Students Prof':'sum', 'Students Tested':'sum'})
test_ela['Percent Prof'] = test_ela['Students Prof'] / test_ela['Students Tested']
test_ela.head()

test_topela = test_ela[test_ela['Avg Salary'] > test_ela['Avg Salary'].mean()]['Percent Prof']
test_bottomela = test_ela[test_ela['Avg Salary'] <= test_ela['Avg Salary'].mean()]['Percent Prof']
stats.ttest_ind(test_topela, test_bottomela)

#ELA testing group by county with max of avg salary p = 0.001
test_ela2 = fullela.groupby("Co").agg({'Avg Salary':'max', 'Students Prof':'sum', 'Students Tested':'sum'})
test_ela2['Percent Prof'] = test_ela2['Students Prof'] / test_ela2['Students Tested']
test_ela2.head()

test2_topela = test_ela2[test_ela2['Avg Salary'] > test_ela2['Avg Salary'].mean()]['Percent Prof']
test2_bottomela = test_ela2[test_ela2['Avg Salary'] <= test_ela2['Avg Salary'].mean()]['Percent Prof']
stats.ttest_ind(test2_topela, test2_bottomela)

#Math testing group by county with avg of avg salary p = 0.02
test_math = fullmath.groupby("Co").agg({'Avg Salary':'mean', 'Students Prof':'sum', 'Students Tested':'sum'})
test_math['Percent Prof'] = test_math['Students Prof'] / test_math['Students Tested']
test_math.head()

test_topmath = test_math[test_math['Avg Salary'] > test_math['Avg Salary'].mean()]['Percent Prof']
test_bottommath = test_math[test_math['Avg Salary'] <= test_math['Avg Salary'].mean()]['Percent Prof']
stats.ttest_ind(test_topmath, test_bottommath)

#Math testing group by county with max of avg salary p = 0.03
test_math2 = fullmath.groupby("Co").agg({'Avg Salary':'max', 'Students Prof':'sum', 'Students Tested':'sum'})
test_math2['Percent Prof'] = test_math2['Students Prof'] / test_math2['Students Tested']
test_math2.head()

test2_topmath = test_math2[test_math2['Avg Salary'] > test_math2['Avg Salary'].mean()]['Percent Prof']
test2_bottommath = test_math2[test_math2['Avg Salary'] <= test_math2['Avg Salary'].mean()]['Percent Prof']
stats.ttest_ind(test2_topmath, test2_bottommath)


#HIST
plt.hist(top, alpha = .5, bins = 1000)
plt.hist(bottom, alpha = .5, bins = 1000);

def cdf(value, array):
    return (array<value).sum()/len(array)

vcdf = np.vectorize(cdf, excluded = ['array'])
top_cdf = vcdf(value = top, array = top)
bottom_cdf = vcdf(value = bottom, array = bottom)
plt.scatter(top, top_cdf, marker = '.')
plt.scatter(bottom, bottom_cdf, marker = '.')

top.mean(), bottom.mean()