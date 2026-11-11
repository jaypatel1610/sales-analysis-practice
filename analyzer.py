# import os

# print("Current directory : " , os.getcwd())


# data_path = "../../python/maths.py"  

# if os.path.exists(data_path):
#     print(f"✅Found {data_path} ")

# else:
#     print(f"Cannot❌ find {data_path}")
# ==================================================================================
# import os
# import pandas as pd
# import json

# # PRINT THE DATA
# df = pd.read_csv("data/sales.csv")
# print(f"CSV DATA : /n {df}")
# print(f"Data has {df.shape[0]} rows and {df.shape[1]} columns.")

# # CALCULATE TOTAL FOR EACH ROW
# df['total'] = df['quantity'] * df['price']
# print(f"DF with total  /n {df}")

# #Convert it to json file
# df.to_json("output/sales_data.json" , orient= "records")

# #Convert it to csv file
# df.to_csv("output/sales_data.csv" , index=False)

# #Convert it to excel filse


# print("All Files Saved : ")


import pandas as pd
from helpers import calculate_total , format_currency

divider =  "--------------------------------------------"
df = pd.read_csv("data/sales.csv")
print(df)
print(divider)
totals = []

for index , row in df.iterrows():
    total = calculate_total(row['quantity'],row['price'])
    totals.append(total)

df ['total'] = totals

print(df)
print(divider)

for index , row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']} : {formatted_total}")

grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)

print(divider)

print(f"Grand total : {formatted_grand_total}")
