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

#----       BAR GRAPHS
def make_maxsalary(df):
    """
    Parameters:
        df = dataframe that will be used to group by county and find the max salary

    Returns:
        bar graph of max teacher salary in each county
    """   
    salary_graph = df.groupby('County Name').agg({'Avg Salary':'max'})\
                        .reset_index()\
                        .sort_values(by='Avg Salary')\
                        .rename(columns={"Avg Salary": "Max Salary"})

    fig, ax = plt.subplots(figsize= (18,9))
    ax.bar(salary_graph['County Name'], salary_graph['Max Salary'], color = blue_color)
    ax.set_ylabel('Highest Average Salary', fontdict=fontaxis)
    ax.set_xlabel("County Name", fontdict=fontaxis)
    ax.axhline(np.median(salary_graph['Max Salary']), linestyle ='--', linewidth=6, 
                        color = green_color, label = 'Median')
    ax.legend(loc=2)
    plt.xticks(rotation=90)
    plt.ylim(40000, 120000)
    plt.title('Highest Average Teacher Salary in the County', fontdict=fonttitle)
    plt.show();

def make_district_salary_by_county(df, county_lst, color):
    """
    Parameters:
        df = dataframe that will be used to group by county and find the max salary
        county_lst = list of counties to be graphed
        color = graph color desired
    Returns:
        bar graph of max teacher salary in each county
    """  
    fig, axs = plt.subplots(1, 4, figsize= (6,4), sharey=True)

    for ax, county in zip(axs.flatten(), county_lst):
        temp_df = df[df['County Name'] == county][["Avg Salary", 'District Name']].sort_values(by='Avg Salary', ascending = False)
        ax.bar(temp_df['District Name'], temp_df['Avg Salary'], color = color)
        ax.set_xticks([])
        ax.set_title(f'{county} County')
        ax.set_ylabel(f'Average Salary by District')
        ax.set_xlabel(f'District(s) in {county}')
        plt.ylim(40000, 120000)
    plt.show();


#----       SCATTER PLOTS 
def scatter_salary_met(df1, df2, color1, color2, marker = ('o')):
    """
    Parameters:
        df1 = dataframe of test 1 to graph
        df2 = dataframe of test 2 to graph
        color1 = graph color desired for df1
        color2 = graph color desired for df2
    Returns:
        scatter plot of teacher salary and % proficient
    """ 
    fig, ax = plt.subplots(figsize= (18,9))
    ax.scatter(df1['Avg Salary'], df1['Met or Above'], 
                        color = color1, alpha = 0.4, label = 'ELA', marker = marker)
    ax.scatter(df2['Avg Salary'], df2['Met or Above'], 
                        color = color2, alpha = 0.4, label = 'Math', marker = marker)
    plt.title('Salaries and Standards', fontdict=fonttitle)
    ax.set_ylabel('All Students Who Met or Exceeded Standard', fontdict=fontaxis)
    ax.set_xlabel("Average Teacher Salary by District", fontdict=fontaxis)
    ax.legend(loc=2)
    fig.tight_layout
    plt.show();

def group_df(df):
    """
    Parameters:
        df = dataframe of group
    Returns:
        df grouped by District name
    """
    grouped = df.groupby('District Name').agg({'Avg Salary':'max', 'Met or Above':'mean'})
    return grouped 


#----       pvalue
def find_p(df, test): 
    """ 
    Parameters: 
        df = full dataframe of test 1 result to be split into two 
        test = which test is the above dataframe for 
    Returns: 
        test statistics and p value for those two means 
    """     
    top = df[df['Avg Salary'] > df['Avg Salary'].median()]['Met or Above'] 
    bottom = df[df['Avg Salary'] <= df['Avg Salary'].median()]['Met or Above'] 
    _, pvalue = stats.ttest_ind(top, bottom) 
    return(f'p-value for {test} test {pvalue}.') 


if __name__ == "__main__":
    find_p(fullela, 'ELA')
    find_p(fullmath, 'Math') 
    
    make_maxsalary(full)

    top4 = ['Santa Barbara', 'Santa Clara', 'Monterey', 'San Mateo']
    bottom4 = ['Plumas', 'Alpine', 'Sierra', 'Lake']
    make_district_salary_by_county(full, top4, green_color)
    make_district_salary_by_county(full, bottom4, purple_color)

    scatter_salary_met(fullela, fullmath, blue_color, green_color)

    grouped_ela = group_df(fullela)
    grouped_math = group_df(fullmath)
    scatter_salary_met(grouped_ela, grouped_math, blue_color, green_color, 'D')