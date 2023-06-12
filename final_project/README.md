# Environment Configuration
To configure your environment, run the snippet below.
```
pip3 install -r requirements.in
```

# Explanation For Every Program
- dataset.py : download the stock data from "yfinance" for later usage, and calculate the daily returns , buy and hold returns in advance. 
- models.py : all the strategies for testing, calculating returns, and optimizing the given parameters.
- main.py : this is the program to run the whole thing.

# Parameters
To run the main.py:
- stock name: please go to the yahoo finance to check the stock name first. (e.g. "2330.TW", "TSLA", "MSFT", ect.)
- days: the days to test. (e.g. 1000)
- capital: initial value of your asset. (e.g. 1000000)
- strategy: all the strategies correspond to a number, please check the hint in your terminal. (e.g. 2)
- others: depends on the strategie you choose, please check the hint in your terminal.

# Output
- A plot should pop up after running the main.py
- Your terminal should include three values: the best parameters, the daily returns, the strategy returns, respectively.

Have Fun.