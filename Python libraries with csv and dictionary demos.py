# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 12:20:25 2019

@author: admin
"""

import numpy as np
import pandas as pd
eid=np.arange(101,106,1)
fn=np.array(["Akshay","Dipak","Payal","Trisha","Manish"])
ln=np.array(["Jain","Jain","Jain","Jain","Jain"])
sal=np.array([50000,6000,7000,5000.01,6000])
did=np.array([10,20,20,30,40])
#emp=pd.DataFrame([eid,fn,ls,sal,did])
#emp=pd.DataFrame([eid,fn,ls,sal,did]).T #for Transpose
#print(emp)
#Coloumn
col=['eid','fn','ls','sal','did']
emp=pd.DataFrame([eid,fn,ln,sal,did],col).T
#print(emp) ##coloumn name 

#DataFrames with Dictionary
import pandas as pd
E={"eid":[101,102,103,104,105],
   "fn":["Akshay","Dipak","Payal","Trisha","Manish"],
   "ln":["Jain","Jain","Jain","Jain","Jain"],
   "sal":[500,60,7000,5000.01,6000]
   }
emp1=pd.DataFrame(data=E)(header=[1,2,4])
print(emp1)

col=['eid','fn','ls','sal','did']
emp2=pd.DataFrame(data=E,['eid1','fn','ls','sal','did'])
print(emp2)

##-------CREATING DF FROM CSV--------##
import pandas as pd
A=pd.read_csv(r"C:/Users/admin/Desktop/Python Programs/notepad.csv",header=None)
print(A)
A1=pd.read_csv("C:/Users/admin/Desktop/Python Programs/notepad1.csv",skiprows=[2])
A2=pd.read_csv("C:/Users/admin/Desktop/Python Programs/notepad1.csv", index_col ='Type') 

print(A2)
A1.index
A1.columns
A1.shape
A1[A1.Name=="Eric"]





