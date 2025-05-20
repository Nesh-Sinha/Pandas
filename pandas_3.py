import pandas as pd


# savind data of empData.csv in df
df = pd.read_csv('empData.csv') 
print(df)

print(df.head())  # Display first 5 enteries by default
print(df.head(12)) # Display first 12 enteries 

print(df.tail()) # tail() = Last 5 entries by default


# ilock() = (how many rows, how many columns)
# iloc is index/integer based location
print(df.iloc[:2]) # first 2 rows

print(df.iloc[:10,2:4]) # 10 rows and  column from 2 to 4

print(df.iloc[0:6:2,0:10:2]) # printing even rows and even columns (start,stop, step)

print(df.iloc[2,1]) # printing 2nd row and 1st column


# loc() = (row, column) it is used to access a group of rows and columns by labels or a boolean array
# fromat of condition is df.loc[condition, [column1, column2]]
print(df.loc[df['PerformanceScore']>=7.0,['EmployeeID','Name','PerformanceScore']]) # printing EmployeeID, Name and PerformanceScore of employees whose performance score is more than 7.0


print(df.loc[df['Salary']>7000]) 


df.loc[0,'Name'] = None # changing the value of 0th row and Name column to None
print(df.head(5))

df['Name'].fillna(df['Name'].mode()[0], inplace=True) # filling the missing values of Name column with mode
print(df.head(5))