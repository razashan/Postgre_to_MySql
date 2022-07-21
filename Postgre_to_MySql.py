#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install psycopg2')


# In[70]:


import psycopg2 as pg
import pymysql
import pandas.io.sql as psql
from sqlalchemy import create_engine


# In[72]:


connection = pg.connect("host=10.66.210.149 dbname=service_monitoring user=smc_cisco password=LQSif0K")


# In[73]:


connection


# In[83]:


dataframe = psql.read_sql("select * from v_cisco_hpd_help_desk_tech",connection)


# In[85]:


my_conn = create_engine("mysql+mysqldb://root:cisco123@localhost/sakila")


# In[86]:


dataframe.to_sql(con=my_conn,name='myqs',if_exists='append',index=False)


# In[ ]:




