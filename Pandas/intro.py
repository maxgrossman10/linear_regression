# %%

import pandas as pd

a = ([1,2,3],[4,5,6])

ser = pd.Series(a)

print(ser[0])


# %%
import pandas as pd

a = ([1,2,3],[4,5,6])

ser = pd.Series(a, index = ["x","y"])

print(ser["x"])


# %%
import pandas as pd

x = ([110,112,131,111],[57,60,55,59])

data = pd.Series(x, index = ["Revenue","COGS"])

print(data)


# %%
import pandas as pd

data = {"day1":100, "day2":200, "day3":300}

data = pd.Series(a)

print(data)


# %%

import pandas as pd

data = {"Revenue":[100,200,300],"COGS":[50,60,70]}

df = pd.DataFrame(data)

print(df)

print(df.loc[0])

# %%
import pandas as pd

data = {"Wood lbs":[5000,4900,5050,5100],"House ft":[2000,1900,2100,2200]}

df = pd.DataFrame(data, index = ["house1","house2","house3","house4"])

print(df)


