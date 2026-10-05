import pandas as pd

#Lets log all the things we did in this script to a log file
import logging

logging.basicConfig(level=logging.INFO, filename='pandas_prac.log')

my_data = pd.read_csv('sales_data.csv')
logging.info("Data loaded from sales_data.csv")


# print(my_data)

# Validate the schema of the the loaded data
# print(my_data.dtypes)

# Lets clean the data by removing any rows with missing values
cleaned_data = my_data.dropna()
logging.info("Data cleaned by removing rows with missing values")

# print(cleaned_data)
# Lets turn the different columns into the correct data types


#Lets turn invalid values into Nan and then drop them
cleaned_data['sales_amount'] = pd.to_numeric(cleaned_data['sales_amount'], errors='coerce')
logging.info("Sales amounts converted to numeric, invalid values set to NaN")

new_data = cleaned_data.dropna()
logging.info("Rows with missing sales amounts removed")

new_data['tax_amount'] = new_data['sales_amount'] * 0.1
logging.info("Tax amount calculated as 10% of sales amount")

print(new_data)
new_data['order_id'] = new_data['order_id'].astype(int)
new_data['customer'] = new_data['customer'].astype(str)
new_data['region'] = new_data['region'].astype(str)
new_data['product'] = new_data['product'].astype(str)
new_data['category'] = new_data['category'].astype(str)
new_data['sales_amount'] = new_data['sales_amount'].astype(float)
new_data['order_date'] = new_data['order_date'].astype(str)
new_data['tax_amount'] = new_data['tax_amount'].astype(float)



print(new_data.dtypes, '\n')

# Lets aggregate the data by region, only the sales_amount and tax_amount columns will be summed up 
aggregated_data = new_data.groupby('region')[['sales_amount', 'tax_amount']].sum()
logging.info("Data aggregated by region, summing sales_amount and tax_amount")

print(aggregated_data)

# Lets export the aggregated data to a new CSV file
aggregated_data.to_csv('aggregated_sales_data.csv', index=True)
logging.info("Aggregated data exported to aggregated_sales_data.csv")

