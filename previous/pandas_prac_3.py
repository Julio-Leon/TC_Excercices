import pandas as pd
import csv


#1. Load CSV file
my_data = pd.read_csv('transactions_data.csv')

#2. Check first 5 rows
# print(my_data.head(5), '\n')

#3. Get the shape
# print(my_data.shape, '\n')

#4. Get summary data
# print(my_data.describe(), '\n')

#5. Get data types of each column
my_data['region'] = my_data['region'].astype('string')
my_data['amount'] = pd.to_numeric(my_data['amount'], errors='coerce')
my_data['amount'].astype(float)
# print(my_data.dtypes, '\n')

#7 Rename a column in the dataframe
my_data = my_data.rename(columns={'region': 'regional'})
# print(my_data.columns, '\n')

#8 Filter for rows where a value is greater than another value
filtered_data = pd.DataFrame(columns=my_data.columns)
for item in range(len(my_data)):
    if my_data.loc[item]['amount'] > 550:
        filtered_data.loc[len(filtered_data)] = my_data.loc[item]

# print(filtered_data, '\n')

filtered_data2 = pd.DataFrame(my_data[my_data['amount'] > 550])
print(filtered_data2, '\n')

#9 Select specific columns from the DataFrame

# print(my_data['amount'], '\n')

#10 Drop a column
my_data = my_data.drop(columns=['customer_id'])
# print(my_data, '\n')


#11 Apply a transformation to a column
my_data['amount'] = my_data['amount'] * 2
# print(my_data, '\n')

#12 Adda new column based on a calculation of another column
my_data['amountDivided'] = my_data['amount'] / 2
# print(my_data, '\n')

#13 Group the data by a column and get the mean of the each group
grouped_data = my_data.groupby('regional')['amount'].mean()
# print(grouped_data, '\n')