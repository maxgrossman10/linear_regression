# %%
## This will return the first and last 5 rows
import pandas as pd

df = pd.read_csv(r'C:\Projects\csv_python\amazon.csv')

df.head()



# %%
## This will print the maximum number of rows
import pandas as pd

df = pd.read_csv(r'C:\Projects\csv_python\amazon.csv')

print(df.to_string())


# %%
## This will print the first 5 rows or the amount specified in the ()
import pandas as pd

df = pd.read_csv(r'C:\Projects\csv_python\amazon.csv')

df.head(10)




# %%
## Importing csv data into python using paths
import pandas as pd

data_file_path = """C:\Projects\csv_python\data.csv"""
df = pd.read_csv(data_file_path)

print(df) 
