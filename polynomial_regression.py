# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:30:40 2019

@author: admin
"""


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy import stats
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.preprocessing import PolynomialFeatures


# In[ ]:


#FETCH DATA
A = pd.read_csv("C:/Users/admin/Desktop/Python Programs/poly.csv")
sns.pairplot(A)


# In[ ]:


X = A[['X']]
Y = A[['Y']]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20, random_state = 40)


# In[ ]:


# Fitting Polynomial Regression to the dataset 
from sklearn.preprocessing import PolynomialFeatures 
poly=PolynomialFeatures(degree = 2)
X_poly=poly.fit_transform(X)
 

plm = LinearRegression() 
W = plm.fit(X_poly,Y) 


# In[ ]:


# Visualising the Polynomial Regression results 
plt.scatter(X,Y, color = 'blue') 
 
plt.plot(X, plm.predict(poly.fit_transform(X)), color = 'red') 
plt.title('Polynomial Regression') 
plt.xlabel('X axis') 
plt.ylabel('Y axis') 
 
plt.show() 


# In[ ]:


# plm.predict(poly.fit_transform(125))