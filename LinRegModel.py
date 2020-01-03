# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:54:04 2019

@author: alanq
"""

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
import pandas
from scipy.stats import linregress
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

lr = pd.read_csv(r'C:\Users\alanq\.spyder-py3\LinRegtrain.csv')
lrt = pd.read_csv(r'C:\Users\alanq\.spyder-py3\LinRegtest.csv') 
print(lr.shape)
lr.cov()
array = lr.values
X = array[:,0]
X=X.astype('int')
print(len(X))
print(X)
Y = array[:,1]
print(len(Y))
print(Y)
stats.linregress(X,Y)
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
print("slope: %f    intercept: %f" % (slope, intercept))
print("r-squared: %f" % r_value**2)
plt.plot(X, Y, 'o', label='original data')
plt.plot(X, intercept + slope*X, 'r', label='fitted line')
plt.legend()
plt.show()
