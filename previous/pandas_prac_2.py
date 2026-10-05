import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, filename='pandas_prac_2.log')

my_data = pd.read_csv('Git_Practice/git_lab/data/sales_data.csv')

#print(my_data.head(5))

# print data types of the columns and shape of the data
# print(my_data.dtypes, '\n')
# print(my_data.shape)

my_data['sales_amount'] = pd.to_numeric(my_data['sales_amount'], errors='coerce')

try:
    my_data['sales_amount'] = my_data['sales_amount'].fillna(my_data['sales_amount'].mean())
    logging.info("Sales amounts converted to numeric, invalid values set to NaN and filled with mean")
except Exception as e:
    logging.error(f"Error filling NaN values in sales_amount: {e}")

# Adding a duplicate so I can then remove duplicates and show that it works
my_data.loc[len(my_data)] = my_data.loc[0]
logging.info('Added a duplicate so I can demostrate removing duplicates')
# print(my_data)

my_data.drop_duplicates(inplace=True)
logging.info('Removed dupicates from my data, Idempotency check')
# print(my_data)

my_data['sales_amount'] = my_data['sales_amount'].astype('int32')
# print(my_data.dtypes)

#select row where sales_amount is greater than 1000
big_sales = my_data[my_data['sales_amount'] > 1000]
logging.info('Logging big sales')

#filter data to only inlcude rows where column is a string and contains the word 'data'
my_data.loc[len(my_data)] = ['data', 'data', 'data', 'data', 'data', 1234, '2023-01-01']
filtered_data = pd.DataFrame(columns=my_data.columns)
for item in range(len(my_data)):
    if my_data.loc[item].dtype == 'object' and my_data.loc[item].str.contains('data').any():
        # print(my_data.loc[item])
        filtered_data.loc[len(filtered_data)] = my_data.loc[item].astype(str)

# print(filtered_data)

# filtered_data = my_data[my_data['column_name'].str.contains('data')]

# print(my_data.describe())

# group by sales
try:
    # print(my_data)
    print('\n')
    # grouped = my_data.groupby(["category", 'region'])['sales_amount'].count()
    # print(grouped)
except:
    logging.error('Some error')


# for item in range(len(my_data)):
#     print(my_data.iloc[item])
#     print(my_data.iloc[item].nunique())

grouped_data = my_data.groupby(['category', 'region'])['sales_amount'].mean().sort_values()

try:
    grouped_data.to_csv('pandas_prac_2.csv')
    logging.info('Moved cleaned data to a CSV file')
except:
    print('Logged Error')
    logging.error('Export to CSV error')


a = [1, 2, 2, 3]

print(list(set(a)))