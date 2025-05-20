''' ---- Series And DataFrame ---- '''

import pandas as pd

df = pd.read_csv('customer.csv')

# Displaying data where age >= 30 and AdSpend >= 5000 (Practising Conditional Selection)
df_c= df.loc[(df['Age']>=30) & (df['AdSpend']>=5000)]
print(df_c)


# Single Aggregation
# Grouping by CampaignChannel and getting the maximum AdSpend
# groupby(column name for grouping same element )[column name to perform action on].agg(['action'])
df_a = df.groupby('CampaignChannel')['AdSpend'].agg(['max']) 
print(df_a)


# Multiple Aggregation
# Grouping by CampaignChannel and getting the maximum, minimum, mean, count and sum of AdSpend
df_a = df.groupby('CampaignChannel')['AdSpend'].agg(['max','min','mean','count','sum']) 
print(df_a)

# Describe() function gives the count, mean, std, min, 25%, 50%, 75% and max of the AdSpend
df_a = df.groupby('CampaignChannel')['AdSpend'].describe()
print(df_a)


#Multiple Columns
# Grouping by CampaignChannel and CampaignType, and getting the maximum ClickThrough
df_a = df.groupby(['CampaignChannel','CampaignType'])['ClickThrough'].max()
print(df_a)



# apply() function is used to apply a function along the axis of the DataFrame
# Format of apply() function is df.apply(function, axis=0/1)
# Grouping by Age-group and getting the maximum, minimum, mean, count and sum of AdSpend
def age_group(age):
    if age < 25:
        return 'Group 1 (0 - 24)'
    elif 25 <= age <= 35:
        return 'Group 2 (25 - 34)'
    elif 35 < age <= 45:
        return 'Group 3 (35 - 44)'
    elif 45 < age <= 55:
        return 'Group 4 (45 - 54)'
    else:
        return 'Group 4 (55+)'
    
df['AgeGroup'] = df['Age'].apply(age_group) # Creating a new column AgeGroup by applying the function age_group on the Age column
age_group = df.groupby('AgeGroup')['AdSpend'].agg(['max','min','mean','count','sum']) # Grouping by AgeGroup and getting the maximum, minimum, mean, count and sum of AdSpend
print(age_group)