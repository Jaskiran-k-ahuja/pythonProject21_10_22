import pandas as pd
population=[1000,2000,3000,4000]
countries=['India','China','England','Australia']
s2=pd.Series(population,index=countries)
print(s2.min())