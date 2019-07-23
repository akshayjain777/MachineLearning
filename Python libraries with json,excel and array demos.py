# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 12:27:09 2019

@author: admin
"""
import pandas as pd
import Numpy as np

##-------CREATING DF FROM JSON--------##

#Columns Oriented
#A=emp.to_json("C:/Users/admin/Desktop/Python Programs/DataframeC.json",orient='columns')
#print(A)
#Row Oriented
#A1=emp.to_json("C:/Users/admin/Desktop/Python Programs/DataframeR.json",orient='records')
#print(A1)

###Separator for CSV

#S=pd.read_csv("C:/Users/admin/Desktop/Python Programs/ABC.csv",sep=":",header=0,skiprows=0)
#print(S)

###FOR Excel
E=pd.read_excel("C:/Users/admin/Desktop/Python Programs/ExcelFirst3Words.xlsx",sep=":")
#print(E)
###Sheetname in Excel
E1=pd.read_excel("C:/Users/admin/Desktop/Python Programs/ExcelFirst3Words.xlsx",sheet_name="Sheet1",index=False)
print(E1)

#E1=pd.read_excel("C:/Users/admin/Desktop/Python Programs/ExcelFirst3Words.xlsx",sheet_name="Sheet1")
#print(E1)


######  Inserting
emp["dName"]=np.array(["106","HR","HR","Variable","1","2"])