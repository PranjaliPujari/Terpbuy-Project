#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python   #connecting my sql with python.')


# In[2]:


import mysql.connector    #importing required libraries
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')


# In[3]:


conn = mysql.connector.connect(host='127.0.0.1', database='terpbuy', user='root', password='pranjali@1991') #connecting database in mysql


# ## Q.1 Write a query to show the quantity of items sold by each department. Sort the results by department name.

# In[4]:


dataframe_sold_quantity = pd.read_sql('SELECT  department.department_name, count(order_line.quantity_sold)as sold_quantity                                    FROM terpbuy.product                                    inner join order_line on product.product_id = order_line.product_id                                    inner join department on department.department_id = product.department_id                                    group by department.department_name;', conn) #joining various tables to get result.
dataframe_sold_quantity                                   #showing department_name and sold_quantity by inner joining tables


# # Q.2 Using the query you wrote in Question 1, create a data visualization (e.g., a bar chart) showing all departments and the number of items each of them sold. Using a markdown cell, explain what you observe from the analysis.

# In[5]:


import matplotlib.pyplot as plt  #importing matplotlib library which will be used for data visualization purpose.


# In[6]:


from matplotlib import pyplot as plt
import numpy as np

sold_quantity = [1556,772,319,1252,310,120,285,64,54,12,39]
department_name=['Fan Shop', 'Golf', 'Footwear', 'Apparel', 'Outdoors' , 'Fitness' , 'Discs Shop' , 'Health and Beauty' , 'Pet Shop' , 'Book Shop' , 'Technology']
dataframe_sold_quantity.plot(kind='bar',x='department_name', y='sold_quantity',figsize=(10,6));          #visualizing data in bar chart
plt.title('Total sales quantity per department')                                                         #plotting name of bar chart is 'Total sales quantity per department'
plt.xlabel('department_name')                                                                            #plotting department names on x axis
plt.ylabel('sold_quantity')                                                                              #plotting sold quantity on y axis
for index, value in enumerate (dataframe_sold_quantity['sold_quantity']):
    plt.text(index, value, str(value),fontsize=8)
plt.show()


# ## Q.3 Write a query to show the number of orders placed in each year in which at least one order was placed. 

# In[7]:


dataframe_total_orders= pd.read_sql('SELECT YEAR(orders.order_date)as year, COUNT(DISTINCT orders.order_id) as total_orders_placed                             FROM Orders                              JOIN customer ON orders.customer_id = customer.customer_id                              GROUP BY YEAR(orders.order_date);',conn)     #joining customer and orders table.
dataframe_total_orders                  #the number of orders placed in each year in which at least one order was placed. 


# ## Q4. Using the query you wrote in Question 3, create a data visualization (e.g., a line graph) showing all years and the number of orders placed during each year, to see if there is a trend in ordering. 

# In[8]:


year = dataframe_total_orders.year                            #showing all years
orders = dataframe_total_orders.total_orders_placed           #showing number of orders

plt.plot(year,orders)                               
plt.title('No.of orders pleaced each year')            #plotting the title of line graph
plt.xlabel('Years')                                    #plotting years on x axis 
plt.ylabel('No. of orders')                            #plotting orders on Y axis
plt.show()

#In 2018 total orders was 585. In next year i.e in 2019 total orders has increased.
#But in next two years total orders rate is reduced to a great extent.The graph of orders placed is declined.
#So necessary steps have to be executed as order rate is getting reduced to a great extend day by day. 

