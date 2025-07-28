import pandas as pd 
import sqlite3

conn = sqlite3.connect('chinook.db')

# Show list of tables
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

conn.close()

conn = sqlite3.connect('chinook.db')
df1=pd.read_sql_query('select*from customers',conn)
conn.close()

# Customer Purchases Analysis:
# Find the total amount spent by each customer on purchases (considering invoices).
conn = sqlite3.connect('chinook.db')
df2=pd.read_sql_query('select*from invoices',conn)
conn.close()

grouped=df2.groupby('CustomerId')

# df2.sort_values(by='CustomerId',ascending=True)

summed=grouped.agg({'Total':'sum'})

grouped=df2.groupby('CustomerId')
# df2.sort_values(by='CustomerId',ascending=True)
summed=grouped.agg({'Total':'sum'})
summed

df_concatted = df1.merge(summed, on='CustomerId', how='inner')

selected_df = df_concatted[['CustomerId','FirstName', 'LastName', 'Total']]
selected_df


# Identify the top 5 customers with the highest total purchase amounts.
# Display the customer ID, name, and the total amount spent for the top 5 customers.

sorted_df=selected_df.sort_values(by='Total',ascending=False)
sorted_df.head()


# Album vs Individual Track Purchases:

conn_album = sqlite3.connect('chinook.db')
readed_album = pd.read_sql_query('select*from albums',conn_album)
readed_album


readed_artist = pd.read_sql_query('select*from artists',conn_album)
readed_artist

readed_customers = pd.read_sql_query('select*from customers',conn_album)
readed_customers


# Determine the percentage of customers who prefer to buy individual tracks instead of full albums.


readed_invoice_items = pd.read_sql_query('select*from invoice_items',conn_album)
readed_invoice_items


df_invoice = readed_invoice_items.groupby('InvoiceId')
counted_quantity = df_invoice.agg({'Quantity':'count'})
single_quantity = counted_quantity[counted_quantity['Quantity'] == 1]


single_quantity       #asosiylaridan biri


counted_id = grouped.agg({'CustomerId':'size'})
counted_id

readed_invoice = pd.read_sql_query('SELECT * FROM invoices', conn_album)

single_invoice_with_customer = single_quantity.merge(readed_invoice, on='InvoiceId')

# A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album
# Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).




individual_buyers = single_invoice_with_customer['CustomerId'].unique()
total_customers = readed_customers['CustomerId'].nunique()


num_individual_buyers = len(individual_buyers)

percent_individual_buyers = (num_individual_buyers / total_customers) * 100

print(f"{percent_individual_buyers:.2f}% of customers bought only individual tracks.")
percent_individual_buyers
