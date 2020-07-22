import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#--- R using Pandas
full['Met or Above'].corr(full['avg'])


#--- R using Pandas by county
r = []
for i in range(1, 59):
    temp_df = full[full['Co'] == i][['avg','Met or Above']]
    temp_r = temp_df['Met or Above'].corr(temp_df['avg'])
    r.append([i, temp_r])

r_df = pd.DataFrame(r, columns = ['Co', 'r']).sort_values(by = 'r').dropna()



#---- THROW AWAY?
# #pearsonr test return pearson's correlation, p-value
# from scipy import stats
# x = np.array(temp['avg'])
# y = np.array(temp['Met or Above'])

# stats.pearsonr(x, y)