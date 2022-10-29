import pandas as pd
li=[[1000,3000,4000],['Depar1','Depar2','Depar1','Depar2'],[219,220,221,222]]
li=[[1000,'DB201',555],[4000,'DB201',111],[2000,'DB202',222],[3000,'DB201',333],[1000,'DB202',444]]
lid={'Salary':[1000,2000,3000,4000,5000],
     'Department':['DB201','DB201','DB202','DB201','DB202'],
     'empid':[555,444,333,222,111]
     }
names=["kevin","ben","suzy","mohit",'KHAN']
df=pd.DataFrame(li,index=names,columns=["salary","Department",'eMPid'])
df["Seats"]=pd.Series([1,2,3,4,5],index=names)
# dp=pd.DataFrame(lid,index=names)
# ds=pd.DataFrame.from_records(lid,index=names)

print(df.loc["ben"])
print(df.iloc[1])
print(df.iat[0,2])
print(df)


