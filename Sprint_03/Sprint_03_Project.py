#Sprint 3: Exploratory Data Analysis (EDA)
#Chapter 8: EDA Project

# Import the libraries you'll need for this analysis
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
# Note: These files use semicolon (;) as the separator instead of comma
orders         = pd.read_csv('/datasets/instacart_orders.csv', sep=';')
products       = pd.read_csv('/datasets/products.csv', sep=';')
departments    = pd.read_csv('/datasets/departments.csv', sep=';')
aisles         = pd.read_csv('/datasets/aisles.csv', sep=';')
order_products = pd.read_csv('/datasets/order_products.csv', sep=';')

# run orders_products.info() below, but include the argument show_counts=True since this is a large file.
order_products.info(show_counts=True)

# Display rows where the product_name column has missing values
print(products[products['product_name'].isna()])

# Combine conditions to check for missing product names in aisles other than 100
print(products[(products['product_name'].isna()) & (products['aisle_id'] != 100)])

# Combine conditions to check for missing product names in aisles other than 21
print(products[(products['product_name'].isna()) & (products['aisle_id'] != 21)])

# What is this aisle and department?
print(aisles[aisles['aisle_id'] == 100])
print(departments[departments['department_id'] == 100])
print(aisles[aisles['aisle_id'] == 21])
print(departments[departments['department_id'] == 21])

# Fill missing product names with 'Unknown'
products['product_name'].fillna('Unknown', inplace=True)

# Display rows where the days_since_prior_order column has missing values
print(orders[orders['days_since_prior_order'].isna()])

# Are there any missing values where it's not a customer's first order?
print(orders[(orders['days_since_prior_order'].isna()) & (orders['order_number'] > 1)])

# Display rows where the add_to_cart_order column has missing values
print(order_products[order_products['add_to_cart_order'].isna()])

# Use .min() and .max() to find the minimum and maximum values for this column.
print(order_products['add_to_cart_order'].min())
print(order_products['add_to_cart_order'].max())

# Save all order IDs with at least one missing value in 'add_to_cart_order'
missing_order_ids = order_products[order_products['add_to_cart_order'].isna()]['order_id'].unique()
print(missing_order_ids)

# Do all orders with missing values have more than 64 products?
print(order_products[order_products['order_id'].isin(missing_order_ids) & (order_products['add_to_cart_order'] > 64)])

# Replace missing values with 999 and convert column to integer type
order_products['add_to_cart_order'].fillna(999, inplace=True)
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].astype(int)

# Find the number of duplicate rows in the orders dataframe
print(orders.duplicated().sum())

# View the duplicate rows
print(orders[orders.duplicated()])

# Remove duplicate orders
orders.drop_duplicates(inplace=True)

# Double check for duplicate rows
print(orders.duplicated().sum())

# Check for fully duplicate rows
print(orders.duplicated(subset=['user_id', 'order_id', 'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order']).sum())

# Check for just duplicate product IDs using subset='product_id' in duplicated()
print(products.duplicated(subset='product_id').sum())

# Check for just duplicate product names (convert names to lowercase to compare better)
print(products['product_name'].str.lower().duplicated().sum())

products[products['product_name'].str.lower() == 'high performance energy drink']
# Drop duplicate product names (case insensitive)
products.drop_duplicates(subset='product_name', keep='first', inplace=True, ignore_index=True)

# Check for duplicate entries in the departments dataframe
print(departments.duplicated(subset='department_id').sum())

# Check for aisles entries in the departments dataframe
print(aisles.duplicated(subset='aisle_id').sum())

# Check for duplicate entries in the order_products dataframe
print(order_products.duplicated(subset=['order_id', 'product_id']).sum())

# [A1] Verify that the 'order_hour_of_day' and 'order_dow' values in the orders tables are sensible (i.e. 'order_hour_of_day' ranges from 0 to 23 and 'order_dow' ranges from 0 to 6)
# To verify that the values in the order_hour_of_day and order_dow columns are sensible:
# Check unique values: Use .unique() on each column to extract all distinct values present.
# Sort the results: Use sorted() to arrange the unique values in ascending order for easier verification.
# Validate ranges:
# Ensure order_hour_of_day values range from 0 to 23 (representing hours of the day).
# Ensure order_dow values range from 0 to 6 (representing days of the week).
# This process confirms that the data aligns with expected ranges and there are no out-of-bound or invalid entries.
print(sorted(orders['order_hour_of_day'].unique()))
print(sorted(orders['order_dow'].unique()))

# [A2] What time of day do people shop for groceries?
# To determine the time of day people shop for groceries, analyze the order_hour_of_day column in the orders dataset. Use .value_counts() to count the number of orders placed at each hour, and then sort the results by the hour for a clear chronological order.
# Finally, visualize the data with a bar plot to easily observe the shopping trends across different times of the day.
print(orders['order_hour_of_day'].value_counts().sort_index())
plt.figure(figsize=(10, 6))
plt.bar(orders['order_hour_of_day'].value_counts().sort_index().index, orders['order_hour_of_day'].value_counts().sort_index().values)
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.title('Time of Day People Shop for Groceries')
plt.show()

# [A3] What day of the week do people shop for groceries?
# To figure out what day of the week people shop for groceries, analyze the order_dow column in the orders dataset. Use .value_counts() to count the number of orders for each day of the week, and then sort the results by the day index to maintain the correct order.
# Visualize the data with a bar plot to clearly observe shopping patterns across the days of the week.
print(orders['order_dow'].value_counts().sort_index())
plt.figure(figsize=(10, 6))
plt.bar(orders['order_dow'].value_counts().sort_index().index, orders['order_dow'].value_counts().sort_index().values)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Orders')
plt.title('Day of the Week People Shop for Groceries')
plt.show()

# [A4] How long do people wait until placing another order?
# To understand how long people wait before placing another order, analyze the days_since_prior_order column in the orders dataset. Use .value_counts() to count how many orders were placed for each interval of days, then sort the results by the number of days for clarity.
# Visualize the data using a bar plot to observe patterns in ordering frequency over time.
print(orders['days_since_prior_order'].value_counts().sort_index())
plt.figure(figsize=(10, 6))
plt.bar(orders['days_since_prior_order'].value_counts().sort_index().index, orders['days_since_prior_order'].value_counts().sort_index().values)
plt.xlabel('Days Since Prior Order')
plt.ylabel('Number of Orders')
plt.title('Frequency of Orders Over Time')
plt.show()

# [B1] Is there a difference in 'order_hour_of_day' distributions on Wednesdays and Saturdays? Plot the bar charts for both days and describe the differences that you see.
# To determine if there's a difference in the order_hour_of_day distributions on Wednesdays and Saturdays, follow these steps:
# Create masks for Wednesday (order_dow == 3) and Saturday (order_dow == 6) to filter the orders data.
# Count the order hours for each day using .value_counts() and sort them by hour with .sort_index() for clarity.
# Combine the counts for both days into a single DataFrame using pd.concat(), and label the columns for easier interpretation.
# After preparing the data, plot bar charts for both days to visually compare the distribution of order times. Look for patterns such as peaks or differences in the busiest times throughout the day.
# Create masks for Wednesday and Saturday
wednesday_orders = orders[orders['order_dow'] == 3]
saturday_orders = orders[orders['order_dow'] == 6]
# Count the order hours for each day and sort them by hour
wednesday_counts = wednesday_orders['order_hour_of_day'].value_counts().sort_index()
saturday_counts = saturday_orders['order_hour_of_day'].value_counts().sort_index()
# Combine the counts for both days into a single DataFrame
day_counts = pd.concat([wednesday_counts, saturday_counts], axis=1)
day_counts.columns = ['Wednesday', 'Saturday']
# Plot bar charts for both days
day_counts.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.title('Order Hour Distribution on Wednesdays and Saturdays')
plt.show()

# [B2] What's the distribution for the number of orders per customer?
# To explore the distribution of the number of orders per customer:
# Group the data by user_id to calculate the total number of orders for each customer. Use .groupby('user_id') and count the order_id for each group.
# Sort the results using .sort_values() for better readability.
# Visualize the distribution using a histogram to observe how many orders most customers typically place.
# Adjust the number of bins in the histogram to refine the visualization and better capture the pattern.
# Group by user_id and count the number of orders for each customer
customer_order_counts = orders.groupby('user_id')['order_id'].count().sort_values()
# Plot a histogram to visualize the distribution of orders per customer
plt.figure(figsize=(10, 6))
plt.hist(customer_order_counts, bins=20, edgecolor='black')
plt.xlabel('Number of Orders per Customer')
plt.ylabel('Number of Customers')
plt.title('Distribution of Number of Orders per Customer')
plt.show()

# [B3] What are the top 20 popular products (display their id and name)?
# To identify the top 20 most popular products:
# Merge the datasets: Combine order_products and products on product_id to access both the product IDs and names in a single DataFrame.
# Group the data: Group by both product_id and product_name to aggregate the order counts for each product using .size().
# Sort the results: Use .sort_values(ascending=False) to rank products by their popularity.
# Display the top 20: Use .head(20) to focus on the most frequently ordered products.
# Visualize the results: Create a bar chart to highlight the top products and their order counts.
# This will give you a clear view of the most popular products and their ranking.
# Merge order_products and products on product_id
merged_data = pd.merge(order_products, products, on='product_id')
# Group by product_id and product_name, and count the order counts for each product
product_order_counts = merged_data.groupby(['product_id', 'product_name']).size().sort_values(ascending=False)
# Display the top 20 popular products
top_20_products = product_order_counts.head(20)
print(top_20_products)
# Plot a bar chart to visualize the top 20 popular products
plt.figure(figsize=(12, 8))
plt.bar(top_20_products.index.get_level_values('product_name'), top_20_products.values)
plt.xlabel('Product Name')
plt.ylabel('Number of Orders')
plt.title('Top 20 Popular Products')
plt.xticks(rotation=45)
plt.show()

# [C1] How many items do people typically buy in one order? What does the distribution look like?
# To analyze how many items people typically buy in one order:
# Group the data by order_id and count the number of products (product_id) in each order using .count(). This gives the number of items in each order.
# Aggregate the counts: Use .value_counts() to determine how frequently different order sizes occur, and then sort the results with .sort_index() to organize by the number of items.
# Visualize the distribution: Use a bar plot to show the frequency of orders for each size, with the x-axis representing the number of items and the y-axis representing the number of orders.
# This will help you understand the typical size of a grocery order and identify any trends in purchasing behavior.
# Group by order_id and count the number of products in each order
order_sizes = order_products.groupby('order_id')['product_id'].count()
# Count the frequency of each order size and sort by the number of items
order_size_distribution = order_sizes.value_counts().sort_index()
# Plot a bar chart to visualize the distribution of order sizes
plt.figure(figsize=(10, 6))
plt.bar(order_size_distribution.index, order_size_distribution.values)
plt.xlabel('Number of Items in Order')
plt.ylabel('Number of Orders')
plt.title('Distribution of Order Sizes')
plt.show()

# [C2] What are the top 20 items that are reordered most frequently (display their names and product IDs)?
# To find the top 20 most frequently reordered items:
# Filter the data: Use order_products['reordered'] == 1 to isolate only the products that have been reordered.
# Merge the datasets: Combine the filtered order_products with the products dataset on product_id to get both the product names and IDs.
# Group the data: Group by both product_id and product_name to calculate how many times each product was reordered, using .size().
# Sort the results: Use .sort_values(ascending=False) to rank the products by reorder frequency.
# Display the top 20: Use .head(20) to focus on the most frequently reordered products.
# Visualize the data: Create a bar chart to showcase the top reordered items and their frequencies.
# This process highlights the products that customers consistently return to and reorder.
# Filter order_products to include only reordered items
reordered_items = order_products[order_products['reordered'] == 1]
# Merge reordered_items with products on product_id
merged_reordered_data = pd.merge(reordered_items, products, on='product_id')    
# Display the top 20 most frequently reordered items
top_20_reorders = merged_reordered_data.groupby(['product_id', 'product_name']).size().sort_values(ascending=False).head(20)
# Plot a bar chart to visualize the top 20 most frequently reordered items
plt.figure(figsize=(12, 8))
plt.bar(top_20_reorders.index.get_level_values('product_name'), top_20_reorders.values)
plt.xlabel('Product Name')  # Corrected the x-axis label
plt.ylabel('Number of Reorders')    # Corrected the y-axis label
plt.title('Top 20 Most Frequently Reordered Items')   # Corrected the title label
plt.xticks(rotation=45) # Rotate x-axis labels for better readability
plt.show()  

# [C3] For each product, what proportion of its orders are reorders?
# To calculate the proportion of orders for each product that are reorders:
# Merge the datasets: Combine order_products with the products dataset to access product names and IDs in the same DataFrame.
# Group the data: Group by product_id and product_name to isolate each product's order history.
# Calculate the mean of reordered: Use .mean() on the reordered column to compute the proportion of orders for each product that were reorders. The value represents the reorder rate.
# Sort the results: Use .sort_values(ascending=False) to rank products by their reorder rates.
# Convert to a DataFrame: Use .reset_index() to organize the grouped data into a readable DataFrame.
# Optional Sorting: Sort the results by product_id or another column for better clarity.
# This approach provides insights into how frequently each product is reordered, helping identify customer favorites or staples.
# Merge order_products with products on product_id
merged_data = pd.merge(order_products, products, on='product_id')
# Group by product_id and product_name, and calculate the mean of reordered for each product
reorder_proportions = merged_data.groupby(['product_id', 'product_name'])['reordered'].mean().sort_values(ascending=False)
# Convert to a DataFrame and reset the index
reorder_proportions_df = reorder_proportions.reset_index()
# Display the top 20 products by reorder proportion
print(reorder_proportions_df.head(20))

# [C4] For each customer, what proportion of their products ordered are reorders?
# To calculate the proportion of products reordered by each customer:
# Merge the datasets: Combine order_products with orders to link order and customer information.
# Group the data: Group by user_id to focus on each customer's ordering behavior.
# Calculate the mean of reordered: Use .mean() on the reordered column to determine the proportion of products reordered by each customer.
# Sort the results: Use .sort_values(ascending=False) to identify customers with the highest reorder rates.
# Convert to a DataFrame: Use .reset_index() to format the grouped data into a structured DataFrame for further analysis.
# This analysis reveals the extent to which individual customers reorder products, providing insights into customer loyalty and preferences.

merged = order_products.merge(orders[['order_id', 'user_id']], on='order_id', how='left')
merged['reordered'] = merged['reordered'].astype(int)
customer_stats = (
    merged.groupby('user_id')['reordered']
    .agg(prop_reordered='mean', total_products='count', total_reorders='sum')
    .reset_index()
    .sort_values('prop_reordered', ascending=False)
)
print(customer_stats.head(20))

# [C5] What are the top 20 items that people put in their carts first?
# To identify the top 20 items that people most frequently add to their carts first:
# Merge the datasets: Combine order_products with products to link product names and IDs.
# Filter the data: Focus on rows where add_to_cart_order equals 1, indicating the first item added to the cart.
# Group the data: Group by product_id and product_name to aggregate the count of how often each product was the first in a cart.
# Count occurrences: Use .count() to calculate the total number of times each product was the first added.
# Sort the results: Use .sort_values(ascending=False) to rank products by their first-in-cart frequency.
# Display the top 20: Use .head(20) to extract the most popular first-in-cart items.
# This provides insights into which products customers prioritize in their shopping process.


# 1) Merge to attach product_name to each order_product row
merged = order_products.merge(products[['product_id', 'product_name']], on='product_id', how='left')

# 2) Ensure add_to_cart_order is numeric and filter for first item added (== 1)
merged['add_to_cart_order'] = pd.to_numeric(merged['add_to_cart_order'], errors='coerce')
first_items = merged[merged['add_to_cart_order'] == 1]

# 3) Count how often each product was the first in cart
first_counts = (
    first_items
    .groupby(['product_id', 'product_name'])
    .size()
    .reset_index(name='first_count')
    .sort_values('first_count', ascending=False)
)

# 4) Top 20
top20_first = first_counts.head(20)
print(top20_first)
# or use .nlargest(20, 'first_count') to be slightly faster for large data