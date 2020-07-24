import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import scipy.stats as stats
import folium
from import_data import *

fonttitle = {'fontname':'Helvetica', 'fontsize':25}
fontaxis = {'fontname':'Helvetica', 'fontsize':18}
blue_color = '#1f788bff'
green_color = '#b2df8a'
purple_color = '#8da0cb'

#----       CDF GRAPH
def cdf(value, array):
    return (array<value).sum()/len(array)

def make_cdf(df1, df2, test1, df3, df4, test2):
    """
    Parameters:
        df1, df2 = top and bottom paying districts
        test1 = which test corresponds with above df
        df3, df4 = top and bottom paying districts
        test2 = which test corresponds with above df

    Returns:
        two side by side CDF graphs
    """
    fig, ax = plt.subplots(1, 2, figsize = (15, 9))
    vcdf = np.vectorize(cdf, excluded = ['array'])
    new_df1 = vcdf(value = df1, array = df1)
    new_df2 = vcdf(value = df2, array = df2)
    
    vcdf = np.vectorize(cdf, excluded = ['array'])
    new_df3 = vcdf(value = df3, array = df3)
    new_df4 = vcdf(value = df4, array = df4)

    ax[0].scatter(df1, new_df1, marker = '.', color = green_color, label = 'Top paying districts')
    ax[0].scatter(df2, new_df2, marker = '.', color = purple_color, label = 'Bottom paying districts')
    ax[0].legend(loc="upper left")
    ax[0].set_title(f'Cumulative Distribution \n of Students Proficient or \n higher in {test1}', fontdict=fonttitle)
    ax[0].set_xlabel("Percent of Students", fontdict=fontaxis);
    
    ax[1].scatter(df3, new_df3, marker = '.', color = green_color, label = 'Top paying districts')
    ax[1].scatter(df4, new_df4, marker = '.', color = purple_color, label = 'Bottom paying districts')
    ax[1].legend(loc="upper left")
    ax[1].set_title(f'Cumulative Distribution \n of Students Proficient or \n higher in {test2}', fontdict=fonttitle)
    ax[1].set_xlabel("Percent of Students", fontdict=fontaxis)
    plt.show()


#----   Histogram Graphs:
fig, ax = plt.subplots(1, 2, figsize = (15, 9))

ax[0].hist(bottommath, alpha = .8, bins = 70, color = purple_color, label = 'Bottom paying districts')
ax[0].hist(topmath, alpha = .6, bins = 70, color = green_color, label = 'Top paying districts')
ax[0].legend(loc="upper left")
ax[0].set_title(f'Percentage of students \n proficient or higher \n in Math by District', fontdict=fonttitle)
ax[0].set_xlabel("Percent of Students", fontdict=fontaxis)
ax[0].set_ylabel("Number of Students", fontdict=fontaxis);

ax[1].hist(bottomela, alpha = .8, bins = 70, color = purple_color, label = 'Bottom paying districts')
ax[1].hist(topela, alpha = .6, bins = 70, color = green_color, label = 'Top paying districts')
ax[1].legend(loc="upper left")
ax[1].set_title(f'Percentage of students \n proficient or higher \n in ELA by District', fontdict=fonttitle)
ax[1].set_xlabel("Percent of Students", fontdict=fontaxis)
ax[1].set_ylabel("Number of Students", fontdict=fontaxis)
# plt.show();


if __name__ == "__main__":
