import pandas as pd
import math

class Asset:
    def __init__(self, icon, average_price, current_price, quantity):
        self.icon = icon
        self.average_price = average_price
        self.current_price = current_price
        self.quantity = quantity
        self.initial_balance = round(average_price * quantity, 2)
        self.current_balance = round(current_price * quantity, 2)
        self.returns = round(((self.current_balance / self.initial_balance) - 1) * 100, 3)

    def __repr__(self):
        return f"Asset(icon={self.icon}, average_price={self.average_price}, current_price={self.current_price}, quantity={self.quantity}, initial_balance={self.initial_balance}, current_balance={self.current_balance}, returns={self.returns})"


assets = []
total_initial_portfolio = 0
total_current_portfolio = 0
portfolio_returns = 0

net_monthly_return = 1.2555


df = pd.read_csv('dados.csv', delimiter=';')

for index, row in df.iterrows():
    new_asset = Asset(row['icon'], row['average_price'], row['current_price'], row['quantity'])
    assets.append(new_asset)
    total_initial_portfolio += new_asset.initial_balance
    total_current_portfolio += new_asset.current_balance

for asset in assets:
    portfolio_returns += ((asset.initial_balance / total_initial_portfolio) * asset.returns)

portfolio_net_returns = total_initial_portfolio * portfolio_returns / 100

print('Rentabilidade do portfolio:', round(portfolio_returns, 2))
print('Rentabiliadde do portfolio, em reais: R$', round(portfolio_net_returns, 2))

if portfolio_net_returns < 0:
    time = math.log(1 + (portfolio_net_returns * -1 / total_current_portfolio), (1 + (net_monthly_return/100)))
    print('Tempo, em meses, para recuperar o valor perdido: ', round(time, 2))