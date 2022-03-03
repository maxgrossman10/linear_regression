# %%

import pandas as pd
import sqlalchemy
import db_conf as dbc

path_to_dirty_data = """C:\Projects\csv_python\dirty_data.csv"""
dirty_data = pd.read_csv(path_to_dirty_data)

dirty_data.head()




# %%
