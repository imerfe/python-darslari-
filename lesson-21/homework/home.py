# DataFrame 1: Student Grades

import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1

# Exercise 1: Calculate the average grade for each student.

df1.set_index('Student_ID',inplace=True)

df1_mean=df1.mean(axis=1)
df1_mean

# Exercise 2: Find the student with the highest average grade.

highest_avg_grade=df1_mean.nlargest(1)
highest_avg_grade

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.

df1_sum=df1.sum(axis=1)
summed_df=pd.DataFrame(df1_sum,columns=['total'])
summed_df

df1.join(summed_df,how='inner',on='Student_ID')

# Exercise 4: Plot a bar chart to visualize the average grades in each subject.


df1.mean()


df_meaned_subjects=pd.DataFrame(df1.mean(),columns=['mean_grade'])
df_meaned_subjects
value=df1.mean()
category=df1.columns


import matplotlib.pyplot as plt

plt.bar(category,value,0.5,color=['red','grey','green'])
plt.xlabel('subjects')
plt.ylabel('grades')
plt.legend()
plt.title('average grade by subject')




# DataFrame 2: Sales Data
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
df2

# Exercise 1: Calculate the total sales for each product.

# df2.set_index('Date',inplace=True)

# df2_transposed=df2.transpose()

# grouped_df2 = df2_transposed.groupby('Date')
# result = grouped_df2.sum()  # yoki .mean(), .count(), .first(), .max() va hokazo
# print(result)


total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()

total_sales_df=pd.DataFrame(total_sales,columns=['total'])
total_sales_df

# Exercise 2: Find the date with the highest total sales.

gr=df2.groupby("Date")

summed_gr=gr[['Product_A', 'Product_B', 'Product_C']].sum()

cls=summed_gr.sum(axis=1)

cls.nlargest(1)

# Exercise 3: Calculate the percentage change in sales for each product from the previous day.

prct_change=cls.pct_change()
prct_change

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.
plt.plot(cls,marker='o',markersize=2,color='blue')


# DataFrame 3: Employee Information

import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department.

df3_grouped=pd.DataFrame(df3.groupby('Department')['Salary'].mean())
df3_grouped

# Exercise 2: Find the employee with the most experience.
df3.nlargest(1,'Experience (Years)')

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in 
# salary from the minimum salary in the dataframe.

min_salary=df3['Salary'].min()
min_salary

changing_pct=df3['Salary Increase']=((df3['Salary']-min_salary)/min_salary)*100
df3

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.

# grouped_df3=df3.groupby('Department')['Employee_ID'].count()

# categoriez=df3.columns['Department']

# # value=
# # plt.bar()


grouped_df3 = df3.groupby('Department')['Employee_ID'].count().reset_index()

categories = grouped_df3['Department']
values = grouped_df3['Employee_ID']

plt.bar(categories,values,color=['green','black','grey','pink'])
plt.xlabel('departments')
plt.ylabel('numbers')

plt.legend()


# DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Exercise 1: Calculate the total revenue from all orders.

df4.set_index('Order_ID',inplace=True)
summed_all=df4.groupby('Customer_ID')['Total_Price'].sum()

summed_all

# Exercise 2: Find the most ordered product.

popular=df4.groupby('Product')['Quantity'].sum()
popular.nlargest(1)


# Exercise 3: Calculate the average quantity of products ordered.

df4.groupby('Product')['Quantity'].mean()

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.


df4['revenue']=df4['Quantity']*df4['Total_Price']
grouped_df4=df4.groupby('Product')['revenue'].sum().reset_index()

labels=grouped_df4['Product']
colors = ['red','yellow','blue','green']
sizes=grouped_df4['revenue']

plt.pie(sizes, labels=labels, colors=colors, startangle=90)


