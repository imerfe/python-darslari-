import pandas as pd 
sales=pd.read_csv('sales_data.csv')
sales

# Homework Assignment 1: Analyzing Sales Data

# You are given a dataset containing sales data for an e-commerce website. 
# The dataset (task\sales_data.csv) has the following columns:
# Date: Date of the sale.
# Product: Name of the product sold.
# Category: Category to which the product belongs.
# Quantity: Number of units sold.
# Price: Price per unit.


# Tasks:
# Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.
# Identify the top-selling product in each category based on the total quantity sold.
# Find the date on which the highest total sales (quantity * price) occurred.

group=sales.groupby(['Category']).agg({'Quantity':['sum','max'],'Price':'mean'})

group_sum=sales.groupby(['Category','Product'])['Quantity'].sum().reset_index()

grouped_max_sold=group_sum.sort_values(['Category','Quantity'], ascending=[True,False]).reset_index()

top_selling=grouped_max_sold.groupby('Category').first().reset_index()

# print(f'{group}"\n"{top_selling}')

sales

def total_sales(x):
    return (x['Quantity'] * x['Price']).sum()
    

tot = sales.groupby('Date').apply(total_sales).reset_index()
top=tot.groupby(['Date']).first().reset_index()
top


import pandas as pd 
# Homework Assignment 2: Examining Customer Orders
# You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:

# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# Tasks:

readed=pd.read_csv('customer_orders.csv')
readed

# Group the data by CustomerID and filter out customers who have made less than 20 orders.

grouped=readed.groupby('CustomerID')
grouped

cnt=grouped['OrderID'].agg('size').reset_index()
cnt

f=cnt[cnt['OrderID']<=20]
f



# Identify customers who have ordered products with an average price per unit greater than $120.
readed

avg=grouped['Price'].agg('mean').reset_index()
avg

completed=avg[avg["Price"]>120]
completed



# Find the total quantity and total price for each product ordered, 
# and filter out products that have a total quantity less than 5 units.

producted_gr=readed.groupby('Product')
total_price_qu=producted_gr.agg({'Quantity':'sum','Price':'sum'})
a=total_price_qu.sort_values(['Quantity','Price'],ascending=[False,False])
less=a[a['Quantity']<5]
less


# Homework Assignment 3: Population Salary Analysis
import sqlite3

# "task\population.db" sqlite database has population table.
conn=sqlite3.connect('population (1).db')

population=pd.read_sql_query('SELECT*FROM population',conn)
conn.close()

population.reset_index()

# "task\population salary analysis.xlsx" file defines Salary Band categories.

pop_sal=pd.read_excel('population_salary_analysis.xlsx')

pop_sal

# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;

def categorize(s):
    if  s<200000:
        a='till $200,000'
    elif s<400000:
        a='$200,001 - $400,000'
    elif s<600000:
        a='$400,001 - $600,000'
    elif s<800000:
        a='$600,001 - $800,000'
    elif s<1000000:
        a='$800,001 - $1,000,000'
    elif s<1200000:
        a='$1,000,001 - $1,200,000'
    elif s<1400000:  
        a='$1,200,001 - $1,400,000'
    elif s<1600000:  
        a='$1,400,001 - $1,600,000'
    elif s<1800000:  
        a='$1,600,001 - $1,800,000'
    elif s>1800000:  
        a='over'
    return a



population['salary_category']=population['salary'].apply(categorize)


population['salary_category'].value_counts().reset_index()

total = population['salary_category'].count()
df1 = population['salary_category'].value_counts()/total*100


df1

population['% ulushda']=df1

population

# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;

population

sal_cat=population.groupby('salary_category')
sal_cat

avg=sal_cat.agg({'salary':['mean','median'],'id':'count'})

population
avg


df2=(
    population.groupby('salary_category').agg(
        average_salary=pd.NamedAgg(column="salary",aggfunc="mean"),
        median_salary=pd.NamedAgg(column='salary',aggfunc='median'),
        total_employee=pd.NamedAgg(column='id',aggfunc="count"))
)

df2


# Calculate the same measures in each State

df3=(
    population.groupby('state').agg(
        average_salary_by_state=pd.NamedAgg(column='salary',aggfunc='mean'),
        median_salary_by_state=pd.NamedAgg(column='salary',aggfunc='median'),
        population_volume=pd.NamedAgg(column='id',aggfunc='count')
    )
)

df3
