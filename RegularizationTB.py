# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:37:09 2019

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
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn import metrics
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

lm = LinearRegression(copy_X=True)
lm_lasso = Lasso()
lm_ridge = Ridge()
lm_Elastic = ElasticNet()


dataset = pd.read_excel (r'C:\Users\alanq\.spyder-py3\tb_gene_data.xlsx') 
print(list(dataset.columns.values))
print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('dst').size())

RSEED = 50

feature_cols = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12a', '13a', '14a', '15a', '16a', '17a', '18a', '19a', '20a', '21a', '22a', '23a', '24a', '25a', '26a', '27a', '28a', '29a', '30a', '31a', '32a', '33a', '34a', '35a', '36a', '37a', '38a', '39a', '40a', '41a', '42a', '43a', '44a', '45a', '46a', '47a', '48a', '49a', '50a', '51a', '52a', '53a', '54a', '55a', '56a', '57a', '58a', '59a', '60a', '61a', '62a', '63a', '64a', '65a', '66a', '67a', '68a', '69a', '70a', '71a', '72a', '73a', '74a', '75a', '76a', '77a', '78a', '79a', '80a', '81a', '82a', '83a', '84a', '85a', '86a', '87a', '88a', '89a', '90a', '91a', '92a', '93a', '94a', '95a', '96a', '97a', '98a', '99a', '100a', '101a', '102a', '103a', '104a', '105a', '106a', '107a', '108a', '109a', '110a', '111a', '112a', '113a', '114a', '115a', '116a', '117a', '118a', '119a', '120a', '121a', '122a', '123a', '124a', '125a', '126a', '127a', '128a', '129a', '130a', '131a', '132a', '133a', '134a', '135a', '136a', '137a', '138a', '139a', '140a', '141a', '142a', '143a', '144a', '145a', '146a', '147a', '148a', '149a', '150a', '151a', '152a', '153a', '154a', '155a', '156a', '157a', '158a', '159a', '160a', '161a', '162a', '163a', '164a', '165a', '166a', '167a', '168a', '169a', '170a', '171a', '172a', '173a', '174a', '175a', '176a', '177a', '178a', '179a', '180a', '181a', '182a', '183a', '184a', '185a', '186a', '187a', '188a', '189a', '190a', '191a', '192a', '193a', '194a', '195a', '196a', '197a', '198a', '199a', '200a', '201a', '202a', '203a', '204a', '205a', '206a', '207a', '208a', '209a', '210a', '211a', '212a', '213a', '214a', '215a', '216a', '217a', '218a', '219a', '220a', '221a', '222a', '223a', '224a', '225a', '226a', '227a', '228a', '229a', '230a', '231a', '232a', '233a', '234a', '235a', '236a', '237a', '238a', '239a', '240a', '241a', '242a', '243a', '244a', '245a', '246a', '247a', '248a', '249a', '250a', '251a', '252a', '253a', '254a', '255a', '256a', '257a', '258a', '259a', '260a', '261a', '262a', '263a', '264a', '265a', '266a', '267a', '268a', '269a', '270a', '271a', '272a', '273a', '274a', '275a', '276a', '277a', '278a', '279a', '280a', '281a', '282a', '283a', '284a', '285a', '286a', '287a', '288a', '289a', '290a', '291a', '292a', '293a', '294a', '295a', '296a', '297a', '298a', '299a', '300a', '301a', '302a', '303a', '304a', '305a', '306a', '307a', '308a', '309a', '310a', '311a', '312a', '313a', '314a', '315a', '316a', '317a', '318a', '319a', '320a', '321a', '322a', '323a', '324a', '325a', '326a', '327a', '328a', '329a', '330a', '331a', '332a', '333a', '334a', '335a', '336a', '337a', '338a', '339a', '340a', '341a', '342a', '343a', '344a', '345a', '346a', '347a', '348a', '349a', '350a', '351a', '352a', '353a', '354a', '355a', '356a', '357a', '358a', '359a', '360a', '361a', '362a', '363a', '364a', '365a', '366a', '367a', '368a', '369a', '370a', '371a', '372a', '373a', '374a', '375a', '376a', '377a', '378a', '379a', '380a', '381a', '382a', '383a', '384a', '385a', '386a', '387a', '388a', '389a', '390a', '391a', '392a', '393a', '394a', '395a', '396a', '397a', '398a', '399a', '400a', '401a', '402a', '403a', '404a', '405a', '406a', '407a', '408a', '409a', '410a', '411a', '412a', '413a', '414a', '415a', '416a', '417a', '418a', '419a', '420a', '421a', '422a', '423a', '424a', '425a', '426a', '427a', '428a', '429a', '430a', '431a', '432a', '433a', '434a', '435a', '436a', '437a', '438a', '439a', '440a', '441a', '442a', '443a', '444a', '445a', '446a', '447a', '448a', '449a', '450a', '451a', '452a', '453a', '454a', '455a', '456a', '457a']
print(feature_cols)
X = dataset.values[:,0:457] # Features
Y = dataset.dst # Target variable
validation_size = 0.20
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

#lm.fit(X_train, Y_train)
#lm_lasso.fit(X_train, Y_train)
#lm_ridge.fit(X_train, Y_train)
lm_Elastic.fit(X_train, Y_train)