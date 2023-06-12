# read the input data
days, threshold, cash = [int(i) for i in input().split(",")]
buy_prices = [int(i) for i in input().split(",")]
sell_prices = [int(i) for i in input().split(",")]
stock_price = [int(i) for i in input().split(",")]

# calculate the daily cash considering the daily stock price and different strategies
max_cash = 0
for buy_price, sell_price in zip(buy_prices, sell_prices):
    stocks_held = 0
    curr_cash = cash
    for i in range(len(stock_price)):
        # sell all stocks on the last day
        if i == len(stock_price) - 1:
            curr_cash += stock_price[i] * stocks_held
            break
        # if buying condition is satisfied
        if stock_price[i] <= buy_price:
            curr_buy = curr_cash // 2 // stock_price[i]
            stocks_held += curr_buy
            curr_cash -= curr_buy * stock_price[i]
        # if selling condition is satisfied
        elif stock_price[i] >= sell_price:
            curr_sell = stocks_held // 2
            stocks_held -= curr_sell
            curr_cash += curr_sell * stock_price[i]
    if curr_cash > max_cash: max_cash = curr_cash
print(max_cash)