# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:19:50 2019

@author: admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge

A = pd.read_csv("C:/Users/admin/Desktop/Python Programs/ab2.csv")
A

# In[ ]:

sb.pairplot(A)


# In[ ]:


X = A[['RND']]
Y = A[['PROFIT_TYPE']]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20, random_state = 40)


# In[ ]:


lr = LogisticRegression()
model = lr.fit(X_train, Y_train)



# In[ ]:


predicted = model.predict(X_test)
#X_test['predicted'] = predicted.reset_index()
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)
# disable chained assignments
pd.options.mode.chained_assignment = None


# In[ ]:


X_test['predicted'] = predicted
X_test['Actual'] = Y_test
X_test


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,predicted)
cm
