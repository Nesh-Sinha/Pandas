# Pandas DATA PreProcessing

import pandas as pd

df = pd.read_csv('spotify.csv')

# print(df.head(5)) 


# Display number of values which are null in each column
value_missing = df.isnull().sum()
print(value_missing)

# Display number of values which are null if they are greater than 0
print(value_missing[value_missing>0])

# Dropping all the null values
df_c = df.dropna(subset=['song'])
print(df_c.isnull().sum())

# Checking all the data types of columns
print(df_c.dtypes)

# COnverting the int column to float
df_c['Release Date'] = pd.to_datetime(df_c['Release Date'], format = '%Y')

print(df_c.dtypes)
print(df_c.iloc[0,4:]) 


# Checking duplicates

print(df_c.duplicated().sum())

df.drop_duplicates() # Drop duplicates
print(df_c.duplicated().sum())


# TASK 1: AVerage popularity by Emotions

df_a = df.groupby('emotion')['Popularity'].mean().sort_values(ascending=True)
print(df_a)

# TASK 2: Average Energy and Danceability by Genre
df_a = df.groupby('Genre')[['Energy','Danceability']].mean()
print(df_a)

# TASK 3: Emotion associated with popularity
df_a = df.groupby('emotion')['Popularity'].mean().sort_values(ascending=False)
print(df_a)


# TASK 4: Top Artist By Soung Count
df_a = df.groupby('artist')['song'].count().sort_values(ascending=False)
print(df_a)

# Task 5: Top 10 Loud Songs
df_a = df[['song','Loudness']].sort_values(by='Loudness',ascending=False).head(10)
print(df_a) 

# Task 6 : Songs released by an artist in a year
df_a = df.groupby(['artist','Release Date'])['song'].count().sort_values(ascending=False)
print(df_a)