# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile 

df=pd.read_excel(r'C:\Users\alanq\.spyder-py3\tb_gene_data.xlsx')
print(df.columns)
for i in df.index:
    print(df['dst'][i])

#corr heatmap--------------------------------
import numpy as np

import seaborn as sns
corr = df.corr()
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)



#---------------------

#remove dst
df1=df.iloc[:, 0:457]
print(df1)
#---------https://stackoverflow.com/questions/17778394/list-highest-correlation-pairs-from-a-large-correlation-matrix-in-pandas

# find highest corr column

def get_redundant_pairs(df1):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df1.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df1, n=5):
    au_corr = df1.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df1)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

print("Top Absolute Correlations")
print(get_top_abs_correlations(df1, 44))
#rd = get_top_abs_correlations(df1, 44)
#rd.drop(['1.0'], axis=1)
df1=df1.drop(['55a','144a','57a','343a', '243a','70a','49a','180a','22a','146a','99a','221a','372a','46a','343a','138a','73a','349a','105a','172a','188a','75a','356a','273a','181a', '192a','431a','105a','352a','138a','144a','234a','16a','56a','258a','183a','237a','312a','268a','213a','144a','166a'], axis = 1)
print(df1)