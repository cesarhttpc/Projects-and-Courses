# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# path = 'Coppel/train_data/train_data.csv'
path = 'C:/Users/ce_ra/Documents/CIMAT/Python/Experimentos/Coppel/train_data/train_data.csv'

df = pd.read_csv(path)

# df.head()
df.info()
# print(df.isnull().sum())


# %%
# Convert 'datetime' column to datetime object
df['order_date'] = pd.to_datetime(df['order_date'])

# Truncate datetime to date
df['order_date'] = df['order_date'].dt.date

# Display the DataFrame
print(df)

# Create a date range from the minimum to the maximum date in the DataFrame
date_range = pd.date_range(start=df['order_date'].min(), end=df['order_date'].max(), freq='D')

# Identify missing dates
missing_dates = date_range.difference(df['order_date'])

# Print missing dates
print("Missing dates:")
print(missing_dates)

# %%

# Group by date and category, then count the number of sold articles (SKU)
daily_sales_by_category = df.groupby(['order_date', 'cat']).size().reset_index(name='articles_sold')

# Display the resulting DataFrame
print(daily_sales_by_category)

# %%

# Pivot the DataFrame to get categories as columns
sales_pivot = daily_sales_by_category.pivot(index='order_date', columns='cat', values='articles_sold')

# Plot the data
# plt.figure(figsize=(150,100))
sales_pivot.plot(kind='line', marker='', linewidth = 0.3)
plt.title('Number of Sold Articles Per Day by Category')
plt.xlabel('Date')
plt.ylabel('Number of Sold Articles')
plt.xticks(rotation=45)
plt.legend(title='Category')
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()

# %%

# Group by date and category, then count the number of sold articles (SKU)
daily_sales = df.groupby(['order_date', 'cat']).size().reset_index(name='articles_sold')

# Display the resulting DataFrame
print(daily_sales_by_category)


















# %%
import pandas as pd

# Sample data with datetime, SKU, and category
data = {
    'datetime': ['2019-01-05 00:20:29.257000+00:00', '2019-01-05 12:34:56.123000+00:00',
                 '2019-01-06 14:15:00.000000+00:00', '2019-01-06 18:20:00.000000+00:00',
                 '2019-01-07 09:00:00.000000+00:00'],
    'SKU': ['A001', 'A002', 'A003', 'A004', 'A005'],
    'category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'datetime' column to datetime object
df['datetime'] = pd.to_datetime(df['datetime'])

# Truncate datetime to date
df['date'] = df['datetime'].dt.date

# Group by date and category, then count the number of sold articles (SKU)
daily_sales_by_category = df.groupby(['date', 'category']).size().reset_index(name='articles_sold')

# Display the resulting DataFrame
print(daily_sales_by_category)

# %%



