Pandas Series is a one-dimensional labeled array capable of holding data of any type
 We usually use pd as alias
 # import pandas as pd--> where pd is alias

 * One dimensional Data(Single column)
  # using series we can access data using indexes
  # We can specify the index associated with a given series
  s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
  # can be accessed using specific index s['a']--> 10 // This will give the output as 10
  # can also give multiple index values using s[['a','b]]
  output will be :-
    b    2
    c    3
_________________________________________
Crucial Data structure in Pandas is DATAFRAMES
column manipulation
df["name"]
#it will give all the names in the data frame
#if we want to delete a specific column from the data frame
--del df["name"]
#if we want to add new column in a data frame
then use Series data structure and index it as well because
with indexing it you will get null value stores as your new column


df["new_col"]=pd.Series([1,2,3,4,5],index=[the previous index values for example 'p1','p2','p3','p4'])

-------------------------------------------------------------------------------------------------------
Row Manipulation
#loc()-if we define the 'label' of the row ie. the index value which we have given
#iloc()-when we use the integer representation (it is faster)
#at()-specify the row and column index
#iat()- integer index of row and column(This is the fastest approach)


