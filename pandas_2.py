import pandas as pd

data=pd.Series([10,20,30,40,50])

print(data)
print(type(data))
print(type(data.values))
print(data.index)

data=pd.Series([10,20,30],index=['a','b','c'])
print(data)

print(data['b'])
