# Calculate XYZ's original stock purchase cost and brokerage
num_stock = 500
stock_buy_price = 25.04
stock_sell_price = 36.06
comp_rate = 0.23

#Calculate stock and commission with precision
stock_buy = num_stock * stock_buy_price
buy_comp = comp_rate * stock_buy

#Format buy output with currency
stock_pay = '${:,.2f}'.format(stock_buy)
buy_comp = '${:,.2f}'.format(buy_comp)

#Calculate XYZ Sell Price with precision
stock_sell = num_stock * stock_sell_price
sell_comp = comp_rate * stock_sell
profit = stock_sell - stock_buy

#Format sell output with currency
stock_sell = '${:,.2f}'.format(stock_sell)
sell_comp = '${:,.2f}'.format(sell_comp)
profit = '${:,.2f}'.format(profit)
sell_stock_str = '${:,.2f}'.format(stock_sell_price)

#Print to screen
print('XYZ paid', stock_pay, 'for', num_stock, 'units of stock')
print('Brokerage paid on purchase of', num_stock, 'units of stock was', buy_comp)
print('XYZ sold', num_stock, 'units of stock for', stock_sell)
print('Brokerage paid upon selling', num_stock, 'units of stock was', sell_comp)
print('XYZ made', profit, 'profit on selling', num_stock, 'units of stock at a sale price of', sell_stock_str)

#