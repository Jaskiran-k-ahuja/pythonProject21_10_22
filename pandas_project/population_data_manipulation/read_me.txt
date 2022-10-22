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

