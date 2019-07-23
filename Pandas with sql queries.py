# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:34:50 2019

@author: admin
"""
import pandas as pd
import pandasql as ps
emp=pd.read_csv("C:/Users/admin/Desktop/Python Programs/sql.csv")
#print(emp)
A=ps.sqldf("select * from emp",locals())
print(A)
#Substring
S=ps.sqldf("Select eid,fn,Substr(fn,1,1) as INITS from emp",locals())
print(S)

#Shape
S.shape
A.shape

#Logical Operators
Salary=ps.sqldf("Select * from emp where sal<=8000",locals())
Salary

Sal=ps.sqldf("Select * from emp where sal>=7000 and sal<10000",locals())
Sal

#Like Operator
firstName=ps.sqldf("Select * from emp where fn like 'A%'")
firstName

#Aggrgate Functions

Avg=ps.sqldf("Select Avg(Sal) from emp")
print(Avg)

Aggr=ps.sqldf("Select Avg(Sal),Sum(Sal),Max(Sal),Min(Sal),Count(Sal) from emp",locals())
print(Aggr)

#Group By Clause
Grp=ps.sqldf("Select count(sal),did from emp Group By did")
print(Grp)

SS=ps.sqldf("Select did,sum(sal) as sumsal,max(sal) as maxsal from emp group by did",locals())
print(SS)

# Day8 Joins
import pandasql as ps
import pandas as pd
emp=pd.read_csv("C:/Users/admin/Desktop/Python Programs/sql.csv")
dept=pd.read_csv("C:/Users/admin/Desktop/Python Programs/dept.csv")
Inner=ps.sqldf("Select * from emp as e join dept as d on e.did=d.Dept_id")
print(Inner)

LeftJoin=ps.sqldf("Select * from emp as e left join dept as d on e.did=d.Dept_id")
print(LeftJoin)

#Right Join needs swaping in left join
RightJoin=ps.sqldf("Select * from dept as d left join emp as e on e.did=d.Dept_id")
print(RightJoin)

#Union
FullJoin=ps.sqldf("Select * from emp as e left join dept as d on e.did=d.Dept_id union Select * from dept as d left join emp as e on e.did=d.Dept_id")
print(FullJoin)

#Subquery
subqr=ps.sqldf("Select * from emp where sal>(select Avg(sal) from emp)")
print(subqr)

S1=ps.sqldf("Select eid,sal,Avg(sal) from emp where sal>(Avg(sal))")
print(S1) #Wrong approach as aggregate not works in where clause

S2=ps.sqldf("Select * from emp Join (select Avg(sal) A from emp) w where sal>w.A")
print(S2) #Dumpy coloumn 