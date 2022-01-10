import investpy as inv
import pandas as pd
import time
import numpy as np
import datetime
from pandas.io.parsers import read_csv

res = read_csv("data.csv")

stamp = datetime.datetime.strptime("2021-01-01","%Y-%m-%d")
res = res[res['Price'] != 0]
res = res.dropna()
#вибираємо тільки ті що платили в 21 році

for i in range(len(res["Price"])):
    datek = datetime.datetime.strptime(res.iloc[i,6], "%Y-%m-%d %H:%M:%S")
    if datek < stamp :
        res.iloc[i, 4] = 0
        print(datek, stamp,res.iloc[i,4])

res = res[res['divident_persentage'] != 0]
# for i in range(len(res["Price"])):
#     if res.iloc[i,5] != 'quarterly':
#         res.loc[i,['Price','divident_value','divident_in_persentage_now','divident_persentage',
#             'divident_type','last_divident_date']] = [0,0,0,0,0,0]

res = res[res['divident_type'] == 'quarterly']
res = res.sort_values(by=['divident_in_persentage_now'], ascending=False)
res.reset_index(drop=True, inplace=True)
print(res)

res.to_excel("output.xlsx")
