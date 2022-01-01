import investpy as inv
import pandas as pd
import time
import numpy as np

from pandas.io.parsers import read_csv
countries = inv.stocks.get_stock_countries()

countries = ['united states']

first_start = 0
# overview = inv.get_stocks_overview(country = 'united states')
if first_start == 1:
    for i in countries:
        ov = inv.stocks.get_stocks_list(country = i)
        #print(ov, len(ov))

    result = pd.DataFrame(columns=['Ticker', 'Price', 'divident_value',
    'divident_in_persentage_now', 'divident_persentage', 'divident_type', 'last_divident_date'])

    for i in ov:
        result = result.append({'Ticker':i},  ignore_index=True)

    result.to_csv("data.csv", index=False)


def parse_dividents(sto):
    try:
        start_time = time.time()
        div_info = inv.stocks.get_stock_dividends(stock = sto, country = countries[0])
        comp_info =  inv.stocks.get_stock_recent_data(stock = sto, country = countries[0])
        print("--- %s seconds ---" % (time.time() - start_time))
    except:
        return 0
    return [comp_info.iloc[-1, 3], div_info.iloc[0,1],(div_info.iloc[0,1]/comp_info.iloc[-1, 3])*4*100,
      div_info.iloc[0,4],div_info.iloc[0,2],div_info.iloc[0,0]]


ind = 5
res = read_csv("data.csv")
for i in range(len(res["Price"])):
    print(res.iloc[i]['Price'])
    if (np.isnan(res.iloc[i,1])) :
        ind = i
        stock_data = parse_dividents(res.iloc[i,0])
        print(res.iloc[i,0],stock_data)
        if stock_data != 0:
            res.loc[i,['Price','divident_value','divident_in_persentage_now','divident_persentage',
            'divident_type','last_divident_date']] = stock_data
        elif (stock_data == 0):
            res.loc[i,['Price','divident_value','divident_in_persentage_now','divident_persentage',
            'divident_type','last_divident_date']] = [0,0,0,0,0,0]
        res.to_csv("data.csv", index=False)

# summarise = 0
# if summarise ==1:



# for i in ov:
#     stock_data = parse_dividents(i)
#     print(stock_data)
#     if stock_data != 0:
#         result = result.append(stock_data,  ignore_index=True)
# print(result)


# {'Ticker':sto,'Price': comp_info.iloc[-1, 3], 'divident_value':div_info.iloc[0,1],
#       'divident_in_persentage_now': (div_info.iloc[0,1]/comp_info.iloc[-1, 3])*4*100,
#       'divident_persentage':div_info.iloc[0,4],
#       'divident_type':div_info.iloc[0,2], 'last_divident_date':div_info.iloc[0,0]}
