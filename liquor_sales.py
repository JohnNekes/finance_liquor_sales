import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\John Nekes\\Desktop\\Analytics\\Python\\finance_liquor_sales2.csv")

# Identify the predominant item per zipcode
bottles_sold = df.groupby(['zip_code', 'item_number']).size().reset_index(name='count')
bottles_sold = bottles_sold.loc[bottles_sold.groupby('zip_code')['count'].idxmax()]

# Calculate the proportion of sales for each store
sales_proportion_per_store = df.groupby('store_name').size() / len(df) * 100

# Step 3: Data Visualization

# Plot predominant item per zipcode
plt.figure(figsize=(12, 6))
plt.scatter(bottles_sold['zip_code'], bottles_sold['count'], color='blue')
plt.title('Predominant Item per Zipcode')
plt.xlabel('Zipcode')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot proportion of sales per store
plt.figure(figsize=(10, 6))
sales_proportion_per_store_sorted = sales_proportion_per_store.sort_values(ascending=True)
sales_proportion_per_store_sorted.plot(kind='barh', color='lightgreen')
plt.title('Proportion of Sales per Store (2016-2019)')
plt.xlabel('Store Name')
plt.ylabel('Proportion (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
