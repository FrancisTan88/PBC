# read the input data
days, cash = [int(i) for i in input().split(",")]
stock_price = [int(i) for i in input().split(",")]
buy_price, sell_price = [int(i) for i in input().split(",")]
stocks_held = 0
curr_buy, curr_sell = 0, 0

# calculate the daily cash considering the daily stock price
for i in range(len(stock_price)):
    # sell all stocks on the last day
    if i == len(stock_price) - 1:
        cash += stock_price[i] * stocks_held
        break
    # if buying condition is satisfied
    if stock_price[i] <= buy_price:
        curr_buy = cash // 2 // stock_price[i]
        stocks_held += curr_buy
        cash -= curr_buy * stock_price[i]
    # if selling condition is satisfied
    elif stock_price[i] >= sell_price:
        curr_sell = stocks_held // 2
        stocks_held -= curr_sell
        cash += curr_sell * stock_price[i]
print(cash)