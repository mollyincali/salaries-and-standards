import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

fullela = full[full['Test Id'] == 1]
fullmath = full[full['Test Id'] == 2]

top = fullela[fullela['Avg Salary'] > fullela['Avg Salary'].mean()]['Met or Above']
bottom = fullela[fullela['Avg Salary'] <= fullela['Avg Salary'].mean()]['Met or Above']
stats.ttest_ind(top,bottom)

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