import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#pearsonr test return pearson's correlation, p-value
from scipy import stats
x = np.array(temp['avg'])
y = np.array(temp['Met or Above'])

stats.pearsonr(x, y)