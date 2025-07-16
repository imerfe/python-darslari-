# Homework 1:

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# # Rename column names using function. "First Name" --> "first_name", "Age" --> "age"
# a=df.rename(columns={'First Name':'first_name',"Age":"age","City":"city"})
# a

# # Print the first 3 rows of the DataFrame
# a.head(3)

# Find the mean age of the individuals
# df
# average=df['Age'].mean()
# print(average)

# Select and print only the 'Name' and 'City' columns

# df.loc[:, ['First Name', 'City']]

# Add a new column 'Salary' with random salary values

import numpy as np 
ran=np.random.randn(4)*1000+5000
list=[]

for i in ran:
   list.append(i)

sr=pd.Series(list)

df['salary']=sr



# Display summary statistics of the DataFrame

df.describe()




# Homework 2:

# Create a DataFrame named sales_and_expenses with columns 
# 'Month', 'Sales', and 'Expenses',
# representing monthly sales and expenses data.
#  Use below table.

# Month	Sales	Expenses
# Jan	5000	3000
# Feb	6000	3500
# Mar	7500	4000
# Apr	8000	4500

dat= {'Month':['Jan','Feb','Mar','Apr'],'Sales':[5000,6000,7500,8000],'Expenses':[3000,3500,4000,4500]}
dtf=pd.DataFrame(dat)


# Calculate and display the maximum sales and expenses.
# Calculate and display the minimum sales and expenses.
mxS=dtf['Sales'].max()
mnS=dtf['Sales'].min()
mnE=dtf['Expenses'].min()
mxE=dtf['Expenses'].max()

print('max and min value of sales',mxS,mnS)
print('max and min value of expenses',mxE,mnE)


# Calculate and display the average sales and expenses.
avg=dtf[['Sales','Expenses']].mean()
avg


# Homework 3:

# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', 
# representing monthly expenses for different categories. 
# Use below table.

# Category	January	February	March	April
# Rent	1200	1300	1400	1500
# Utilities	200	220	240	250
# Groceries	300	320	330	350
# Entertainment	150	160	170	180
import pandas as pd 
expenses={
    'Category':['rent','utilities','groceries','entertainment'],
    'January':[1200,1300,1400,1500],
    'February':[200,220,240,250],
    'March':[300,320,330,350],
    'April':[150,160,170,180]}

exp=pd.DataFrame(expenses)


# Calculate and display the maximum expense for each category.
# Calculate and display the minimum expense for each category.
# Calculate and display the average expense for each category.
exp['max_expense']=exp[['January', 'February', 'March', 'April']].max(axis=1)
exp['min_expense']=exp[['January', 'February', 'March', 'April']].min(axis=1)
exp['avg_expense']=exp[['January', 'February', 'March', 'April']].mean(axis=1)
exp

# In this task, use .set_index method to make Category column as index.
exp.set_index('Category')





