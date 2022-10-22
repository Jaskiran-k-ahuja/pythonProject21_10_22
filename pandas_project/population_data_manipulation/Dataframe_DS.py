import pandas as pd
d=[['kevin',20],['sim',30],['ben',40],['kat',50]]
ds={'name':['kevin','sam','ben'],
    'age':[10,20,30]   }
s=[1,2,3]
df=pd.DataFrame(ds,index=['person1','person2','person3'])
# print(df)

df["new_col"]=pd.Series(s,index=['person1','person2','person3'])

# print(df.loc["person1"])
# print(df.iloc[1])
# print(df.at["person1","age"])
print(df.iat[2,0])