
# %%
## Importing a csv file into MySQL

import pandas      
import sqlalchemy
import db_conf as dbc  ## This is Mysql login credentials

cpi_data_file_path = """C:\Projects\csv_python\cpi_data.csv"""
cpi_data = pandas.read_csv(cpi_data_file_path)
##cpi_data.head() ##This is just to see if it works so far
## This has only read a csv file into python 


engine = sqlalchemy.create_engine(
    f"mysql+pymysql://{dbc.username}:{dbc.password}@{dbc.hostname}/{dbc.dbname}"
    )
## This connects us to MySQL


cpi_data.to_sql('consumer_data',engine,index=False)
#This creates a table named consumer_data MySQL


read_df = pandas.read_sql('SELECT * FROM stock.consumer_data',engine)
read_df.head(10)
## This reads in 10 rows of data FROM MySQL.





# %%
import pandas as pd
import sqlalchemy
import db_conf as dbc

heart_data_path = """C:\Projects\csv_python\heart_data.csv"""

heart_data = pd.read_csv(heart_data_path)

engine = sqlalchemy.create_engine(
    f"mysql+pymysql://{dbc.username}:{dbc.password}@{dbc.hostname}/{dbc.dbname}"
    )

heart_data.to_sql('heart_data',engine,index=False)


read_df = pd.read_sql('SELECT * FROM heart_data',engine)
read_df.head(15)


# %%
